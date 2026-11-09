def get_extension(path: str) -> str:
    name = path.split("/")[-1]
    if "." not in name:
        return ""
    return name.rpartition(".")[2].lower()


def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        ext = get_extension(path)
        counts[ext] = counts.get(ext, 0) + 1
    return counts