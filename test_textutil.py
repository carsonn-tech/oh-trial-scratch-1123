from textutil import slugify, word_count

def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"

def test_slugify_runs():
    assert slugify("a  --  b") == "a-b"

def test_word_count_whitespace():
    assert word_count("a  b\tc\nd") == 4
