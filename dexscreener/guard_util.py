
def ensure_length_is_under(ls: list, max_count: int, message: str):
    if len(ls) > max_count:
        raise ValueError(message)
