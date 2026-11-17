"""Модульні тести для note_search.py (запускаються через pytest)."""

from note_search import Note, tokenize, score_note, search_notes


def make_notes():
    return [
        Note(1, "Python основи", "Змінні, типи даних, цикли for і while", ["python", "навчання"]),
        Note(2, "Нейронні мережі", "Перцептрон, функції активації, backpropagation", ["ml", "нейромережі"]),
        Note(3, "Проєкт: чат-бот", "Архітектура чат-бота на основі RAG та Python", ["проєкт", "python", "ml"]),
    ]


def test_tokenize_basic():
    assert tokenize("Привіт, світ!") == ["привіт", "світ"]


def test_tokenize_empty_string():
    assert tokenize("") == []


def test_score_note_counts_matches():
    notes = make_notes()
    query_tokens = tokenize("python проєкт")
    assert score_note(query_tokens, notes[2]) == 2  # "python" і "проєкт" збігаються
    assert score_note(query_tokens, notes[1]) == 0  # жодного збігу


def test_search_notes_returns_relevant_first():
    notes = make_notes()
    results = search_notes("python проєкт", notes)
    assert results[0].id == 3  # найбільше збігів


def test_search_notes_respects_top_k():
    notes = make_notes()
    results = search_notes("python", notes, top_k=1)
    assert len(results) == 1


def test_search_notes_no_match_returns_empty():
    notes = make_notes()
    results = search_notes("квантова фізика", notes)
    assert results == []
