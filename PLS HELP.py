def koduj_cezar(znak, klucz):
    kod_znaku = ord(znak)
    ost_litera = ord("Z")
    il_znak = 26  # ord('Z')-ord('A')+1
    if kod_znaku + klucz <= ost_litera:
        return chr(kod_znaku + klucz)
    else:
        return chr(kod_znaku + klucz - 26)


znak = "A"
klucz = 3
print(koduj_cezar(znak, klucz))  # Write your code here :-)
