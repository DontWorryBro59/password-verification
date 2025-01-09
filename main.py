from art import tprint


def main_program():
    print_wellcome_message()


def make_cute_line(main_l):
    """
    This function can to make a formatted line
    :param main_l: str()
    :return: (str)
    """
    LOGO_LENGTH = 122
    result = "=" * ((LOGO_LENGTH - len(main_l)) // 2) + main_l + "=" * ((LOGO_LENGTH - len(main_l)) // 2)
    if len(result) < LOGO_LENGTH: result += '='
    return result


def print_wellcome_message():
    """
    This function can write a wellcome text
    :return: None
    """
    tprint("Check - the - password")
    print(make_cute_line("Программа предназначена для проверки вашего пароля или генерации нового пароля"))
    print(make_cute_line("Доступный функционал:"))
    print(make_cute_line("Проверка пароля на сложность"))
    print(make_cute_line("Проверка пароля на необходимые символы и длину"))
    print(make_cute_line("Генерация паролей"))


if __name__ == "__main__":
    main_program()
