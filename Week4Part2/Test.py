# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 21:28:43 2018

@author: Dyass
"""
def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
fancy_divide([0, 2, 4],0)