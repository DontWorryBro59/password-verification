from math import log2
from make_cute_line import make_cute_line

"""
Оценка стойкости парольных систем определяется по  формуле энтропии E = log2(M**N)
    M - Мощность алфавита пароля
    N - Длина пароля
Зависимость уровня стойкости пароля от значения энтропии
    < 28 бит Очень слабый - не рекомендуется использовать как пароль;
    28-35 Слабый - данный тип паролей способен предотвратить атаку не на долго;
    35-59 Средний - пароли с уровнем «Средний» используются в корпоративных сетях;
    60-127 Высокий - пароль со статусом «Высокая сложность» используются для защиты конфиденциальной или финансовой информации;
    128 Сверхнадежный - пароль обладает очень большой стойкостью к подбору.
"""


def calculate_complexity(user_pas):
    """
    This function can check evaluate the password complexity
    :param user_pas: - str() The password from the user
    :return: str() - result
    """
    m = calculate_password_power(user_pas)
    if m == 'Error: is a space in the password':
        return m
    n = len(user_pas)
    # print(f'[LOG] m - {m}')
    # print(f'[LOG] n - {n}')
    dif_levels = ["очень слабый - мгновенный взлом",
                  "слабый - данный тип паролей способен предотвратить атаку не на долго",
                  "средний - пароли с уровнем «Средний» можно использовать в корпоративных сетях;",
                  "высокий - пароль можно использовать для защиты конфиденциальной или финансовой информации;",
                  "сверхнадежный - пароль обладает очень большой стойкостью к подбору."]
    entrop = round(log2(m ** n))
    if entrop < 28:
        return f"{entrop} бит: {dif_levels[0]}"
    elif 28 <= entrop < 35:
        return f"{entrop} бит: {dif_levels[1]}"
    elif 35 <= entrop < 60:
        return f"{entrop} бит: {dif_levels[2]}"
    elif 60 <= entrop < 128:
        return f"{entrop} бит: {dif_levels[3]}"
    else:
        return f"{entrop} бит: {dif_levels[4]}"


def calculate_password_power(user_pas):
    """
    This function calculates the password strength
    :param user_pas: str() - user password
    :return: int() - alphabet power
    """
    rus_alph_low = 0  # 33
    rus_alph_up = 0  # 33
    eng_alph_low = 0  # 26
    eng_alph_up = 0  # 26
    numb_alph = 0  # 10
    symbols_alph = 0  # 32

    if ' ' in set(user_pas):
        return 'Error: is a space in the password'
    else:
        for el in user_pas:
            if ord(el) in range(1072, 1104):
                rus_alph_low = 1
            elif ord(el) in range(1040, 1072):
                rus_alph_up = 1
            elif ord(el) in range(97, 123):
                eng_alph_low = 1
            elif ord(el) in range(65, 91):
                eng_alph_up = 1
            elif el.isdigit():
                numb_alph = 1
            else:
                symbols_alph = 1
        # print(f'[LOG] {rus_alph_low,rus_alph_up,eng_alph_low,eng_alph_up,numb_alph,symbols_alph}')
        result = rus_alph_low * 33 + rus_alph_up * 33 + eng_alph_low * 26 + eng_alph_up * 26 + numb_alph * 10 + symbols_alph * 32
        return result


def start_check_the_pass():
    """
    This function to start the check_the_password function
    :return: None
    """
    result = None
    while result != 0:
        print(make_cute_line("Введите ваш пароль или 0 для выхода в главное меню:"))
        user_pass_inp = input()
        result = calculate_complexity(user_pass_inp)
        if user_pass_inp.isdigit() and int(user_pass_inp) == 0:
            return 0
        elif result == 'Error: is a space in the password':
            print(make_cute_line('Вы ввели неверный пароль, присутствуют пробелы'))
        else:
            print(make_cute_line(result))
