# Github.com/m000000000n
import random
import requests
import time
a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k',]
print("Wait ten seconds for codes to start coming  \n | \n V")
while True:
 w = random.choice(a)
 d = random.choice(a)
 e = random.choice(a)
 f = random.choice(a)
 m = f+e+w+d
 c = 'https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'?with_application=false&with_subscription_plan=true'
 time.sleep(10)
 b = requests.get(c)
 if "Unknown Gift Code" in b.text:

    print('\033[31m' + 'discord.gifts/'+m+' Was invalid'+ '\033[0m')
 elif b.status_code == 429:
   print("\033[1;33m"+"Rate Limited"+"\033[0m")

 else:
   print('discord.gifts/'+m+'Is Valid!')
   file = open("codes.txt", "w")
   file.write('discord.gifts/'+m)
   file.close()
   
