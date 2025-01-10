from art import tprint


def main_program():
    tprint("Check - the - password")
    print(make_cute_line(" Программа предназначена для проверки вашего пароля или генерации нового пароля "))
    print(make_cute_line(" Доступный функционал: "))
    print_menu_points()
    open_submenu(get_item_menu()) # We receive a menu selection from the user and run the function


def make_cute_line(main_l):
    """
    This function can to make a formatted line
    :param main_l: str()
    :return: str()
    """
    logo_length = 122
    result = "=" * ((logo_length - len(main_l)) // 2) + main_l + "=" * ((logo_length - len(main_l)) // 2)
    if len(result) < logo_length: result += '='
    return result


def print_menu_points():
    """
    This function can write a wellcome text
    :return: None
    """
    tprint("Check - the - password")
    print(make_cute_line(" 1 - Проверка пароля на сложность "))
    print(make_cute_line(" 2 - Проверка пароля на необходимые символы и длину "))
    print(make_cute_line(" 3 - Генерация паролей "))
    print(make_cute_line(" 0 - Выход "))


def get_item_menu():
    """
    This function can write a menu text and check the command
    :return: int()
    """
    print(make_cute_line(" Пожалуйста введите необходимый пункт меню для продолжения "))
    user_input = input("Вы ввели пункт меню: ")
    user_input = check_user_input_item(user_input)
    # print('Результат выполнения комманды : ', user_input)
    return user_input


def check_user_input_item(user_inp):
    """
    This function is check the user input item menu and return INT or Message
    :param user_inp: str()
    :return: int() or str()
    """
    result = ''
    try:
        if float(user_inp) == int(user_inp) and (int(user_inp) in range(0, 4)):
            return int(user_inp)
        else:
            int('go to except')
    except:
        result = make_cute_line('Вы некорректно ввели пункт меню, введите число от 0 до 3, повторите ввод: ')
        print(result)
        user_inp = input("Вы ввели пункт меню: ")
        return check_user_input_item(user_inp)


def open_submenu(item):
    """
    This function is print submenu for user point
    :param item:
    :return:
    """
    if item == 1:
        print(make_cute_line('Проверка пароля на сложность'))
    elif item == 2:
        print(make_cute_line('Проверка пароля на необходимые символы и длину'))
    elif item == 3:
        print(make_cute_line('Генерация паролей'))
    else:
        print(make_cute_line('Пока!'))


if __name__ == "__main__":
    main_program()
