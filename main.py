from art import tprint
import check_the_password
import check_symbols
from make_cute_line import make_cute_line


def main_program():
    tprint("Check - the - password")
    print(make_cute_line(" Программа предназначена для проверки вашего пароля или генерации нового пароля "))
    print_menu_points()
    open_submenu(get_item_menu())  # We receive a menu selection from the user and run the function





def print_menu_points():
    """
    This function can write a wellcome text
    :return: None
    """
    print(make_cute_line(" Главное меню "))
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
    user_input = input()
    user_input = check_user_input_item(user_input)
    # print('Результат выполнения комманды : ', user_input)
    return user_input


def check_user_input_item(user_inp: str) -> int:
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


def open_submenu(item: int) -> None:
    """
    This function is print submenu for user point
    :param item:
    :return:
    """
    if item == 1:
        print(make_cute_line('Запущена проверка пароля на сложность'))
        if check_the_password.start_check_the_pass() == 0:
            print_menu_points()
            open_submenu(get_item_menu())
    elif item == 2:
        print(make_cute_line('Запущена проверка пароля на необходимые символы и длину'))
        if check_symbols.start_check_symbols() == 0:
            print_menu_points()
            open_submenu(get_item_menu())
    elif item == 3:
        print(make_cute_line('Генерация паролей'))
    else:
        print(make_cute_line('Пока!'))


if __name__ == "__main__":
    main_program()
