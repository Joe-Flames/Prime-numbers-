# Enter Any Number To Check For PRIME. ForEg-  3

import math
print("✴️✴️✴️✴️ Made by Joe-Flames 🔥 🔥🔥🔥✴️✴️✴️✴️ ")
i = int(input('Please Enter The Number:'))
flag = True
fr = (int)(math.sqrt(i))+1
for num in range(2, fr): 
   if i % num == 0:   
      flag = False 
      
if flag == False or i == 1:
   print(f" {i} is Not Prime") 
   print(''' 
      ▀▄▀▄▀▄ ℕ𝕆𝕋 ℙℝ𝕀𝕄𝔼 ▀▄▀▄▀▄
                  ''')       
else: 
   print(f" {i} is Prime")
   print(''' 
       ▀▄▀▄▀▄ ℙℝ𝕀𝕄𝔼 ▀▄▀▄▀▄        
          ''')
          
print('🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟')
           