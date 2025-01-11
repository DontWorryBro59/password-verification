def make_cute_line(main_l: str) -> str:
    """
    This function can to make a formatted line
    :param main_l: str()
    :return: str()
    """
    logo_length = 122
    result = "=" * ((logo_length - len(main_l)) // 2) + main_l + "=" * ((logo_length - len(main_l)) // 2)
    if len(result) < logo_length: result += '='
    return result