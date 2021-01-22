# https://www.geeksforgeeks.org/program-to-find-the-next-prime-number/
import math

n = int(input())

def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
      
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True

# Function to return the smallest  
# prime number greater than N  
def nextPrime(N): 
  
    # Base case  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
  
    # Loop continuously until isPrime returns  
    # True for a number greater than n  
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 

for i in range(n):
    d = [1]
    d.append(int(input()))
    for i in range(2):
        x = d[i] + d[i+1]
        d.append( x if isPrime(x) else nextPrime(x) )

    print(d[2]*d[3])


import math
n = 37
print(int(math.sqrt(n) + 1))
for i in range(5,int(math.sqrt(n) + 1), 6):  
    if(n % i == 0 or n % (i + 2) == 0): 
        print(i)
print(n)