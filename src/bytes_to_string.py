#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

In Python, how to convert bytes to string?

En Python, ¿Cómo convertir bytes a string?
'''

#create a bytes object
b = b'El ni\xc3\xb1o come camar\xc3\xb3n'
print(b)

#return an encoded version of 'b' as a string object. Default encoding
#is 'utf-8'.
s = b.decode()
print(type(s))
print(s)

#create a bytes object encoded using 'cp855'
b = b'\xd8\xe1\xb7\xeb\xa8\xe5 \xd2\xb7\xe1'

#return a string using decode 'cp855'
s = b.decode('cp855')
print(s)
