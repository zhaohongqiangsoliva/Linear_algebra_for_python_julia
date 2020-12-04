#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: main_numpy.py
@time: 2020/12/3
@desc:
'''
import numpy as np

A = np.array([[1,2],[3,4]])
#单位矩阵
I = np.identity(2)
print(I)
#逆矩阵
invA = np.linalg.inv(A)
print(invA.dot(A))