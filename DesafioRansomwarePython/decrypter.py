import os
import pyaes

## abrir arquivo criptografado

file_name = 'teste.txt.ransomwareteste'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia

key = b'teste-ransomware' ## chave deve ter 16 caracteres
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## criar arquivo novo descriptografado

new_file_name = 'teste.txt'
new_file = open(f'{new_file_name}', 'wb')
new_file.write(decrypt_data)
new_file.close()

## remover o arquivo criptografado

os.remove(file_name)
