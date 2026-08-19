#byte = 42

#print("Decimal:" , byte)
#print("Binário:" , "{:08b}" .format(byte,))

texto = "CASA"

for letra in texto:
    codigo = ord(letra)

    print(
        letra,
        "->",
        codigo,
        "->",
        "{:08b}" .format(codigo ,)
    )