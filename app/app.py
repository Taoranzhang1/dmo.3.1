def dedupe_list(items):
    """Remove duplicates preserving order."""
    seen = set()
    result = []
    for i in items:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


if __name__ == "__main__":
    data = ["a", "b", "a", "c", "b"]
    print("input:", data)
    print("output:", dedupe_list(data))