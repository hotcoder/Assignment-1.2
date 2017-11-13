#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 01:20:00 2017

@author: z002krv
"""
result=","

for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        result=result+str(i)+","
result = result[1:-1]
print(result)