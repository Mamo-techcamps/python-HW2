

# take input from the user
number = int(input('Enter a number : '))

# prime numbers are greater than 1
if number > 1 : 
  for i in range(2,number):
    if number % i == 0 : 
      print(number , " is not prime number") 
      break
  else: 
    print(number, ' is a prime number')

# if number is less than or equal to one, it is not prime
else :
  print(number , " is not prime number")
  

