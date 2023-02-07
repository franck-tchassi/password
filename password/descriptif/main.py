import hashlib
from random import randint, choice
import random
import secrets
import string
import json


def generate_password():
    while True:
        password = ''
        characters = string.ascii_letters + string.digits + '!@#$%^&*'
        password_length = 8
        for i in range(password_length):
           password += random.choice(characters)
       
        if len(password) >= 8:
            
            
            minuscule = any(char.islower() for char in password)
            majuscule = any(char.isupper() for char in password)
            chiffres = any(char.isdigit() for char in password)
            caractère_special = any(char in '!@#$%^&*' for char in password)
            if minuscule and majuscule and chiffres and caractère_special:
              return password
            else:
                print(password, "Le mot de passe ne respecte pas les exigences de sécurité.")
        
        
password = generate_password()
print(password, "validé")

#crypte le mot de passe que l’utilisateur a entré précédemment.
codage = hashlib.sha256(password.encode('ascii')).hexdigest()
print(codage)















#employee ='{"name": "Nitin", "department":"Finance",\
#"company":"GFG"}'

 

#employee_dict = json.loads(employee)
#print("Data after conversion")
#print(employee_dict)
#print(employee_dict['department'])

