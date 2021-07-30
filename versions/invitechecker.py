

url = "https://discordapp.com/api/v6/invite/"+m
  r = requests.get(url)
  if r.status_code == 200:
    print('discord.gg/'+m+"Is valid!")
  elif r.status_code == 404:
    print(f"Invalid {url}")
  elif r.status_code == 429:
    print("Ratelimited.")
    
