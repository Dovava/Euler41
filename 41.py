import math
highestPrime = -1dtygdfctyfcddgyhh
nums = '123456789'

def isPrime(n):
   for i in range(2,int(math.sqrt(n))+1):
      if n%i == 0:
         return False
   return True

def getInt(a):
   num = ""   
   for n in a:
      num += n
   return int(num)

def findPermutations(string, i = 0):
    global highestPrime
    if i == len(string):
        if isPrime(getInt(string)) and getInt(string) >= highestPrime:
           highestPrime = getInt(string)

    for j in range(i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        findPermutations(words, i + 1)
for i in range(1,len(nums)+1):
   findPermutations(nums[:i])
print(highestPrime)
