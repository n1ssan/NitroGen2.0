import random
import requests
a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','7','8','9','0']


while True:                                                                     
   w = random.choice(a)                                                           
   d = random.choice(a)                                                           
   e = random.choice(a)                                                           
   f = random.choice(a)                                                           
   g = random.choice(a)                                                           
   h = random.choice(a)                                                           
   i = random.choice(a)
   j = random.choice(a) 
   k = random.choice(a)
   m = f+e+w+d+g+h+i+j+k


   url = "https://discordapp.com/api/v6/invite/"+m
   r = requests.get(url)
   if r.status_code == 200:
    print('discord.gg/'+m+"Is valid!")
   elif r.status_code == 404:
    print(f"Invalid {url}")
   elif r.status_code == 429:
    print("Ratelimited.")
    

    

