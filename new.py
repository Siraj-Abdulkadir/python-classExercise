# fibonnaci sequence

def fibonnaci(i):
    if i ==0:
        return 0
    elif i ==1:
        return 1
    else:
        return fibonnaci(i-1) + fibonnaci(i -2)
    
for y in range(20):
    print(fibonnaci(y))   

 # factorial of a number

def factorial(n):
    if n== 0:
        return 1
    else:
        answer = 1
        for x in range(1,n+1):
            answer = x * answer  
        return answer 
        
print(factorial(5))

# factorial of a number


n = int(input("Enter your number"))
def factorial5(n):
    if n== 0:
        return 1
    else:
        answer = 1
        for i in range(1,n+1):
            answer = i * answer
        return answer
print(factorial5(n))        

even or odd numbers 

userInput = int(input("Enter a number: "))

def evenOdd (userInput):
    if userInput%2 == 0:
        print("Your number is Even")
    else:
        print("Your number is Odd")    
evenOdd(userInput)     

How many digits in a number?

def fibonacci(n):
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
a= int(input("enter the number: "))
print(fibonacci(a))

a=int(input("enter the numbers")) 
b=int(input("enter the numbers")) 
c=int(input("enter the numbers")) 
if a>b and a>c:
    print(a)   
elif b>c:
    print(b)
else:
    print(c)



#check if a number is prime or not 
n=int(input("enter number"))
if n<=1:
    print("its not prime")
else:
    is_prime=True
    for i in range(2,n):
      if n%i==0:
        is_prime=False
        break
if is_prime:
    print("its prime")
else:
    print("its composite")


for i in range(5):
    for j in range(i,5):
        print("*", end="")
        
    print()

pyramid 
  
n = int(input("Rows"))

for i in range(n):

    print((" " * (n-1) ) + ("x" * (n+1)))

n=int(input("enter number"))
divisor=1
while divisor<=n:
    if n%divisor==0:
        print(divisor)
    divisor=divisor+1
    
armstrong nmbers

num = int(input("enter "))
numb_str=len(str(num))
temp=num
sum=0

while temp!=0:
    digit=temp%10
    sum+=digit**numb_str
    temp=temp//10
if num==sum:
    print("it is armstrong")
else:
    print("its not armstrong")

num = int(input("enter "))
divisor = 1

while divisor <= num:
    if num % divisor == 0:
      print(divisor)
    divisor += 1 

def fibonacci(n):
 if n<=1:
   return n
 else:
   return (fibonacci(n-1) + fibonacci(n-2))
userInput = int(input("Enter a number: "))
for y in range(userInput): 
 print(fibonacci(y) )


def fibonnaci(n):
    if n<= 1:
        return n 
    else:
        return (fibonnaci(n -2) + fibonnaci(n-1))
    
userInput = int(input("enter: "))    
for i in range(userInput):
    print(fibonnaci(i))

Count Vowels in a String
vowels = 'aeiou'
string = "hello world"
count = 0
for char in string:
 if char.lower() in vowels:
  count += 1
print(count)





fibonacci sequence

def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-2) + fibonacci(n-1))
userInput = int(input("Enter a number: "))    
for i in range(userInput + 1):
    print(fibonacci(i))

divisors of a number

num = int(input("Enter a number: "))
divisor= 1

while divisor <= num:
    if num%divisor==0:
        print(divisor)
    divisor += 1    


the number of digits in a given number

num = int(input("Enter a number: "))
count = 0

while num != 0:
    num //= 10
    count += 1
print(count)    
     

factorial numbers

n = int(input("Enter a number: "))
def factorial(n):
    if n==0:
        return 1
    else:
        answer = 1 
        for y in range(1,n+1):
            answer = y * answer
            return answer
print(factorial(n))
