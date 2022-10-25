import random

# используемые символы
chars = 'abcdefghijklmnopqrstuvwxyz'
chars += chars.upper()
nums = str(1234567890)
chars += nums
special_chars = '!@#$%^&*()_+-'
chars += special_chars

length = 8  # длина пароля
password = "".join(random.sample(chars, length))
print(f"Ваш пароль из 8 знаков : {password}")

# -----------------------------------------------------
print("Ваш пароль из 12 знаков : ", ''.join([random.choice(list(
    '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))
