# 1. Define a recursive function that takes two integers as input and returns their product using repeated addition, without employing the multiplication operator.
def multiply_recursive(a: int,b:int):
    if b==0:
        return 0
    if b<0:
        return -multiply_recursive(a,-b)
    return a + multiply_recursive(a,b-1)
# Example
print(multiply_recursive(5,3))


#2.Define a recursive function that computes the result of raising a given base to a specified exponent, without using the exponentiation operator(**)
def power_recursive(base:int,exponent:int)->int:
    if exponent==0:
        return 1
    if exponent<0:
        return 1/power_recursive(base,-exponent)
    return base * power_recursive(base,exponent-1)
# Example
print(power_recursive(2,3))


# 3.Implement a recursive function that prints all integers from a given number n down to 0.
def countdown(n:int)->None:
    if n<0:
        return
    print(n)
    countdown(n-1)
# Example
countdown(5)


# 4.Implement a recursive function that prints all integers from 0 up to a given number n by modifying the previous countdown function.
def count_up(n:int,current:int=0)->None:
    if current > n:
        return
    print(current)
    count_up(n,current+1)
#Example
count_up(5)


# 5.Write a recursive function that takes a string as input and returns a reversed copy of the string,using only string concatenation.
def reverse_string_recursive(s:str)-> str:
    if len(s)<= 1:
        return s
    return s[-1]+reverse_string_recursive(s[:-1])
# Example
print(reverse_string_recursive("Hello"))


# 6.Write a recursive function that determines whether a given integer n is a prime number by checking for divisibility by integers less than n.
def is_prime_recursive(n: int,divisor:int=None)->bool:
    if n<2:
        return False
    if divisor is None:
        divisor=n-1
    if divisor==1:
        return True
    if n%divisor==0:
        return False
    return is_prime_recursive(n,divisor-1)
# Example
print(is_prime_recursive(6))


 # 7.Write a recursive function that takes in one argument n and computes Fn, the nth value of theFibonacci sequence.
# Recall that the Fibonacci sequence is defined by the relation Fn = Fn−1 + Fn−2where F0=0andF1=1
def fibonacci_recursive(n:int)->int:
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
# Example
print(fibonacci_recursive(5))
