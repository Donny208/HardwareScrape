# A fiile containing a bunch of methods for helping other classes
import re


def get_state(title: str) -> str:
    normalized_title = title.lower().strip()
    match = re.search("usa-[a-z]{2}", normalized_title)
    if match is None:
        return ""
    return match.group()[-2::]


def valid_title(title: str, verbose: bool = False) -> bool:
    normalized_title = title.lower().strip()
    pattern = r"\[usa-[a-z]{2}\]\s*\[h\].+\[w].+"
    if re.search(pattern, normalized_title) is not None:
        return True
    if verbose:
        print(f"Rejected Title: {title}")
    return False


def get_trade(title: str) -> tuple:
    normalized_title = title.lower().strip()
    pattern = r"\[usa-[a-z]{2}\]\s*\[h\](.+)\[w](.+)"
    match = re.search(pattern, normalized_title)
    return match.groups() if match is not None else None


def process_selling(raw_item: str) -> list:
    normalized_text = raw_item.lower().strip()
    return normalized_text.split(",")