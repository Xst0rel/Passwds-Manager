import cipher 
import time 
import os 

def func_read_data_file():
    if os.path.isfile("data.bin"):
        # дешифруем файл для возможности чтения данных
        cipher.func_decrypt_file("data.bin")

    try:
        with open("data", "r") as file_read: 
            file_r = file_read.readlines() 
            # выводим сохранённые данные 
            for string in file_r: print(string, end="")

    except FileNotFoundError: print("[+] Файл не найден!")

# Сохранение новых данных 
def func_save_data_file():
    
    if os.path.isfile("data.bin"):
        # если запись осуществляется тогда, когда файл уже был зашифрован, дешифруем его 
        cipher.func_decrypt_file("data.bin")
    else: 
        # проверяем наличие необходимого файла, если файл не был найден, создаём его 
        if os.path.isfile("data") == False: 
            file = open("data", "w+")
            file.close() 

    # запрашиваем ресурс 
    resource = input("Введите ресурс: ")
    login = input("Введите логин: ")
    answer = input("Дальше Вы можете: (1 - указать уже существующий пароль; 2 - сгенерировать новый пароль): ")

    if answer == "1": passwd = input("Введите пароль: ")
    else: passwd = cipher.func_generation_passwd()

    print(f"{resource}|{login}|{passwd}|. Сохраняем? (Y/n): ") 
    # просим пользователя подтвердить свои действия 
    agree = input() 

    if agree in ("Y", "y"): 
        with open("data", "a") as file_wrote: 
            file_wrote.write(f"{resource}|{login}|{passwd}|\n") 
            print("[+] Сохранение данных . . .")
            time.sleep(3) 
            print("Данные были успешно сохранены!")

