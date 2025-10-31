# Encriptador-Desencriptador-XOR-Objetivo

Implementar un programa que cifre y descifre texto usando XOR con una clave repetida (keystream).  
El alumno entiende cómo funciona XOR como operación básica de cifrado.

---

## Descripción
El programa toma un texto ingresado por el usuario, genera una llave binaria del mismo largo y aplica la operación lógica **XOR** para cifrar y descifrar el texto.  
El mismo proceso de XOR se usa para desencriptar, demostrando la propiedad de reversibilidad.

---

##  Ejemplo de ejecución

```bash
$ python xor_cipher.py
Texto: Hola
Texto plano: Hola
Llave: 1011
Texto encriptado: Gnka
Texto desencriptado: Hola