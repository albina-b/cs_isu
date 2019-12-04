#start python 

#prime number checker

def isPrime(num): 
  for i in range(2, num): 
    if not(num%i): 
      return False 
   else: 
     return True
  
  array = [i for i in range(200)]
  for n in array: 
    if isPrime(n): 
      print(n)
      
