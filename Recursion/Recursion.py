# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:59:36 2021

@author: Abeg
"""
#factorial using recursion
"""def factorial(n):
  if n==0 or n==1:
    return 1
  elif n==2:
    return n  
  else:
    return n*factorial(n-1)
n=int(input("enter the no"))
print(factorial(n))"""
#fibonancci using recursion
"""def fiborecursively(n):
  if n<=1:
    return n
  else:
    return(fiborecursively(n-1) + fiborecursively(n-2))
for i in range(0,10):
  print(fiborecursively(i))"""
  
#reverse a string with recursion
def reverse(string): 
  if len(string) == 0: 
      return
  temp = string[0] 
  reverse(string[1:]) 
  print(temp,end="")
string=(input())
reverse(string)