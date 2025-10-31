import random
t = input("Texto: ")
k = ''.join(str(random.randint(0,1)) for _ in t)
c = ''.join(chr(ord(t[i]) ^ int(k[i])) for i in range(len(t)))
d = ''.join(chr(ord(c[i]) ^ int(k[i])) for i in range(len(c)))
print("Texto plano:", t, "\nLlave:", k, "\nTexto encriptado:", c, "\nTexto desencriptado:", d)