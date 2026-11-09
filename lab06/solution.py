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


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda path: (-path.count("/"), path))


UNITS = ["Б", "КБ", "МБ", "ГБ", "ТБ"]


def human_size(n_bytes: int) -> str:
    size = float(n_bytes)
    unit = 0
    while size >= 1024 and unit < len(UNITS) - 1:
        size /= 1024
        unit += 1

    if unit == 0:
        return f"{n_bytes} Б"

    if round(size, 1) >= 1024 and unit < len(UNITS) - 1:
        size /= 1024
        unit += 1

    return f"{size:.1f} {UNITS[unit]}"