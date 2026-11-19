"""Reference solution for exercise 12-3 (Optional values)."""


def display_name(user: dict) -> str:
    """Write display_name(user: dict) -> str that returns the nickname, else the
    name, else "anonymous".

    A key that is missing and a key set to None both count as "not there".
    """
    nickname = user.get("nickname")
    if nickname is not None:
        return nickname
    name = user.get("name")
    return name if name is not None else "anonymous"
