import phonenumbers
from phonenumbers import geocoder

number = "+221778391417"

# Parser le numéro
numero = phonenumbers.parse(number)

# Afficher l'objet PhoneNumber
print("Numéro parsé:", numero)

# Vérifier si le numéro est valide
is_valid = phonenumbers.is_valid_number(numero)
print("Le numéro est-il valide ?", is_valid)

# Récupérer la localisation
location = geocoder.description_for_number(numero, "fr")
print("Location:", location)
