import sys
from lightdsa import LightDSA

#Prosimy uzytkownika o podanie sciezki do pliku i wybieramy algorytm
file_path = input("Podaj ścieżkę do pliku, który chcesz podpisać:")
dsa = LightDSA(algorithm_name="dsa")

#Odczytujemy plik i tworzymy podpis cyfrowy
with open (file_path, "r", encoding="utf-8") as f:
    message = f.read()
signature = dsa.sign(message)
#Wywolujemy podpis
print (signature)