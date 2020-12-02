import rsa
import rsa.core

# pip install rsa

(public_key, private_key) = rsa.newkeys(256)
print('生成公钥私钥')
print('public key:', public_key)
print('private key:', private_key)
print('接下来加密计算 2 x 20')
print('加密 2')
enc1 = rsa.core.encrypt_int(2, public_key.e, public_key.n)
print(enc1)
print('加密 20')
enc2 = rsa.core.encrypt_int(20, public_key.e, public_key.n)
print(enc2)

print('相乘')
result = enc1 * enc2
print(result)

print('解密结果')
decrypt_result = rsa.core.decrypt_int(result, private_key.d, public_key.n)
print(decrypt_result)