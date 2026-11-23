def slugify(s):
    """Lowercase, replace runs of non-alphanumerics with one hyphen, strip hyphens."""
    out = ""
    for ch in s:
        out += ch.lower() if ch.isalnum() else "-"
    return out.strip("-")


def word_count(s):
    return len(s.split(" "))
