"""
Live integration: export one year to CSV, pick a random ``pdf_url``, confirm ``%PDF`` at start.

Requires network. **Pytest does not read ``.env`` on its own** — this repo’s ``tests/conftest.py``
loads only keys named ``PARLIAMENT_LIVE_*`` from the repo-root ``.env``.

Put in ``.env`` (no spaces around ``=`` is fine)::

    PARLIAMENT_LIVE_CSV_TEST=1
    PARLIAMENT_LIVE_CSV_YEAR=2024
    PARLIAMENT_LIVE_CSV_MAX_NODES=100

Default ``pytest`` **excludes** this test (``-m "not live_parliament"`` in ``pytest.ini``).
Run the live check explicitly from the ``stateconscious`` directory::

    python -m pytest tests/test_parliament_live_year_csv_pdf.py -m live_parliament

There is no separate script — only this test module.
"""

from __future__ import annotations

import csv
import os
import random
import tempfile
from pathlib import Path

import pytest

from lib.sources.my.parliament_my.dhtmlx_arkib import (
    arkib_page_url_with_lang_en,
    drop_bm_billindex_urls,
    list_bill_records_arkib_dhtmlx_sweep,
    resolve_arkib_bill_pdf_urls,
    write_arkib_bills_csv_by_year,
)
from lib.sources.my.parliament_my.fetch import probe_pdf_magic

pytestmark = pytest.mark.live_parliament

ARKIB_PAGE = "https://www.parlimen.gov.my/bills-dewan-rakyat.html?uweb=dr&arkib=yes"


@pytest.mark.skipif(
    not os.environ.get("PARLIAMENT_LIVE_CSV_TEST"),
    reason="Set PARLIAMENT_LIVE_CSV_TEST=1 to run live parliament CSV + PDF checks",
)
def test_year_csv_random_row_is_pdf_magic() -> None:
    target_year = os.environ.get("PARLIAMENT_LIVE_CSV_YEAR", "2024")
    max_nodes = int(os.environ.get("PARLIAMENT_LIVE_CSV_MAX_NODES", "250"))

    rows, probe_cookies = list_bill_records_arkib_dhtmlx_sweep(
        ARKIB_PAGE,
        verify_tls=False,
        max_nodes=max_nodes,
        verbose=False,
        log=None,
    )
    year_rows = [r for r in rows if (r.get("year") or "").strip() == target_year]
    if not year_rows:
        pytest.skip(f"No bill rows for year {target_year!r} (try another PARLIAMENT_LIVE_CSV_YEAR)")

    # Resolve only this year — full-archive resolve is too slow for a default live test.
    resolve_arkib_bill_pdf_urls(
        year_rows,
        verify_tls=False,
        verbose=False,
        log=None,
        probe_cookies=probe_cookies if probe_cookies else None,
    )
    drop_bm_billindex_urls(year_rows)

    with tempfile.TemporaryDirectory() as td:
        out_dir = Path(td)
        written = write_arkib_bills_csv_by_year(year_rows, out_dir)
        year_file = out_dir / f"bills_{target_year}.csv"
        assert year_file.exists(), f"expected {year_file}, got {written!r}"

        with year_file.open(encoding="utf-8-sig", newline="") as f:
            table = list(csv.DictReader(f))

        urls = [(r.get("pdf_url") or "").strip() for r in table if (r.get("pdf_url") or "").strip()]
        if not urls:
            pytest.skip(f"No pdf_url in bills_{target_year}.csv after resolve/BM drop")

        url = random.choice(urls)
        page_en = arkib_page_url_with_lang_en(ARKIB_PAGE)
        hdrs = {"Referer": page_en}
        ok = probe_pdf_magic(
            url,
            verify=False,
            headers=hdrs,
            cookies=probe_cookies if probe_cookies else None,
        )
        assert ok, f"Expected PDF magic for {url!r} (picked from {len(urls)} candidate(s))"
