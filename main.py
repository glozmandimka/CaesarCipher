ALPHABET_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALPHABET_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET = {i: (ALPHABET_UPPER[i], ALPHABET_LOWER[i]) for i in range(len(ALPHABET_UPPER))}


def decrypt(s: str, step: int) -> str:
    for i in range(len(s)):
        if s[i].isalpha():
            is_alpha_lower = s[i].islower()
            new_index = ALPHABET_UPPER.index(s[i].upper()) + step
            if new_index > 32:
                new_index = new_index - 33
            s = s[:i] + ALPHABET[new_index][is_alpha_lower] + s[i + 1:]
    return s


def encrypt_with_key(s: str, step: int) -> str:
    for i in range(len(s)):
        if s[i].isalpha():
            is_alpha_lower = s[i].islower()
            new_index = ALPHABET_UPPER.index(s[i].upper()) - step
            if new_index < 0:
                new_index = new_index + 33
            s = s[:i] + ALPHABET[new_index][is_alpha_lower] + s[i + 1:]
        else:
            continue
    return s


def encrypt_without_key(s: str) -> list[str]:
    list_of_answer = list()
    for step in range(1, 33):
        s_tmp = s
        for i in range(len(s)):
            if s_tmp[i].isalpha():
                is_alpha_lower = s_tmp[i].islower()
                new_index = ALPHABET_UPPER.index(s_tmp[i].upper()) - step
                if new_index < 0:
                    new_index = new_index + 33
                s_tmp = s_tmp[:i] + ALPHABET[new_index][is_alpha_lower] + s_tmp[i + 1:]
            else:
                continue
        list_of_answer.append(s_tmp)
    return list_of_answer


def menu():
    print("[1]: Зашифровать\n[2]: Расшифровать\n[3]: Выход")


menu()
flag = True
while flag:
    selector = int(input("> "))
    if selector == 1:
        message = input("Введите строку для шифрования: ")
        key = int(input("Введите ключ шифрования: "))
        answer = decrypt(message, key)
        print("+" + "-" * 27 + "-" * (len(answer) + 2) + "+")
        print(f"|  Зашифрованное сообщение: {decrypt(message, key)}  |")
        print("+" + "-" * 27 + "-" * (len(answer) + 2) + "+")
        menu()
    elif selector == 2:
        is_with_key = int(
            input("Знаете ли вы ключ, с помощью которого сообщение было зашифровано?\n[1]: Да\n[2]: Нет\n> "))
        if is_with_key == 1:
            message = input("Введите строку, которую надо расшифровать: ")
            key = int(input("Введите ключ шифрования: "))
            answer = encrypt_with_key(message, key)
            print("+" + "-" * 28 + "-" * (len(answer) + 2) + "+")
            print(f"|  Расшифрованное сообщение: {answer}  |")
            print("+" + "-" * 28 + "-" * (len(answer) + 2) + "+")
            menu()
        elif is_with_key == 2:
            message = input("Введите строку, которую надо расшифровать: ")
            answer = encrypt_without_key(message)
            for i in range(len(answer)):
                print(f"ROT{i + 1}: {answer[i]}")
            menu()
    elif selector == 3:
        print("Спасибо за использование!!!")
        flag = False
    else:
        print("Выберите одно из предложенных действий!")
