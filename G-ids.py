import random
s=input("\033[1;33mEnter first code id example: \033[1;34m10001\033[1;33m-\033[1;34m10002\033[1;33m-\033[1;34m10003 :")
i=int(input("\033[1;32mEnter first number would be 10 digit example:\033[1;31m4326511111 \033[1;37m: "))
x=int(input("\033[1;35mEnter the limit number same digit 10 but would be more much example \033[1;33m4326544444\033[1;31m: "))
while i < x:
   i+=1
   print (s+str(i))

