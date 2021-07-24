# Define Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<0:
        print("Input is < 0 ")
    # when Fibonacci number is 0
    elif n==0:
        return 0
    # when Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# For input 2 and 9 
 
print("Input here : 2" )
print( Fibonacci(2))

print("Input here : 9" )
print( Fibonacci(9))
 
