import sys
from pathlib import Path

from logstats import count_levels, format_report, top_errors

BASE_DIR = Path(__file__).resolve().parent
TOP_N = 3


def find_log(name: str) -> Path:
    path = Path(name)
    if path.exists():
        return path
    return BASE_DIR / name


def main():
    name = sys.stdin.readline().strip()
    path = find_log(name)

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, TOP_N)

    print(sum(counts.values()))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))

    report = format_report(counts, errors)
    with open(BASE_DIR / "report.txt", "w", encoding="utf-8", newline="\n") as out:
        out.write(report)


if __name__ == "__main__":
    main()