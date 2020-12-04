#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: main_linearsystem.py
@time: 2020/12/3
@desc:
'''
from playL_A.Matrix import Matrix
from playL_A.Vector import Vector
from playL_A.LinearSystem import LinearSystem

if __name__ == '__main__':

    A = Matrix([[1,2,4],[3,7,2],[2,3,3]])
    b=Vector([7,-11,1])
    ls = LinearSystem(A,b)
    ls.gauss_jordan_elimination()
    ls.fany_print()
