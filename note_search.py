"""
Joplin Knowledge AI — модуль пошуку релевантних нотаток за ключовими словами.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Note:
    id: int
    title: str
    content: str
    tags: List[str]


def tokenize(text: str) -> List[str]:
    """Розбиває текст на слова в нижньому регістрі, без пунктуації."""
    cleaned = "".join(ch.lower() if ch.isalnum() or ch.isspace() else " " for ch in text)
    return [word for word in cleaned.split() if word]


def score_note(query_tokens: List[str], note: Note) -> int:
    """Рахує кількість збігів слів запиту з текстом нотатки (title+content+tags)."""
    note_text = " ".join([note.title, note.content, " ".join(note.tags)])
    note_tokens = set(tokenize(note_text))
    return sum(1 for token in query_tokens if token in note_tokens)


def search_notes(query: str, notes: List[Note], top_k: int = 3) -> List[Note]:
    """Повертає top_k нотаток, найбільш релевантних до запиту."""
    query_tokens = tokenize(query)
    scored = [(score_note(query_tokens, note), note) for note in notes]
    scored = [pair for pair in scored if pair[0] > 0]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [note for _, note in scored[:top_k]]