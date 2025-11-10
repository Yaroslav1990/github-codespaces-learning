# Это мой первый скрипт в GitHub Codespaces!
print("Привет, мир из моего облачного Codespace!")

# Дополним его чем-то поинтереснее
import datetime
import os
print(f"Сейчас: {datetime.datetime.now()}")
print(f"Я нахожусь в директории: {os.getcwd()}")
print(f"А мой хост так и вовсе: {os.uname().nodename}")