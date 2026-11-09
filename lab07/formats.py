import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    header = [name.strip() for name in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [value.strip() for value in line.split(",")]
        records.append(dict(zip(header, values)))
    return records


def _convert(value: str):
    lowered = value.lower()
    if lowered in ("true", "yes"):
        return True
    if lowered in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        return value


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None

    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue

        if line.startswith("-"):
            if current_list is not None:
                current_list.append(_convert(line[1:].strip()))
            continue

        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value == "":
            current_list = []
            settings[key] = current_list
        else:
            current_list = None
            settings[key] = _convert(value)

    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged = []
    for row in rows:
        info = extra.get(row.get(key), {})
        merged.append({**info, **row})
    return merged


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)