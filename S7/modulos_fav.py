import bcrypt
import hashlib

# Contraseña original
password = "contraseña_segura".encode('utf-8')

# 1️⃣ Generamos una "sal" (valor aleatorio)
salt = bcrypt.gensalt()

# 2️⃣ Generamos el hash usando la sal
hashed = bcrypt.hashpw(password, salt)
print(f"Hash bcrypt: {hashed}")

# 3️⃣ Verificamos una contraseña correcta
if bcrypt.checkpw(password, hashed):
    print("✅ Contraseña correcta")
else:
    print("❌ Contraseña incorrecta")

# 4️⃣ Verificamos una incorrecta
otra = "otra_contraseña".encode('utf-8')
if bcrypt.checkpw(otra, hashed):
    print("✅ Coincide")
else:
    print("❌ No coincide")

print("\n--------------------------------\n")


# Texto original
texto = "contraseña_segura"

# Convertimos el texto a bytes antes de encriptar
texto_bytes = texto.encode('utf-8')

# 1️⃣ Crear un hash MD5
hash_md5 = hashlib.md5(texto_bytes).hexdigest()
print(f"MD5: {hash_md5}")

# 2️⃣ Crear un hash SHA256
hash_sha256 = hashlib.sha256(texto_bytes).hexdigest()
print(f"SHA256: {hash_sha256}")

# 3️⃣ Crear un hash SHA512
hash_sha512 = hashlib.sha512(texto_bytes).hexdigest()
print(f"SHA512: {hash_sha512}")