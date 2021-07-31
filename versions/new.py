# Github.com/m000000000n                                                        
import random                                                                   
import requests
import os
from colorama import Fore, Back, Style
from config import *
a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','7','8','9','0']
logo = """
______  ___                   
___   |/  /__________________ 
__  /|_/ /_  __ \  __ \_  __ \
_  /  / / / /_/ / /_/ /  / / /
/_/  /_/  \____/\____//_/ /_/ 
"""
if lettersOnly == True:
 a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if numbersOnly == True:
  a=['1','2','3','4','5','6','7','8','9','0']
if lnmix == True:
  a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','7','8','9','0']
print(Fore.GREEN + logo)  
choice = input(Fore.BLUE+"What would you like to use \n 1. Nitro code gen & checker \n 2. Nitro code gen only \n 3. invite gen \n 4. invite gen & checker")
if choice == "1":                                                                                   
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
   l = random.choice(a) 
   n = random.choice(a) 
   o = random.choice(a) 
   p = random.choice(a) 
   q = random.choice(a) 
   r = random.choice(a) 
   s = random.choice(a) 
   m = f+e+w+d+g+h+i+j+k+l+n+o+p+q+r+s                                                            
   c = 'https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'?with_application=false&with_subscription_plan=true'
                                                                                  
   b = requests.get(c)                                                            
   if b.status_code == 404:                                                       
                                                                                  
    print('\033[31m' + 'discord.gifts/'+m+' Was invalid'+ '\033[0m')            
   if b.status_code == 429:                                                       
    print("\033[1;33m"+"Rate Limited"+"\033[0m")                                 
                                                                                   
   if b.status_code == 200:                                                       
    print('discord.gifts/'+m+'Is Valid!')
    if sniperOn == True:
      requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'/redeem', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
      print('Nitro redeemed!')
      else:
       file = open("okcodes.txt", "w")                                              
       file.write('discord.gifts/'+m)                                               
       file.close()
       
if choice == "2":
 os.system('python3 gen1.py')
if choice == "3":
 os.system('python3 invitegen.py')
if choice == "4":
 os.system('python3 invitechecker.py')
