from __future__ import annotations

from lib.sources.my.parliament_my.error_pages import soft_error_label
from lib.sources.my.parliament_my.fetch import fetch_url


def test_soft_error_label_english() -> None:
    html = "<html><body>An error has occurred.</body></html>"
    assert soft_error_label(html) == "error_page: generic"


def test_soft_error_label_not_found_en() -> None:
    html = "<div>The requested page cannot be found.</div>"
    assert soft_error_label(html) == "error_page: not_found_en"


def test_soft_error_label_clean_page() -> None:
    html = "<html><a href='/bills'>RUU</a></html>"
    assert soft_error_label(html) is None


def test_fetch_url_marks_soft_200(monkeypatch) -> None:
    class Resp:
        status_code = 200
        content = b"<html>An error has occurred. The requested page cannot be found.</html>"

    def fake_get(*_a, **_k):
        return Resp()

    monkeypatch.setattr("lib.sources.my.parliament_my.fetch.requests.get", fake_get)
    r = fetch_url("https://www.parlimen.gov.my/test-soft", verify=True)
    assert r.http_status == 200
    assert r.status == "error"
    assert r.error is not None and "soft_200" in r.error
    assert r.meta.get("soft_http_error") is True
