"""
Adhoc inbox: human prompts under ``adhoc/todo``, archived under ``adhoc/done``.

No dependency on ``lib`` — safe to import from thin shell wrappers with only stdlib.
"""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def adhoc_root() -> Path:
    return repo_root() / "adhoc"


def todo_dir() -> Path:
    return adhoc_root() / "todo"


def done_dir() -> Path:
    return adhoc_root() / "done"


# Not treated as work items (instructions / templates only).
_TODO_SKIP_NAMES = frozenset({"readme.md"})


def _is_work_item_todo(path: Path) -> bool:
    name = path.name
    if not name.lower().endswith(".md"):
        return False
    if name.lower() in _TODO_SKIP_NAMES:
        return False
    if name.startswith("_"):
        return False
    return path.is_file()


def list_todo_markdown() -> list[Path]:
    """
    Sorted work-item ``*.md`` in ``adhoc/todo``.

    Excludes ``README.md`` (inbox instructions) and underscore-prefixed ``_*.md`` drafts.
    Nothing in this repo calls ``archive_completed`` automatically—only tests or explicit scripts.
    """
    d = todo_dir()
    if not d.is_dir():
        return []
    return sorted(p for p in d.glob("*.md") if _is_work_item_todo(p))


def archive_completed(todo_path: Path, *, footer: str) -> Path:
    """
    Append ``footer`` to ``todo_path`` content, write under ``adhoc/done/``, delete original.
    ``todo_path`` must live under ``adhoc/todo``.
    """
    todo_path = todo_path.resolve()
    base = todo_dir().resolve()
    if todo_path.parent.resolve() != base:
        raise ValueError(f"path must be a direct child of {base}: {todo_path}")
    done_dir().mkdir(parents=True, exist_ok=True)
    text = todo_path.read_text(encoding="utf-8")
    dest = done_dir() / todo_path.name
    dest.write_text(text.rstrip() + "\n\n---\n\n" + footer.strip() + "\n", encoding="utf-8")
    todo_path.unlink()
    return dest
