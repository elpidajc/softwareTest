def is_palindrome(s: str) -> bool:
    """
    判断字符串是否为回文（忽略大小写、空格和标点）
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # 只保留字母和数字，并转为小写
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]