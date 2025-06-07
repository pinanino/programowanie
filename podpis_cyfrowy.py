import sys
from lightdsa import LightDSA

file_path = input("Podaj ścieżkę do pliku, który chcesz podpisać:")
dsa = LightDSA(algorithm_name="dsa")

with open (file_path, "r", encoding="utf-8") as f:
    message = f.read()

signature = dsa.sign(message)

print (signature)