from make_cute_line import make_cute_line
from random import choice


def check_zero(inp: str) -> bool:
    if inp == '0':
        return True
    else:
        return False


def gen_rules() -> bool | list:
    rules = []
    print(make_cute_line(' Запущен процесс генерации пароля '))
    print(make_cute_line(' Необходимо выбрать правила для генерации '))
    print(make_cute_line(' Введите через пробел строку соответствующую необходимым параметрам '))
    print(make_cute_line(' 1 - Включить символы а-я в нижнем регистре '))
    print(make_cute_line(' 2 - Включить символы А-Я в верхнем регистре '))
    print(make_cute_line(' 3 - Включить символы a-z в нижнем регистре '))
    print(make_cute_line(' 4 - Включить символы A-Z в в верхнем регистре '))
    print(make_cute_line(' 5 - Включить цифры  '))
    print(make_cute_line(' 6 - Включить символы '))
    print(make_cute_line(' Пример ввода строки: 1 5 6 '))
    print(make_cute_line(' Пароль будет включать в себя: | а-я | 0-9 | symbols |'))
    print(make_cute_line(' Введите строку согласно инструкции '))
    print(make_cute_line(' Для выхода введите 0 на любом этапе'))
    good_input = False

    while not good_input:
        input_rules = input()
        if check_zero(input_rules):
            return False
        try:
            input_rules = list(set(map(int, input_rules.strip().split())))

            if max(input_rules) > 6 or min(input_rules) < 1:
                print(int('некорректный ввод, переход в блок except'))

            good_input = True

        except:
            print(input_rules)
            print('[LOG]: пользователь ввел некорректный пароль')
            print(make_cute_line(' Ошибка ввода строки '))
            print(make_cute_line(' Пример ввода строки: 1 5 6 '))
            print(make_cute_line(' Пароль будет включать в себя: | а-я | 0-9 | symbols |'))
            print(make_cute_line(' Введите строку согласно инструкции '))

    rules += input_rules
    print(make_cute_line(' Введите необходимую длину пароля (не больше 100 символов)'))

    good_input = False
    while not good_input:
        input_len = input()
        if check_zero(input_len):
            return False
        try:
            input_len = int(input_len)
            if input_len < 1 or input_len > 100:
                print(int('некорректный ввод, переход в блок except'))

            good_input = True
        except:
            print('[LOG]: пользователь ввел некорректную длину строки')
            print(make_cute_line(' Ошибка ввода длины пароля '))
            print(make_cute_line(' Введите необходимую длину пароля '))

    rules.append(input_len)

    print(make_cute_line(' Введите необходимое количество паролей для генерации '))
    good_input = False
    while not good_input:
        input_col = input()
        if check_zero(input_col):
            return False
        try:
            input_col = int(input_col)
            if input_col < 1 or input_col > 9999:
                print(int('некорректный ввод, переход в блок except'))

            good_input = True
        except:
            print('[LOG]: пользователь ввел некорректную длину строки')
            print(make_cute_line(' Ошибка ввода количества паролей '))
            print(make_cute_line(' Введите необходимое количество паролей для генерации '))
    rules.append(input_col)
    return (rules)


def gen_alphabit(rul: str) -> (list, int, int):
    """
    This function can generate options for generator
    :param rul: str
    :return: (list, int, int)
    """
    alphabit = []
    if 1 in rul[:-2]:
        for el in range(ord('а'), ord('я')):
            alphabit.append(chr(el))
    if 2 in rul[:-2]:
        for el in range(ord('А'), ord('Я')):
            alphabit.append(chr(el))
    if 3 in rul[:-2]:
        for el in range(ord('a'), ord('z')):
            alphabit.append(chr(el))
    if 4 in rul[:-2]:
        for el in range(ord('A'), ord('Z')):
            alphabit.append(chr(el))
    if 5 in rul[:-2]:
        for el in range(0, 10):
            alphabit.append(el)
    if 6 in rul[:-2]:
        for el in '!@#$%^&*(){[]}|";"~`,./?':
            alphabit.append(el)
    return alphabit, rul[-2], rul[-1]


def start_generate(alph: list, ln: int, hm: int) -> None:
    """
    This function can start to generate your passwords
    :param alph:
    :param ln:
    :param hm:
    :return:
    """
    print(make_cute_line(' Начало генерации паролей '))
    passwords = []

    for _ in range(hm):
        password = ''
        for _ in range(ln):
            password += str(choice(alph))
        passwords.append(password)

    print(make_cute_line('Хотите сохранить сгенерированные пароли в файл? Введите y/n'))
    user_input = True
    while user_input != False:
        user_input = input()
        if user_input in ['y', 'n']:
            if user_input == 'y':
                user_input = False
                save_to_file(passwords)
                user_input = False
            else:
                user_input = False
        else:
            print(make_cute_line('Вы некорректно ввели ответ, введите y или n'))

    print(make_cute_line('Хотите вывести сгенерированные пароли в консоль? Введите y/n'))
    user_input = True
    while user_input != False:
        user_input = input()
        if user_input in ['y', 'n']:
            if user_input == 'y':
                for count, el in enumerate(passwords, start=1):
                    print(f"{count} - {el}")
                user_input = False
            else:
                user_input = False
        else:
            print(make_cute_line('Вы некорректно ввели ответ, введите y или n'))


def save_to_file(psw: list) -> None:
    """
    This function can save your passwrods list on file
    :param psw: list()
    :return: None
    """
    with open('passwords', 'w', encoding='UTF-8') as file:
        for el in psw:
            file.write(el + '\n')


def main_gen_pass() -> bool:
    """
    This is main program in generet_password for integrate to main project program
    :return: bool
    """
    stop_generate = False
    while not stop_generate:
        rules = gen_rules()
        if rules == False:
            return False
        alphabit, len_lst, how_much = gen_alphabit(rules)
        start_generate(alphabit, len_lst, how_much)
        stop_generate = True
    else:
        return False
