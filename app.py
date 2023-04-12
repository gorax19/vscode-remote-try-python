import requests
import json

# Spécifier le nom du propriétaire du dépôt et le nom du dépôt
owner = "freqtrade"
repo = "freqtrade"

# Envoyer une requête HTTP GET à l'API GitHub pour récupérer les informations du dépôt
response = requests.get(f"https://api.github.com/repos/{owner}/{repo}")

# Extraire le nombre d'étoiles à partir de la réponse JSON
data = json.loads(response.content)
stars = data["stargazers_count"]

# Afficher le nombre d'étoiles
print(f"Le dépôt {owner}/{repo} a {stars} étoiles.")