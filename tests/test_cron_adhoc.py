from __future__ import annotations

from pathlib import Path

from cron.lib.adhoc import archive_completed, list_todo_markdown, repo_root, todo_dir


def test_repo_root_points_at_stateconscious() -> None:
    root = repo_root()
    assert (root / "src" / "lib" / "sources" / "my" / "parliament_my" / "seed_urls.txt").is_file()


def test_list_todo_excludes_readme() -> None:
    paths = list_todo_markdown()
    names = {p.name for p in paths}
    assert "README.md" not in names


def test_list_todo_includes_only_work_items(tmp_path: Path, monkeypatch) -> None:
    fake = tmp_path / "adhoc" / "todo"
    fake.mkdir(parents=True)
    (fake / "README.md").write_text("# instructions\n", encoding="utf-8")
    (fake / "_draft.md").write_text("x\n", encoding="utf-8")
    (fake / "real-task.md").write_text("do thing\n", encoding="utf-8")

    monkeypatch.setattr("cron.lib.adhoc.repo_root", lambda: tmp_path)
    paths = list_todo_markdown()
    assert [p.name for p in paths] == ["real-task.md"]


def test_archive_completed_moves_to_done(tmp_path: Path, monkeypatch) -> None:
    fake_adhoc = tmp_path / "adhoc"
    fake_todo = fake_adhoc / "todo"
    fake_done = fake_adhoc / "done"
    fake_todo.mkdir(parents=True)
    f = fake_todo / "testitem.md"
    f.write_text("hello\n", encoding="utf-8")

    def fake_root() -> Path:
        return tmp_path

    monkeypatch.setattr("cron.lib.adhoc.repo_root", fake_root)
    dest = archive_completed(f, footer="done: synced")
    assert dest == fake_done / "testitem.md"
    assert dest.read_text(encoding="utf-8").strip().endswith("done: synced")
    assert not f.exists()
