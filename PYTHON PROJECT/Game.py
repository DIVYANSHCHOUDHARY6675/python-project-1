import random 
number=random.randint(1,9)
i=1
while(i<3):
  choice=int(input("guess a number between 1 to 9 --"))
  if (choice==number):
      print("congratulation you guessed it correctly!!!")
      break
  else:
    print("try again")
    
  i=i+1
  
