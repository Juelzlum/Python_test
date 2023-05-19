
# x = 10
# x += 3 
# print(x)

# x = 3 == 3

# print(x)

# temp = 20
# if temp > 30 :
#     print('It is hot')
# elif temp < 30 :
#     print("Done")
# else : 
#     print('It is cold')


weight = float(input('Weight: '))
kg = input("(K)g or (L)bs : ")

if kg.upper() == 'L' : 
    converted = weight * 2.2
    print("weight in Lbs:" + str(converted))
elif kg.upper() == 'K' : 
     converted = weight / 2.2
     print("weight in Lbs:" + str(converted))


  