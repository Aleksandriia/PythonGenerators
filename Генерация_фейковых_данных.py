# Для корректной работы требуется установить
# pip install Faker

# документация: https://faker.readthedocs.io/en/latest/

from faker import Faker

# 'en_US'; если убрать значение, результат на английском будет
fake = Faker('ru_RU')

print(fake.name(),
      fake.phone_number(),
      fake.date_of_birth(minimum_age=23),
      fake.address(),
      fake.city(),
      fake.job(),
      # fake.company(),
      # fake.color(),
      sep="\n")

#adres_file = str(input("*Укажите путь файла: "))
