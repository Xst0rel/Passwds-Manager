# Version: 1.1
# Author: Xst0rel 
 
import data_file 
import cipher
import time 


# Приветствие и навигация 
def func_console_interface(): 
    print("""
    =====================================================================================
    ||                                                                                 || 
    ||                 =========================================                       || 
    ||                 |           Добро пожаловать!           |                       || 
    ||                 =========================================                       || 
    ||                                                                                 || 
    ||      Тебя приветствует программа Менеджер паролей, можно просто, МП.            ||     
    ||                                                                                 ||     
    ||      =====================================================================      ||  
    ||      |                                                                   |      ||         
    ||      |        ( Навигация: )                                             |      ||
    ||      |                                                                   |      ||
    ||      |                                                                   |      ||
    ||      |  [+] 1 - Создание ключей шифрования;                              |      ||
    ||      |  [+] 2 - Проверка наличие ключей шифрования;                      |      ||  
    ||      |  [+] 3 - Чтение сохранённых данных;                               |      ||
    ||      |  [+] 4 - Запись новых данных;                                     |      ||  
    ||      |  [+] 5 - Выход;                                                   |      ||  
    ||      |                                                                   |      ||               
    ||      |   ===========================================================     |      ||
    ||      |   |           Прежде чем работать с программой,             |     |      ||                        
    ||      |   |          убедитесь в наличии ключей шифрования.         |     |      || 
    ||      |   ===========================================================     |      ||  
    ||      |                                                                   |      ||  
    ||      |                                                                   |      ||  
    ||      =====================================================================      ||         
    ||                                                                                 ||
    =====================================================================================           
          """)


# интерфейс программы 
def func_interface():
    print("[+] Запуск программы . . .")
    time.sleep(3)
    print("---------------------------------------------")
    func_console_interface() 
    print("---------------------------------------------")

    while True: 
        # обрабатываем пользовательский ввод

        command = input("\nВведите команду: ")

        if command == "1": 
            # прежде, чем сгенерировать ключи, проверяем наличие ранее созданных ключей 
            result = cipher.func_check_keys() 

            if result: 
                print("[+] Ключи шифрования существуют!")

            else:
                print("[+] Генерация ключей . . . ")
                cipher.func_generation_priv_pub_key() 
                time.sleep(3)
                print("[+] Ключи были успешно сгенерированы!")

        elif command == "2": 
            result = cipher.func_check_keys() 

            if result: print("[+] Ключи шифрования существуют!")
            else: print("[+] Ключи шифрования отсутствуют!")

        elif command == "3": data_file.func_read_data_file()
        elif command == "4": data_file.func_save_data_file()  
        elif command == "5":
            answer = input("Подтвердите свои действия (1 - выход; 2 - отмена) : ")

            if answer == "1":
                cipher.func_encrypt_file("data")
                print("До скорой встречи!")
                exit() 
        else: 
            print(f"[+] Команды: {command} не существует!")

func_interface() 