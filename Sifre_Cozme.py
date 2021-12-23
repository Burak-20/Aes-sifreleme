from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from tkinter import *


    
key = b'euWhM6UAfYvM4oIgxQOPR7CwN2F1n0VZ'#key
    
iv = b'SBUF8JCKvVJ6dv7I'#iv
decryption_suite = AES.new(key, AES.MODE_CFB, iv)
plain_text = decryption_suite.decrypt(base64.b64decode("jhrXajQh8czQieg18owIPdzrGQqZFuMNR62AF9Ct175va/XXV8ev+shWXLRQXxbJUxClQsozVR+HA/phFu7WHg+sVRj+7QMOy2+W"))#Şifrelenmiş metin
print(plain_text)

  