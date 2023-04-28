class FactorialError(Exception):
    pass

def fac(a):
    if(a<0):
        raise FactorialError("Factorial of negative numbers are undefined.")
    elif(a==0):
        return 1
    else:
         return a*fac(a-1)

try:
    fac(-1)
except FactorialError:
    print("Calculaiting factorial of negative number is not possible")
finally:
    print("Calculation of factorial completed.")