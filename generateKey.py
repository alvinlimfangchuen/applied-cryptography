"""
generateKey.py Consist Of 7 Main Function:
1 - generateKey
2 - keygen
3 - gcd
4 - findModInverse
5 - rabinMiller
6 - isPrime
7 - generateLargePrime

"""
import random, sys, os

def generateKey(keySize):
   #Generate Large two prime numbers
   p = generateLargePrime(keySize)
   q = generateLargePrime(keySize)
   #Calculate n Value
   n = p * q
	# Generate a number  that is relatively prime to (p-1)*(q-1).
   while True:
      e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
      if gcd(e, (p - 1) * (q - 1)) == 1:
         break
   # Calculate value of and the mod inverse of e.
   d = findModInverse(e, (p - 1) * (q - 1))
   publicKey = (n, e)
   privateKey = (n, d)
   #Return Keys
   return (publicKey, privateKey)

#Keygen Function
#-- This Function will run once the button "Generate Keys" is clicked on the GUI Application And Retrieve Key Size.--#
def keygen(keySize):
   #Call generateKey function to get keys
   publicKey, privateKey = generateKey(keySize)

   #Format Keys To Hex Value for Public Keys
   publicKey0 = format(publicKey[0],"X") 
   publicKey0 = publicKey0.zfill(12) 
   publicKey1 = format(publicKey[1],"X")
   publicKey1 = publicKey1.zfill(12)   

   #Format Keys To Hex Value for Private Keys 
   privateKey0 = format(privateKey[0],"X")
   privateKey0 = privateKey0.zfill(12)
   privateKey1 = format(privateKey[1],"X")
   privateKey1 = privateKey1.zfill(12)

   #write all the keys into text file
   f = open("1_keygen.txt","w")
   f.write("n:")
   f.write(privateKey0)
   f.write("\ne:")
   f.write(publicKey1)
   f.write("\nd:")
   f.write(privateKey1)
   f.close()
   
   #Set All The Keys as global variable to return key separately
   global key_n, key_e, key_d
   key_n = privateKey0
   key_e = publicKey1
   key_d = privateKey1
   keyArray = [privateKey0,publicKey1,privateKey1]
   #Return All Keys To Main File
   return keyArray

#Return Keys Separately To Main File
def key_n():
   return key_n 
def key_e():
   return key_e
def key_d():
   return key_d

#Function To find GDC
def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

#Function To Find Mod Inverse
def findModInverse(a, m):
   if gcd(a, m) != 1:
      return None
   u1, u2, u3 = 1, 0, a
   v1, v2, v3 = 0, 1, m
   
   while v3 != 0:
      q = u3 // v3
      v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
   return u1 % m   



#Rabin Millier Algorithm Function To Generate Larga Prime Number
#Function isPrime() and generateLargePrime() Is Used For This Function
def rabinMiller(num):
   s = num - 1
   t = 0 
   while s % 2 == 0:
      s = s // 2
      t += 1
 
   for trials in range(5):
      a = random.randrange(2, num - 1)
      v = pow(a, s, num)
      if v != 1:
         i = 0
         while v != (num - 1):
            if i == t - 1:
               return False
            else:
               i = i + 1
               v = (v ** 2) % num
      return True

#Pre-Define Low Prime Number In Order To Reduce Computing Power To Find Large Prime Number
def isPrime(num):
   if (num < 2):
      return False

   lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
   67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
   251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349, 
   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 
   457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 
   571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 
   673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
   797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
   911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
	
   if num in lowPrimes:
      return True
   for prime in lowPrimes:
      if (num % prime == 0):
         return False
   return rabinMiller(num)

 #Function That Will Stop Loop Once It Generated Large Prime Number
def generateLargePrime(keysize):
  
   while True:
      num = random.randrange(2**(keysize-1), 2**(keysize))
      if isPrime(num):
         return num