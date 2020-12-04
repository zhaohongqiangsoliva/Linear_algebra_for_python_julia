#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: main_matrix.py
@time: 2020/11/28
@desc:
'''
from playL_A.Matrix import Matrix
from playL_A.Vector import Vector

if __name__ == '__main__':
    matrix = Matrix([[1,2],[3,4]])
    print(matrix)
    matrix2 = Matrix([[3,5],[7,8]])
    print("add :{}".format(matrix+matrix2))
    print("subtract :{}".format(matrix - matrix2))
    print("scalar-mul: {}".format(matrix*2))
    print("scalar-mul: {}".format(2*matrix*2))
    print("zero_2_3:{}".format(Matrix.zero(2,3)))
    print("pos{}".format(matrix/2))
    print("matrix . matrix :{}".format(matrix.dot(matrix2)))
    a=Vector([1,2])
    b=Vector([3,4])
    print(a.dot(b))
    I = Matrix.identity(2)
    print(I)
    print("A.dot(I)={}".format(matrix.dot(I)))
