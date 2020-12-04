#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: Matrix.py
@time: 2020/11/28
@desc:
'''
from .Vector import Vector
class Matrix:
    def __init__(self,list2d):
        self._values = [row[:] for row in list2d]
    @classmethod
    def zero(cls,r,c):
        return cls([[0]*c for  _ in range(r)])
    @classmethod
    def identity(cls,n):
        '''返回N行N列单位矩阵'''
        m= [[0]*n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    def __add__(self, another):
        '''矩阵加法'''
        assert self.shape() == another.shape(), \
            "ERROR in adding ,shape of matrix must be same"
        return Matrix([[a + b for a,b in zip(self.row_vector(i),another.row_vector(i))]
                       for i in range(self.row_num())])
    def __sub__(self, another):
        '''矩阵减法'''
        assert self.shape() == another.shape(), \
            "ERROR in subtracting ,shape of matrix must be same"
        return Matrix([[a - b for a,b in zip(self.row_vector(i),another.row_vector(i))]
                       for i in range(self.row_num())])

    def __mul__(self, k):
        """标量乘矩阵-矩阵乘法:self*k"""
        return Matrix([[e * k for e in self.row_vector(i)]
                       for i in range(self.row_num())])


    def __rmul__(self, k):
        """标量乘矩阵-矩阵乘法:self*k"""
        return Matrix([[e * k for e in self.row_vector(i)]
                       for i in range(self.row_num())])


    def dot(self,another):
        """返回矩阵乘法结果"""
        if isinstance(another,Vector):
            """矩阵向量乘法"""
            assert self.col_num() == len(another),\
                "ERROR in Matrix-Vector multiplication"
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])
        if isinstance(another,Matrix):
            """矩阵x矩阵"""
            assert self.col_num() == another.row_num() ,\
                "ERROR in matrix-matrix multiplication"
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num ())
                            for i in range(self.row_num()) ]])


    def __truediv__(self, k):
        """返回向量除法的结果矩阵: self / k """
        return (1/k)*self
    def __pos__(self):
        """当前结果取正"""
        return 1*self
    def __neg__(self):
        return -1*self


    def row_vector(self,index):
        '''返回矩阵第index个行向量'''

        return Vector(self._values[index])

    def col_vector(self,index):
        '''返回矩阵第index个列向量'''
        return Vector([row[index] for row in self._values])


    def __getitem__(self, pos):
        """返回pos的位置元素"""
        r,c=pos
        return self._values[r][c]

    def size(self):
        '''返回矩阵的元素个数'''
        r,c = self.shape()
        return r*c


    def shape(self):
        '''返回矩阵的性状：（行数，列数）'''
        return len(self._values),len(self._values[0])
    def row_num(self):
        '''
        返回矩阵的行数
        :return:
        '''
        return self.shape()[0]

    def col_num(self):
        '''返回矩阵的列数'''
        return self.shape()[1]

    def __repr__(self):
        return "Matrix({}）".format(self._values)

    __len__ = row_num
    __str__ = __repr__
