import re
import json
import hashlib

def check_password_security(password):
  # Exigences de sécurité
  minimum_length = 8
  minuscule = re.search(r'[A-Z]', password) is not None
  majuscule = re.search(r'[a-z]', password) is not None
  chiffres = re.search(r'\d', password) is not None
  caractère_special = re.search(r'[!@#$%^&*]', password) is not None

  # Vérification des exigences
  if len(password) < minimum_length:
    return False
  if not minuscule:
    return False
  if not majuscule:
    return False
  if not chiffres:
    return False
  if not caractère_special:
    return False

  return True

password = input("Choisissez un mot de passe: ")

while not check_password_security(password):
  print("Le mot de passe ne respecte pas les exigences de sécurité.")
  password = input("Choisissez un nouveau mot de passe: ")

print("Mot de passe valide.")

#crypte le mot de passe que l’utilisateur a entré précédemment.

codage = hashlib.sha256(password.encode('ascii')).hexdigest()

  

# json
file_name = "pass1.txt"
with open(file_name, "w") as file:
  json.dump(codage, file)


 








