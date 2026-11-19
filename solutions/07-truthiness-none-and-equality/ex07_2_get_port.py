"""Reference solution for exercise 07-2 (Truthiness, None and equality)."""


def get_port(config: dict) -> int:
    """Write get_port(config) that returns config["port"] when it exists and isn't
    None, otherwise 8080. A port of 0 must be returned as 0.
    """
    port = config.get("port")
    return port if port is not None else 8080
