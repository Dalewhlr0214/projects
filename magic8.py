name = "Dale"
Question = 'Will I win the lottery'
answer = ''
import random
random_number = random.randint(1, 9)
if random_number == 1:
  print('Yes definitely')
elif random_number == 2:
  print('it is decidely so')
elif random_number == 3:
  print('without a doubt')
elif random_number == 4:
  print('Reply hazy, try again') 
elif random_number == 5:
  print('Ask again later')
elif random_number == 6:
  print('Better not tell you now.')
elif random_number == 7:
  print('My sources say no')
elif random_number == 8:
  print('outlook not so good')
elif random_number == 9:
  print('outlook not so good')
else:
  print('error')
print(name + ' asks: '+ Question)
print('magin 8-ball answer: ' + answer)