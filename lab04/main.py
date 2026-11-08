import sys

from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)

    non_empty = [line for line in lines if line.strip()]
    skipped = len(non_empty) - len(records)

    print(len(records))
    print(skipped)

    if records:
        averages = average_by_city(records)
        best = warmest_city(records)
        print(f"{averages[best]:.1f}")
    else:
        print("нет данных")


if __name__ == "__main__":
    main()