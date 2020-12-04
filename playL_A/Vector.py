#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: Vector.py
@time: 2020/11/24
@desc:
'''
import math
from ._global import EPSILON



class Vector:
    def __init__(self,lst):
        self._values = list(lst)


    def norm(self):
        '''返回向量的摸:求向量的值'''
        return math.sqrt(sum(e**2 for e in self))


    def normalize(self):
        '''单位向量'''
        if self.norm()<EPSILON:
            raise   ZeroDivisionError("normaliez error , norm is  zero ")
        return Vector(self._values)/self.norm()


    @classmethod
    def zero(cls,dim):
        '''
        零向量
        :param dim:
        :return:
        '''
        return cls([0]*dim)
    


    def __len__(self):
        return len(self._values)


    def __getitem__(self, index):
        return self._values[index]


    def __add__(self, another):
        '''
        向量加法
        :param another:
        :return:
        '''
        assert len(self) == len(another),\
            "ERROR IN adding . Length of vectors must be same "
        return Vector([a + b for a,b in zip(self,another)])


    def __sub__(self, another):
        '''
        向量减法
        :param another:
        :return:
        '''
        assert len(self) == len(another), \
            "ERROR IN subtracting . Length of vectors must be same "
        return Vector([a - b for a, b in zip(self, another)])


    def __mul__(self, k):
        '''
        向量乘法
        :param another:
        :return:
        '''
        return Vector([ k * e for e  in self])
    def __rmul__(self, k):
        '''
                向量乘法
                :param another:
                :return:
                '''
        return self*k
    def dot(self,another):
        '''向量点乘，返回结果标量'''
        assert len(self)== len(another),\
            "ERROR in dt product ,length of vectors must be same"
        return sum(a*b for a,b in zip(self,another))

    def __truediv__(self, k):
        ''' 数量除法的结果向量 :self / K'''
        return (1/k) * self

    def __pos__(self):
        '''
        向量取正
        :return:
        '''
        return 1*self

    def underlying_list(self):
        """返回向量底层列表"""
        return self._values[:]



    def __neg__(self):
        return -1*self


    def __iter__(self):
        '''
        向量迭代器
        :return:
        '''
        return self._values.__iter__()
    def __repr__(self):
        return "Vector({})".format(self._values)


    def __str__(self):
        return "({})".format(", ".join(e  for e in self._values))