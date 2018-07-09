# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:31:00 2018

@author: Dyass
"""
"""
    Topics:
        Bubble Sort
"""
def bubble_sort(L):
  swap=False
  while not swap:
      swap=True
      for j in range(1,len(L)):
          if L[j-1]>L[j]:
              swap=False
              temp=L[j]
              L[j]=L[j-1]
              L[j-1]=temp 
  return L
#Complexity is O(n^2)
L=[99,1,6,9,4,110]
print(bubble_sort(L))