LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


def parse_event(line: str) -> dict:
    parts = line.strip().split(None, 2)
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 части (время, уровень, сообщение): {line!r}")

    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"Неизвестный уровень {level!r}: {line!r}")

    return {"time": time, "level": level, "message": message}


def count_levels(lines: list[str]) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():  
            continue
        try:
            level = parse_event(line)["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            message = event["message"]
            counts[message] = counts.get(message, 0) + 1

    ordered = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return [[message, count] for message, count in ordered[:max(n, 0)]]