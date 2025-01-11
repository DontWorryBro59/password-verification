from main import make_cute_line

"""
ord(el) in range(1072, 1104): а-я
ord(el) in range(1040, 1072): А-Я
ord(el) in range(97, 123): a-z
ord(el) in range(65, 91): A-Z
symbols = '@#$%^&*()_+=-{[]};:'",<.>/?~`'
"""


def check_user_input(message: str) -> int:
    """
    This function need for to input user rules
    :param message: str
    :return: bool()  or str() 'quit'
    """
    print(make_cute_line(message))
    user_input = ''
    while user_input not in ['y', 'Y', 'YES', 'yes', 'no', 'n', 'N', 'NO']:
        user_input = input()
        if user_input not in ['y', 'Y', 'YES', 'yes', 'no', 'n', 'N', 'NO']:
            print(make_cute_line('Вы ввели неверный ответ на вопрос'))
            print(make_cute_line(message))
        elif user_input in ['y', 'Y', 'YES', 'yes']:
            return 1
        else:
            return 0


def send_rules() -> list:
    all_rules = []
    print(make_cute_line(' Выберите правила для проверки пароля '))

    while len(all_rules) < 1:
        print(make_cute_line(' Введите какой длины должен быть пароль (число) '))
        lenght_pass = input()
        if lenght_pass.isdigit() and int(lenght_pass) != 0:
            all_rules.append(int(lenght_pass))

    rules = []
    while 1 not in rules:
        rules.append(check_user_input(' Нужны ли русские буквы в нижнем регистре (y - да, n - нет) '))
        rules.append(check_user_input(' Нужны ли русские буквы в верхнем регистре (y - да, n - нет) '))
        rules.append(check_user_input(' Нужны ли английские буквы в нижнем регистре (y - да, n - нет) '))
        rules.append(check_user_input(' Нужны ли английские буквы в верхнем регистре (y - да, n - нет) '))
        rules.append(check_user_input(' Нужны ли цифры (y - да, n - нет '))
        rules.append(check_user_input(' Нужны ли символы (y - да, n - нет '))
        if 1 not in rules[1:]:
            print(make_cute_line(' Вы ответили на все вопросы нет '))
            rules = []
    all_rules += rules
    return all_rules


def check_rules(user_psw: str) -> list:
    """
    This function can create the rules mask
    :param user_psw: str()  User password
    :return: list()  mask of rules
    """
    mask = [0, 0, 0, 0, 0, 0]
    for el in user_psw:
        if ord(el) in range(1072, 1104):
            mask[0] = 1
        elif ord(el) in range(1040, 1072):
            mask[1] = 1
        elif ord(el) in range(97, 123):
            mask[2] = 1
        elif ord(el) in range(65, 91):
            mask[3] = 1
        elif el.isdigit():
            mask[4] = 1
        else:
            mask[5] = 1
    return mask


def check_symbols_in_pass(rul: list):
    """
    This function can check the pass for user rules
    :param rul: list() with rules
    :return: None or False
    """

    p_rul = f'| Длина пароля: {rul[0]} |'
    if rul[1] == 1:
        p_rul += ' а-я |'
    if rul[2] == 1:
        p_rul += ' А-Я |'
    if rul[3] == 1:
        p_rul += ' a-z |'
    if rul[4] == 1:
        p_rul += ' A-Z |'
    if rul[5] == 1:
        p_rul += ' 0-9 |'
    if rul[6] == 1:
        p_rul += ' symbols |'
    print(make_cute_line(' Выбранные правила '))
    print(make_cute_line(f'{p_rul}'))
    user_pass = ''
    while user_pass != '!quit':
        print(make_cute_line(' Введите пароль который вы хотите проверить по выбранным правилам '))
        print(make_cute_line(' Для выхода введите !quit '))
        user_pass = input()
        if user_pass == '!quit': return 0
        pass_check = check_rules(user_pass)
        print(f'{rul[1:]} - выбранные правила, {pass_check} - пароль')
        print(f'{rul[0]} - необходимая длина пароля, {len(user_pass)} - фактическая длина')
        if rul[1:] == pass_check and rul[0] <= len(user_pass):
            print(make_cute_line('Пароль подходит под правила'))
        else:
            print(make_cute_line('Пароль не подходит под правила'))


def start_check_symbols():
    rules = send_rules()
    res = check_symbols_in_pass(rules)
    if res == 0:
        return 0
