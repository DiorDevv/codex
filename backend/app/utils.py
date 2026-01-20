import re


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s-]+", "-", value)
    return value.strip("-")


def list_to_csv(items):
    return ",".join([item.strip() for item in items if item.strip()])


def csv_to_list(value: str):
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]
