def parse_record(line: str) -> dict:
    city, temp, date = line.split(";")
    return {"city": city, "temp": float(temp), "date": date}