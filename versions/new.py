# Github.com/m000000000n                                                        
import random                                                                   
import requests                                                                 
a = ['1','2','3','4','5','6','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
                                                                                     
while True:                                                                     
   w = random.choice(a)                                                           
   d = random.choice(a)                                                           
   e = random.choice(a)                                                           
   f = random.choice(a)                                                           
   g = random.choice(a)                                                           
   h = random.choice(a)                                                           
   i = random.choice(a)                                                           
   m = f+e+w+d+g+h+i                                                              
   c = 'https://discordapp.com/api/v6/entitlements/gift-codes/'+m+'?with_application=false&with_subscription_plan=true'
                                                                                  
   b = requests.get(c)                                                            
   if b.status_code == 404:                                                       
                                                                                  
   print('\033[31m' + 'discord.gifts/'+m+' Was invalid'+ '\033[0m')            
   if b.status_code == 429:                                                       
   print("\033[1;33m"+"Rate Limited"+"\033[0m")                                 
                                                                                   
   if b.status_code == 200:                                                       
   print('discord.gifts/'+m+'Is Valid!')                                        
   file = open("okcodes.txt", "w")                                              
   file.write('discord.gifts/'+m)                                               
   file.close() 