import math


def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}: {line!r}")

    city = parts[0].strip()
    temp_text = parts[1].strip()
    date = parts[2].strip()

    if not city or not date:
        raise ValueError(f"Пустой город или дата: {line!r}")

    try:
        temp = float(temp_text)
    except ValueError:
        raise ValueError(f"Температура не число: {temp_text!r}")

    if not math.isfinite(temp):
        raise ValueError(f"Недопустимая температура: {temp_text!r}")

    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records

def average_by_city(records: list[dict]) -> dict:
    sums = {}
    counts = {}
    for rec in records:
        city = rec["city"]
        sums[city] = sums.get(city, 0) + rec["temp"]
        counts[city] = counts.get(city, 0) + 1
    return {city: round(sums[city] / counts[city], 1) for city in sums}


def warmest_city(records: list[dict]) -> str:
    if not records:
        raise ValueError("Нет записей")

    sums = {}
    counts = {}
    for rec in records:
        city = rec["city"]
        sums[city] = sums.get(city, 0) + rec["temp"]
        counts[city] = counts.get(city, 0) + 1

    averages = {city: sums[city] / counts[city] for city in sums}
    best_value = max(averages.values())
    candidates = [city for city, avg in averages.items() if avg == best_value]
    return min(candidates)


def average_by_city(records: list[dict]) -> dict:
    sums = {}
    counts = {}
    for rec in records:
        city = rec["city"]
        sums[city] = sums.get(city, 0) + rec["temp"]
        counts[city] = counts.get(city, 0) + 1
    return {city: round(sums[city] / counts[city], 1) for city in sums}


def warmest_city(records: list[dict]) -> str:
    if not records:
        raise ValueError("Нет записей")

    sums = {}
    counts = {}
    for rec in records:
        city = rec["city"]
        sums[city] = sums.get(city, 0) + rec["temp"]
        counts[city] = counts.get(city, 0) + 1

    averages = {city: sums[city] / counts[city] for city in sums}
    best_value = max(averages.values())
    candidates = [city for city, avg in averages.items() if avg == best_value]
    return min(candidates)  # первый по алфавиту