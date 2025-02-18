import phonenumbers
import googlemaps
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
number = "Ton numero"
############################################################################
# Parser le numéro
numero = phonenumbers.parse(number)

# Afficher l'objet PhoneNumber
print(f"Numéro parsé: Country Code: {numero.country_code}, National Number: {numero.national_number}")

# Vérifier si le numéro est valide
is_valid = phonenumbers.is_valid_number(numero)
print(f"Le numéro est-il valide ? {is_valid}")

# Récupérer la localisation
localisation = geocoder.description_for_number(numero, "fr")
print(f"Localisation: {localisation}")

# Récupérer le nom de l'opérateur 
operateur = carrier.name_for_number(numero, "fr")
print(f"Opérateur: {operateur}")

#clé API Google Maps
API_KEY = "AIzaSyBxEgQmCaEVJsHogpRApNo__JpgOZkcC-k"

# Configuration de l'API Google Maps
gmaps = googlemaps.Client(key=API_KEY)
########################################################################
if localisation:
    # On peut ajouter un terme plus précis si la localisation est trop générale
    if localisation.lower() == "sénégal":
        localisation = "Dakar, Sénégal"  # Recherche plus précise sur la ville de Dakar
    résultat = gmaps.geocode(localisation)
    
# Vérifier si le résultat est valide et extraire la précision
if résultat and len(résultat) > 0:
    latitude = résultat[0]['geometry']['location']['lat']
    longitude = résultat[0]['geometry']['location']['lng']
    
    # Si disponible, essayer d'obtenir un place_id pour plus de précision
    place_id = résultat[0].get('place_id')
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Aucune coordonnée trouvée pour cette localisation.")

# Création de la carte avec Folium
myMap = folium.Map(location=[latitude, longitude], zoom_start=9)
folium.Marker([latitude, longitude], popup=localisation).add_to(myMap)
print("MAP creer avec succes ")

# Sauvegarde de la carte en fichier HTML
myMap.save("mylocation.html")
print("MAP sauvegarder avec succes")
