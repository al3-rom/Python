# Introducir 5 caracteres y devolver otro string con todos los caracteres
# duplicados. Si el input es ‘sbc56’, el output deberá ser ‘ssbbcc5566

string = input("Pon 5 caracteres: ")

print(string[0] * 2 + string[1] * 2 + string[2] * 2 + string[3] * 2 + string[4] * 2 )