
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from tkinter import *
 
data = b'burakyol,mehmetkilinc,osmankeremerdem,hakanbahsis,yasaremredogru,burakaltun'#Şifrelenecek metin
key = b'euWhM6UAfYvM4oIgxQOPR7CwN2F1n0VZ'#key 
cipher = AES.new(key, AES.MODE_CFB, iv=b'SBUF8JCKvVJ6dv7I')#iv 
ct_bytes = cipher.encrypt(data)

iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv': iv, 'ciphertext': ct})

print(result)
