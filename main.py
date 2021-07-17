import random
import requests
a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k',]

while True:
 w = random.choice(a)
 d = random.choice(a)
 e = random.choice(a)
 f = random.choice(a)
 m = f+e+w+d
 c = 'https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'?with_application=false&with_subscription_plan=true'

 b = requests.get(c)
 if "Unknown Gift Code" in b.text:

    print('\033[31m' + 'discord.gifts/'+m+' Was invalid'+ '\033[0m')
 if b.status_code == 429:
   print("\033[1;33m"+"Rate Limited"+"\033[0m")

 if "Unknown Gift Code" and "You are being rate limited" not in b.text:
   print('discord.gifts/'+m+'Is Valid!')
   file = open("codes.txt", "w")
   file.write('discord.gifts/'+m)
   file.close()
   
