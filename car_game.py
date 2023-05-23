command = ""
while True :
  command = input("> ").lower()
  if command == 'start':
    print('Car started... Ready to go!')  
  elif command == 'stop' :
    print('Car Stopped')
  elif command == 'help' :
    print("""
start - to start the car
stop - to stop the car
quit - to quit
    """)
  elif command == 'quit' : 
   break
  else: 
    print('Sorry, please use an appropriate command')
    break



 



# weight = float(input('Weight: '))
# kg = input("(K)g or (L)bs : ")

# if kg.upper() == 'L' : 
#     converted = weight * 2.2
#     print("weight in Lbs:" + str(converted))
# elif kg.upper() == 'K' : 
#      converted = weight / 2.2
#      print("weight in Lbs:" + str(converted))
