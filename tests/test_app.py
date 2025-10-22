from app.app import dedupe_list

def test_dedupe_list():
    data = ["a", "b", "a", "c", "b"]
    expected = ["a", "b", "c"]
    assert dedupe_list(data) == expected
