#Importujemy pakiet Fernet z biblioteki Pythona
from cryptography.fernet import Fernet
#Generujemy klucz i przypisujemy go do zmiennej
key = Fernet.generate_key()
f = Fernet(key)
#Szyfrujemy i wyświetlamy wiadomość
message = input("Wpisz wiadomosc:")
token=f.encrypt(message.encode())
print("Zaszyfrowana wiadomość:", token)
#Odszyfrowujemy i wyświetlamy wiadomość
d=f.decrypt(token)
print("Odszyfrowana wiadomość:", d.decode())