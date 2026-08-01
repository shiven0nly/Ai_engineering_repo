# Functions:
# -> Store conversation
# (using list and append)

messages: list[dict] = []


def store_memory(entry: dict) -> list[dict]:
    if not isinstance(entry, dict):
        raise TypeError("entry must be a dictionary")

    messages.append(entry)
    return messages


def get_memory() -> list[dict]:
    return messages


def clear_memory() -> None:
    messages.clear()
