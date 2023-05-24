def greetUser(name) :
   return f'Hello {name}'


# print('Start')
# print(greetUser('Julian'))
# print('Finish')

# def plus(number) : 
#    return number + number

# print(plus(3))


def reaction(message) :
  words = message.split(' ') 
  emojis = {
      ':)' : '😃' , 
      ':(' : '😭'
  }
  output = ''
  for word in words: 
    output += emojis.get(word, word) + ' '
  return output

# message = input('> ')
# print(reaction(message))


try: 
  age = int(input('Age: '))
  income = 20000
  risk = income/age
  print(risk)
except ZeroDivisionError: 
  print('Cannot be Zero')
except ValueError: 
  print('Invalid Code')