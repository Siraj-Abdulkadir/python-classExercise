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