from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from random import choice 
import random  
import os 

# Генерация открытого и закрытого ключей 
def func_generation_priv_pub_key(): 
    key = RSA.generate(2048) # размер ключа указывается в битах
    # создаём файл и записываем в него содержимое закрытого ключа 
    with open('Data\\pc\\close.pem', 'wb') as priv:  
        priv.write(key.export_key())

    # создаём файл и записываем в него содержимое открытого ключа
    with open('Data\\pc\\open.pem', 'wb') as pub: 
        pub.write(key.publickey().export_key())

# Шифрование файла с помощью открытого ключа 
def func_encrypt_file(path): # на входе получаем путь к шифруемому файлу
    # открываем и читаем файл для шифрования используя указанный путь 
    with open(path, 'rb') as encrypt_file: 
        data_encrypt = encrypt_file.read() 


    # проверяем наличие открытого ключа 
    if os.path.isfile('Data\\pc\\open.pem'): 
        public_RSA = RSA.import_key(open('Data\\pc\\open.pem').read())
        session_key = get_random_bytes(16)

    # шифруем сессионный ключ открытым ключом RSA
    chipher_RSA = PKCS1_OAEP.new(public_RSA)
    encrypt_session_key = chipher_RSA.encrypt(session_key)

    # шифруем файл с сессионным ключом алгоритма AES
    chipher_AES = AES.new(session_key, AES.MODE_EAX)
    chipher_text, tag = chipher_AES.encrypt_and_digest(data_encrypt)

    with open(f'{path}.bin', 'wb') as file_out:
        for i in (encrypt_session_key, chipher_AES.nonce, tag, chipher_text):
            file_out.write(i)
    # файл зашифрован 
    
    os.remove(path) # удаление начального файла         

# Дешифрование файла с помощью закрытого ключа 
def func_decrypt_file(path): # на входе получаем путь к дешифруемому файлу
    # проверяем наличие закрытого ключа  
    if os.path.isfile("Data\\pc\\close.pem"):
        priv_key_RSA = RSA.import_key(open("Data\\pc\\close.pem").read())
        # Открывается на чтение зашифрованный файл, из которого считывается зашифрованный сессионный ключ.
        with open(path, "rb") as file_in: 
            encrypt_session_key, nonce, tag, chipher_text = [file_in.read(i) for i in (priv_key_RSA.size_in_bytes(), 16, 16, -1)]

        # расшифровка сессионного ключа закрытым ключом алгоритма RSA
        chipher_RSA = PKCS1_OAEP.new(priv_key_RSA)
        session_key = chipher_RSA.decrypt(encrypt_session_key)

        # расшифровка данных сессионным ключом алгоритма AES
        chipher_AES = AES.new(session_key, AES.MODE_EAX, nonce)
        data = chipher_AES.decrypt_and_verify(chipher_text, tag)

        with open(path[:4], "wb") as file_out: 
            file_out.write(data)
        # файл дешифрован 
        os.remove(path) # удаление начального файла

def func_check_keys():
    # проверяем наличие ключей шифрования
    keys = ["Data\\pc\\open.pem", "Data\\pc\\close.pem"] # список ключей шифрования
    results = [os.path.isfile(key) for key in keys] # записываем результат проверки 
            
    if all(results): return True
    else: return False 

# Генерируем пароль (по умолчанию длина пароля = 13)
def func_generation_passwd(length = 13):
    letters_upper_lst = "QWERTYUIOPASDFGHJKLZXCVBNM" # список символов в верхнем регистре 
    letters_lower_lst = "qwertyuiopasdfghjklzxcvbnm" # список символов в нижнем регистре 
    numbers_lst = "1234567890" # список числовых значений
    symbols_lst = "!@#$%^&*()?" # список специальных символов 
    alphabet = [letters_upper_lst, letters_lower_lst, numbers_lst, symbols_lst] # список, содержащий все списки 
    passwd = "" # переменная в которой будет храниться сгенерируемый пароль 
    """ 
    Генерация пароля 
    Алгоритм генерации пароля: 
    
    1. Добавление символа в верхнем регистре 
    2. Добавление символа в нижнем регистре 
    3. Добавление числового значения 
    4. Добавление специального символа 
    5. Случайным образом по одному добавляются элементы из всех списков находящиеся в списке alphabet 
    """
    # 1, 2, 3, 4
    passwd += choice(letters_upper_lst) 
    passwd += choice(letters_lower_lst)
    passwd += choice(numbers_lst)
    passwd += choice(symbols_lst)
    # 5
    while len(passwd) != length: passwd += choice(alphabet[random.randint(0, 3)])

    return passwd 
