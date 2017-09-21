# Greg Stewart 2017

from __future__ import print_function
from pythtb import *
import numpy as np
import pylab as plt

lat = [[14.9849996567, 0.0000000000, 0.0000000000], \
	[0.0000000000, 14.9849996567, 0.0000000000], \
	[0.0000000000, 0.0000000000, 4.2649998665]]

orb = [[0.866558909, 0.500000000, 0.833068728], \
	[0.866558909, 0.500000000, 0.499909639], \
	[0.857349873, 0.581546485, 0.333159149], \
	[0.857349873, 0.581546485, 0.000000000], \
	[0.830256701, 0.659022331, 0.833068728], \
	[0.830256701, 0.659022331, 0.499909639], \
	[0.786547184, 0.728557110, 0.333159149], \
	[0.786547184, 0.728557110, 0.000000000], \
	[0.728557110, 0.786547184, 0.833068728], \
	[0.728557110, 0.786547184, 0.499909639], \
	[0.659022331, 0.830256701, 0.333159149], \
	[0.659022331, 0.830256701, 0.000000000], \
	[0.581546485, 0.857349873, 0.833068728], \
	[0.581546485, 0.857349873, 0.499909639], \
	[0.500000000, 0.866558909, 0.333159149], \
	[0.500000000, 0.866558909, 0.000000000], \
	[0.418453485, 0.857349873, 0.833068728], \
	[0.418453485, 0.857349873, 0.499909639], \
	[0.340977669, 0.830256701, 0.333159149], \
	[0.340977669, 0.830256701, 0.000000000], \
	[0.271442890, 0.786547184, 0.833068728], \
	[0.271442890, 0.786547184, 0.499909639], \
	[0.213452786, 0.728557110, 0.333159149], \
	[0.213452786, 0.728557110, 0.000000000], \
	[0.169743329, 0.659022331, 0.833068728], \
	[0.169743329, 0.659022331, 0.499909639], \
	[0.142650127, 0.581546485, 0.333159149], \
	[0.142650127, 0.581546485, 0.000000000], \
	[0.133441120, 0.500000000, 0.833068728], \
	[0.133441120, 0.500000000, 0.499909639], \
	[0.142650127, 0.418453485, 0.333159149], \
	[0.142650127, 0.418453485, 0.000000000], \
	[0.169743329, 0.340977669, 0.833068728], \
	[0.169743329, 0.340977669, 0.499909639], \
	[0.213452786, 0.271442890, 0.333159149], \
	[0.213452786, 0.271442890, 0.000000000], \
	[0.271442890, 0.213452786, 0.833068728], \
	[0.271442890, 0.213452786, 0.499909639], \
	[0.340977669, 0.169743329, 0.333159149], \
	[0.340977669, 0.169743329, 0.000000000], \
	[0.418453485, 0.142650127, 0.833068728], \
	[0.418453485, 0.142650127, 0.499909639], \
	[0.500000000, 0.133441120, 0.333159149], \
	[0.500000000, 0.133441120, 0.000000000], \
	[0.581546485, 0.142650127, 0.833068728], \
	[0.581546485, 0.142650127, 0.499909639], \
	[0.659022331, 0.169743329, 0.333159149], \
	[0.659022331, 0.169743329, 0.000000000], \
	[0.728557110, 0.213452786, 0.833068728], \
	[0.728557110, 0.213452786, 0.499909639], \
	[0.786547184, 0.271442890, 0.333159149], \
	[0.786547184, 0.271442890, 0.000000000], \
	[0.830256701, 0.340977669, 0.833068728], \
	[0.830256701, 0.340977669, 0.499909639], \
	[0.857349873, 0.418453485, 0.333159149], \
	[0.857349873, 0.418453485, 0.000000000]]

my_model = tb_model(1, 3, lat, orb, per=[2])

# set model parameters
delta = 0.0
t1 = -1.8
t2 = 0.
t3 = 0.

my_model.set_onsite([delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta])

# set hopping parameters for connected orbitals
# (amplitude, i, j, [lattice vector to cell containing j])
my_model.set_hop(t3, 0, 1, [0, 0, 1])
my_model.set_hop(t2, 0, 2, [0, 0, 1])
my_model.set_hop(t1, 0, 3, [0, 0, 1])
my_model.set_hop(t3, 0, 5, [0, 0, 1])
my_model.set_hop(t3, 0, 7, [0, 0, 1])
my_model.set_hop(t3, 0, 51, [0, 0, 1])
my_model.set_hop(t3, 0, 53, [0, 0, 1])
my_model.set_hop(t2, 0, 54, [0, 0, 1])
my_model.set_hop(t1, 0, 55, [0, 0, 1])
my_model.set_hop(t1, 0, 1, [0, 0, 0])
my_model.set_hop(t2, 0, 2, [0, 0, 0])
my_model.set_hop(t3, 0, 3, [0, 0, 0])
my_model.set_hop(t2, 0, 4, [0, 0, 0])
my_model.set_hop(t3, 0, 5, [0, 0, 0])
my_model.set_hop(t2, 0, 52, [0, 0, 0])
my_model.set_hop(t3, 0, 53, [0, 0, 0])
my_model.set_hop(t2, 0, 54, [0, 0, 0])
my_model.set_hop(t3, 0, 55, [0, 0, 0])
my_model.set_hop(t1, 1, 2, [0, 0, 0])
my_model.set_hop(t2, 1, 3, [0, 0, 0])
my_model.set_hop(t3, 1, 4, [0, 0, 0])
my_model.set_hop(t2, 1, 5, [0, 0, 0])
my_model.set_hop(t3, 1, 6, [0, 0, 0])
my_model.set_hop(t3, 1, 50, [0, 0, 0])
my_model.set_hop(t3, 1, 52, [0, 0, 0])
my_model.set_hop(t2, 1, 53, [0, 0, 0])
my_model.set_hop(t1, 1, 54, [0, 0, 0])
my_model.set_hop(t2, 1, 55, [0, 0, 0])
my_model.set_hop(t1, 2, 3, [0, 0, 0])
my_model.set_hop(t2, 2, 4, [0, 0, 0])
my_model.set_hop(t1, 2, 5, [0, 0, 0])
my_model.set_hop(t2, 2, 6, [0, 0, 0])
my_model.set_hop(t3, 2, 7, [0, 0, 0])
my_model.set_hop(t3, 2, 9, [0, 0, 0])
my_model.set_hop(t3, 2, 53, [0, 0, 0])
my_model.set_hop(t2, 2, 54, [0, 0, 0])
my_model.set_hop(t3, 2, 55, [0, 0, 0])
my_model.set_hop(t3, 3, 4, [0, 0, 0])
my_model.set_hop(t2, 3, 5, [0, 0, 0])
my_model.set_hop(t3, 3, 6, [0, 0, 0])
my_model.set_hop(t2, 3, 7, [0, 0, 0])
my_model.set_hop(t3, 3, 54, [0, 0, 0])
my_model.set_hop(t2, 3, 55, [0, 0, 0])
my_model.set_hop(t3, 4, 1, [0, 0, 1])
my_model.set_hop(t2, 4, 2, [0, 0, 1])
my_model.set_hop(t1, 4, 3, [0, 0, 1])
my_model.set_hop(t3, 4, 5, [0, 0, 1])
my_model.set_hop(t2, 4, 6, [0, 0, 1])
my_model.set_hop(t1, 4, 7, [0, 0, 1])
my_model.set_hop(t3, 4, 9, [0, 0, 1])
my_model.set_hop(t3, 4, 11, [0, 0, 1])
my_model.set_hop(t3, 4, 55, [0, 0, 1])
my_model.set_hop(t1, 4, 5, [0, 0, 0])
my_model.set_hop(t2, 4, 6, [0, 0, 0])
my_model.set_hop(t3, 4, 7, [0, 0, 0])
my_model.set_hop(t2, 4, 8, [0, 0, 0])
my_model.set_hop(t3, 4, 9, [0, 0, 0])
my_model.set_hop(t1, 5, 6, [0, 0, 0])
my_model.set_hop(t2, 5, 7, [0, 0, 0])
my_model.set_hop(t3, 5, 8, [0, 0, 0])
my_model.set_hop(t2, 5, 9, [0, 0, 0])
my_model.set_hop(t3, 5, 10, [0, 0, 0])
my_model.set_hop(t3, 5, 54, [0, 0, 0])
my_model.set_hop(t1, 6, 7, [0, 0, 0])
my_model.set_hop(t2, 6, 8, [0, 0, 0])
my_model.set_hop(t1, 6, 9, [0, 0, 0])
my_model.set_hop(t2, 6, 10, [0, 0, 0])
my_model.set_hop(t3, 6, 11, [0, 0, 0])
my_model.set_hop(t3, 6, 13, [0, 0, 0])
my_model.set_hop(t3, 7, 8, [0, 0, 0])
my_model.set_hop(t2, 7, 9, [0, 0, 0])
my_model.set_hop(t3, 7, 10, [0, 0, 0])
my_model.set_hop(t2, 7, 11, [0, 0, 0])
my_model.set_hop(t3, 8, 3, [0, 0, 1])
my_model.set_hop(t3, 8, 5, [0, 0, 1])
my_model.set_hop(t2, 8, 6, [0, 0, 1])
my_model.set_hop(t1, 8, 7, [0, 0, 1])
my_model.set_hop(t3, 8, 9, [0, 0, 1])
my_model.set_hop(t2, 8, 10, [0, 0, 1])
my_model.set_hop(t1, 8, 11, [0, 0, 1])
my_model.set_hop(t3, 8, 13, [0, 0, 1])
my_model.set_hop(t3, 8, 15, [0, 0, 1])
my_model.set_hop(t1, 8, 9, [0, 0, 0])
my_model.set_hop(t2, 8, 10, [0, 0, 0])
my_model.set_hop(t3, 8, 11, [0, 0, 0])
my_model.set_hop(t2, 8, 12, [0, 0, 0])
my_model.set_hop(t3, 8, 13, [0, 0, 0])
my_model.set_hop(t1, 9, 10, [0, 0, 0])
my_model.set_hop(t2, 9, 11, [0, 0, 0])
my_model.set_hop(t3, 9, 12, [0, 0, 0])
my_model.set_hop(t2, 9, 13, [0, 0, 0])
my_model.set_hop(t3, 9, 14, [0, 0, 0])
my_model.set_hop(t1, 10, 11, [0, 0, 0])
my_model.set_hop(t2, 10, 12, [0, 0, 0])
my_model.set_hop(t1, 10, 13, [0, 0, 0])
my_model.set_hop(t2, 10, 14, [0, 0, 0])
my_model.set_hop(t3, 10, 15, [0, 0, 0])
my_model.set_hop(t3, 10, 17, [0, 0, 0])
my_model.set_hop(t3, 11, 12, [0, 0, 0])
my_model.set_hop(t2, 11, 13, [0, 0, 0])
my_model.set_hop(t3, 11, 14, [0, 0, 0])
my_model.set_hop(t2, 11, 15, [0, 0, 0])
my_model.set_hop(t3, 12, 7, [0, 0, 1])
my_model.set_hop(t3, 12, 9, [0, 0, 1])
my_model.set_hop(t2, 12, 10, [0, 0, 1])
my_model.set_hop(t1, 12, 11, [0, 0, 1])
my_model.set_hop(t3, 12, 13, [0, 0, 1])
my_model.set_hop(t2, 12, 14, [0, 0, 1])
my_model.set_hop(t1, 12, 15, [0, 0, 1])
my_model.set_hop(t3, 12, 17, [0, 0, 1])
my_model.set_hop(t3, 12, 19, [0, 0, 1])
my_model.set_hop(t1, 12, 13, [0, 0, 0])
my_model.set_hop(t2, 12, 14, [0, 0, 0])
my_model.set_hop(t3, 12, 15, [0, 0, 0])
my_model.set_hop(t2, 12, 16, [0, 0, 0])
my_model.set_hop(t3, 12, 17, [0, 0, 0])
my_model.set_hop(t1, 13, 14, [0, 0, 0])
my_model.set_hop(t2, 13, 15, [0, 0, 0])
my_model.set_hop(t3, 13, 16, [0, 0, 0])
my_model.set_hop(t2, 13, 17, [0, 0, 0])
my_model.set_hop(t3, 13, 18, [0, 0, 0])
my_model.set_hop(t1, 14, 15, [0, 0, 0])
my_model.set_hop(t2, 14, 16, [0, 0, 0])
my_model.set_hop(t1, 14, 17, [0, 0, 0])
my_model.set_hop(t2, 14, 18, [0, 0, 0])
my_model.set_hop(t3, 14, 19, [0, 0, 0])
my_model.set_hop(t3, 14, 21, [0, 0, 0])
my_model.set_hop(t3, 15, 16, [0, 0, 0])
my_model.set_hop(t2, 15, 17, [0, 0, 0])
my_model.set_hop(t3, 15, 18, [0, 0, 0])
my_model.set_hop(t2, 15, 19, [0, 0, 0])
my_model.set_hop(t3, 16, 11, [0, 0, 1])
my_model.set_hop(t3, 16, 13, [0, 0, 1])
my_model.set_hop(t2, 16, 14, [0, 0, 1])
my_model.set_hop(t1, 16, 15, [0, 0, 1])
my_model.set_hop(t3, 16, 17, [0, 0, 1])
my_model.set_hop(t2, 16, 18, [0, 0, 1])
my_model.set_hop(t1, 16, 19, [0, 0, 1])
my_model.set_hop(t3, 16, 21, [0, 0, 1])
my_model.set_hop(t3, 16, 23, [0, 0, 1])
my_model.set_hop(t1, 16, 17, [0, 0, 0])
my_model.set_hop(t2, 16, 18, [0, 0, 0])
my_model.set_hop(t3, 16, 19, [0, 0, 0])
my_model.set_hop(t2, 16, 20, [0, 0, 0])
my_model.set_hop(t3, 16, 21, [0, 0, 0])
my_model.set_hop(t1, 17, 18, [0, 0, 0])
my_model.set_hop(t2, 17, 19, [0, 0, 0])
my_model.set_hop(t3, 17, 20, [0, 0, 0])
my_model.set_hop(t2, 17, 21, [0, 0, 0])
my_model.set_hop(t3, 17, 22, [0, 0, 0])
my_model.set_hop(t1, 18, 19, [0, 0, 0])
my_model.set_hop(t2, 18, 20, [0, 0, 0])
my_model.set_hop(t1, 18, 21, [0, 0, 0])
my_model.set_hop(t2, 18, 22, [0, 0, 0])
my_model.set_hop(t3, 18, 23, [0, 0, 0])
my_model.set_hop(t3, 18, 25, [0, 0, 0])
my_model.set_hop(t3, 19, 20, [0, 0, 0])
my_model.set_hop(t2, 19, 21, [0, 0, 0])
my_model.set_hop(t3, 19, 22, [0, 0, 0])
my_model.set_hop(t2, 19, 23, [0, 0, 0])
my_model.set_hop(t3, 20, 15, [0, 0, 1])
my_model.set_hop(t3, 20, 17, [0, 0, 1])
my_model.set_hop(t2, 20, 18, [0, 0, 1])
my_model.set_hop(t1, 20, 19, [0, 0, 1])
my_model.set_hop(t3, 20, 21, [0, 0, 1])
my_model.set_hop(t2, 20, 22, [0, 0, 1])
my_model.set_hop(t1, 20, 23, [0, 0, 1])
my_model.set_hop(t3, 20, 25, [0, 0, 1])
my_model.set_hop(t3, 20, 27, [0, 0, 1])
my_model.set_hop(t1, 20, 21, [0, 0, 0])
my_model.set_hop(t2, 20, 22, [0, 0, 0])
my_model.set_hop(t3, 20, 23, [0, 0, 0])
my_model.set_hop(t2, 20, 24, [0, 0, 0])
my_model.set_hop(t3, 20, 25, [0, 0, 0])
my_model.set_hop(t1, 21, 22, [0, 0, 0])
my_model.set_hop(t2, 21, 23, [0, 0, 0])
my_model.set_hop(t3, 21, 24, [0, 0, 0])
my_model.set_hop(t2, 21, 25, [0, 0, 0])
my_model.set_hop(t3, 21, 26, [0, 0, 0])
my_model.set_hop(t1, 22, 23, [0, 0, 0])
my_model.set_hop(t2, 22, 24, [0, 0, 0])
my_model.set_hop(t1, 22, 25, [0, 0, 0])
my_model.set_hop(t2, 22, 26, [0, 0, 0])
my_model.set_hop(t3, 22, 27, [0, 0, 0])
my_model.set_hop(t3, 22, 29, [0, 0, 0])
my_model.set_hop(t3, 23, 24, [0, 0, 0])
my_model.set_hop(t2, 23, 25, [0, 0, 0])
my_model.set_hop(t3, 23, 26, [0, 0, 0])
my_model.set_hop(t2, 23, 27, [0, 0, 0])
my_model.set_hop(t3, 24, 19, [0, 0, 1])
my_model.set_hop(t3, 24, 21, [0, 0, 1])
my_model.set_hop(t2, 24, 22, [0, 0, 1])
my_model.set_hop(t1, 24, 23, [0, 0, 1])
my_model.set_hop(t3, 24, 25, [0, 0, 1])
my_model.set_hop(t2, 24, 26, [0, 0, 1])
my_model.set_hop(t1, 24, 27, [0, 0, 1])
my_model.set_hop(t3, 24, 29, [0, 0, 1])
my_model.set_hop(t3, 24, 31, [0, 0, 1])
my_model.set_hop(t1, 24, 25, [0, 0, 0])
my_model.set_hop(t2, 24, 26, [0, 0, 0])
my_model.set_hop(t3, 24, 27, [0, 0, 0])
my_model.set_hop(t2, 24, 28, [0, 0, 0])
my_model.set_hop(t3, 24, 29, [0, 0, 0])
my_model.set_hop(t1, 25, 26, [0, 0, 0])
my_model.set_hop(t2, 25, 27, [0, 0, 0])
my_model.set_hop(t3, 25, 28, [0, 0, 0])
my_model.set_hop(t2, 25, 29, [0, 0, 0])
my_model.set_hop(t3, 25, 30, [0, 0, 0])
my_model.set_hop(t1, 26, 27, [0, 0, 0])
my_model.set_hop(t2, 26, 28, [0, 0, 0])
my_model.set_hop(t1, 26, 29, [0, 0, 0])
my_model.set_hop(t2, 26, 30, [0, 0, 0])
my_model.set_hop(t3, 26, 31, [0, 0, 0])
my_model.set_hop(t3, 26, 33, [0, 0, 0])
my_model.set_hop(t3, 27, 28, [0, 0, 0])
my_model.set_hop(t2, 27, 29, [0, 0, 0])
my_model.set_hop(t3, 27, 30, [0, 0, 0])
my_model.set_hop(t2, 27, 31, [0, 0, 0])
my_model.set_hop(t3, 28, 23, [0, 0, 1])
my_model.set_hop(t3, 28, 25, [0, 0, 1])
my_model.set_hop(t2, 28, 26, [0, 0, 1])
my_model.set_hop(t1, 28, 27, [0, 0, 1])
my_model.set_hop(t3, 28, 29, [0, 0, 1])
my_model.set_hop(t2, 28, 30, [0, 0, 1])
my_model.set_hop(t1, 28, 31, [0, 0, 1])
my_model.set_hop(t3, 28, 33, [0, 0, 1])
my_model.set_hop(t3, 28, 35, [0, 0, 1])
my_model.set_hop(t1, 28, 29, [0, 0, 0])
my_model.set_hop(t2, 28, 30, [0, 0, 0])
my_model.set_hop(t3, 28, 31, [0, 0, 0])
my_model.set_hop(t2, 28, 32, [0, 0, 0])
my_model.set_hop(t3, 28, 33, [0, 0, 0])
my_model.set_hop(t1, 29, 30, [0, 0, 0])
my_model.set_hop(t2, 29, 31, [0, 0, 0])
my_model.set_hop(t3, 29, 32, [0, 0, 0])
my_model.set_hop(t2, 29, 33, [0, 0, 0])
my_model.set_hop(t3, 29, 34, [0, 0, 0])
my_model.set_hop(t1, 30, 31, [0, 0, 0])
my_model.set_hop(t2, 30, 32, [0, 0, 0])
my_model.set_hop(t1, 30, 33, [0, 0, 0])
my_model.set_hop(t2, 30, 34, [0, 0, 0])
my_model.set_hop(t3, 30, 35, [0, 0, 0])
my_model.set_hop(t3, 30, 37, [0, 0, 0])
my_model.set_hop(t3, 31, 32, [0, 0, 0])
my_model.set_hop(t2, 31, 33, [0, 0, 0])
my_model.set_hop(t3, 31, 34, [0, 0, 0])
my_model.set_hop(t2, 31, 35, [0, 0, 0])
my_model.set_hop(t3, 32, 27, [0, 0, 1])
my_model.set_hop(t3, 32, 29, [0, 0, 1])
my_model.set_hop(t2, 32, 30, [0, 0, 1])
my_model.set_hop(t1, 32, 31, [0, 0, 1])
my_model.set_hop(t3, 32, 33, [0, 0, 1])
my_model.set_hop(t2, 32, 34, [0, 0, 1])
my_model.set_hop(t1, 32, 35, [0, 0, 1])
my_model.set_hop(t3, 32, 37, [0, 0, 1])
my_model.set_hop(t3, 32, 39, [0, 0, 1])
my_model.set_hop(t1, 32, 33, [0, 0, 0])
my_model.set_hop(t2, 32, 34, [0, 0, 0])
my_model.set_hop(t3, 32, 35, [0, 0, 0])
my_model.set_hop(t2, 32, 36, [0, 0, 0])
my_model.set_hop(t3, 32, 37, [0, 0, 0])
my_model.set_hop(t1, 33, 34, [0, 0, 0])
my_model.set_hop(t2, 33, 35, [0, 0, 0])
my_model.set_hop(t3, 33, 36, [0, 0, 0])
my_model.set_hop(t2, 33, 37, [0, 0, 0])
my_model.set_hop(t3, 33, 38, [0, 0, 0])
my_model.set_hop(t1, 34, 35, [0, 0, 0])
my_model.set_hop(t2, 34, 36, [0, 0, 0])
my_model.set_hop(t1, 34, 37, [0, 0, 0])
my_model.set_hop(t2, 34, 38, [0, 0, 0])
my_model.set_hop(t3, 34, 39, [0, 0, 0])
my_model.set_hop(t3, 34, 41, [0, 0, 0])
my_model.set_hop(t3, 35, 36, [0, 0, 0])
my_model.set_hop(t2, 35, 37, [0, 0, 0])
my_model.set_hop(t3, 35, 38, [0, 0, 0])
my_model.set_hop(t2, 35, 39, [0, 0, 0])
my_model.set_hop(t3, 36, 31, [0, 0, 1])
my_model.set_hop(t3, 36, 33, [0, 0, 1])
my_model.set_hop(t2, 36, 34, [0, 0, 1])
my_model.set_hop(t1, 36, 35, [0, 0, 1])
my_model.set_hop(t3, 36, 37, [0, 0, 1])
my_model.set_hop(t2, 36, 38, [0, 0, 1])
my_model.set_hop(t1, 36, 39, [0, 0, 1])
my_model.set_hop(t3, 36, 41, [0, 0, 1])
my_model.set_hop(t3, 36, 43, [0, 0, 1])
my_model.set_hop(t1, 36, 37, [0, 0, 0])
my_model.set_hop(t2, 36, 38, [0, 0, 0])
my_model.set_hop(t3, 36, 39, [0, 0, 0])
my_model.set_hop(t2, 36, 40, [0, 0, 0])
my_model.set_hop(t3, 36, 41, [0, 0, 0])
my_model.set_hop(t1, 37, 38, [0, 0, 0])
my_model.set_hop(t2, 37, 39, [0, 0, 0])
my_model.set_hop(t3, 37, 40, [0, 0, 0])
my_model.set_hop(t2, 37, 41, [0, 0, 0])
my_model.set_hop(t3, 37, 42, [0, 0, 0])
my_model.set_hop(t1, 38, 39, [0, 0, 0])
my_model.set_hop(t2, 38, 40, [0, 0, 0])
my_model.set_hop(t1, 38, 41, [0, 0, 0])
my_model.set_hop(t2, 38, 42, [0, 0, 0])
my_model.set_hop(t3, 38, 43, [0, 0, 0])
my_model.set_hop(t3, 38, 45, [0, 0, 0])
my_model.set_hop(t3, 39, 40, [0, 0, 0])
my_model.set_hop(t2, 39, 41, [0, 0, 0])
my_model.set_hop(t3, 39, 42, [0, 0, 0])
my_model.set_hop(t2, 39, 43, [0, 0, 0])
my_model.set_hop(t3, 40, 35, [0, 0, 1])
my_model.set_hop(t3, 40, 37, [0, 0, 1])
my_model.set_hop(t2, 40, 38, [0, 0, 1])
my_model.set_hop(t1, 40, 39, [0, 0, 1])
my_model.set_hop(t3, 40, 41, [0, 0, 1])
my_model.set_hop(t2, 40, 42, [0, 0, 1])
my_model.set_hop(t1, 40, 43, [0, 0, 1])
my_model.set_hop(t3, 40, 45, [0, 0, 1])
my_model.set_hop(t3, 40, 47, [0, 0, 1])
my_model.set_hop(t1, 40, 41, [0, 0, 0])
my_model.set_hop(t2, 40, 42, [0, 0, 0])
my_model.set_hop(t3, 40, 43, [0, 0, 0])
my_model.set_hop(t2, 40, 44, [0, 0, 0])
my_model.set_hop(t3, 40, 45, [0, 0, 0])
my_model.set_hop(t1, 41, 42, [0, 0, 0])
my_model.set_hop(t2, 41, 43, [0, 0, 0])
my_model.set_hop(t3, 41, 44, [0, 0, 0])
my_model.set_hop(t2, 41, 45, [0, 0, 0])
my_model.set_hop(t3, 41, 46, [0, 0, 0])
my_model.set_hop(t1, 42, 43, [0, 0, 0])
my_model.set_hop(t2, 42, 44, [0, 0, 0])
my_model.set_hop(t1, 42, 45, [0, 0, 0])
my_model.set_hop(t2, 42, 46, [0, 0, 0])
my_model.set_hop(t3, 42, 47, [0, 0, 0])
my_model.set_hop(t3, 42, 49, [0, 0, 0])
my_model.set_hop(t3, 43, 44, [0, 0, 0])
my_model.set_hop(t2, 43, 45, [0, 0, 0])
my_model.set_hop(t3, 43, 46, [0, 0, 0])
my_model.set_hop(t2, 43, 47, [0, 0, 0])
my_model.set_hop(t3, 44, 39, [0, 0, 1])
my_model.set_hop(t3, 44, 41, [0, 0, 1])
my_model.set_hop(t2, 44, 42, [0, 0, 1])
my_model.set_hop(t1, 44, 43, [0, 0, 1])
my_model.set_hop(t3, 44, 45, [0, 0, 1])
my_model.set_hop(t2, 44, 46, [0, 0, 1])
my_model.set_hop(t1, 44, 47, [0, 0, 1])
my_model.set_hop(t3, 44, 49, [0, 0, 1])
my_model.set_hop(t3, 44, 51, [0, 0, 1])
my_model.set_hop(t1, 44, 45, [0, 0, 0])
my_model.set_hop(t2, 44, 46, [0, 0, 0])
my_model.set_hop(t3, 44, 47, [0, 0, 0])
my_model.set_hop(t2, 44, 48, [0, 0, 0])
my_model.set_hop(t3, 44, 49, [0, 0, 0])
my_model.set_hop(t1, 45, 46, [0, 0, 0])
my_model.set_hop(t2, 45, 47, [0, 0, 0])
my_model.set_hop(t3, 45, 48, [0, 0, 0])
my_model.set_hop(t2, 45, 49, [0, 0, 0])
my_model.set_hop(t3, 45, 50, [0, 0, 0])
my_model.set_hop(t1, 46, 47, [0, 0, 0])
my_model.set_hop(t2, 46, 48, [0, 0, 0])
my_model.set_hop(t1, 46, 49, [0, 0, 0])
my_model.set_hop(t2, 46, 50, [0, 0, 0])
my_model.set_hop(t3, 46, 51, [0, 0, 0])
my_model.set_hop(t3, 46, 53, [0, 0, 0])
my_model.set_hop(t3, 47, 48, [0, 0, 0])
my_model.set_hop(t2, 47, 49, [0, 0, 0])
my_model.set_hop(t3, 47, 50, [0, 0, 0])
my_model.set_hop(t2, 47, 51, [0, 0, 0])
my_model.set_hop(t3, 48, 43, [0, 0, 1])
my_model.set_hop(t3, 48, 45, [0, 0, 1])
my_model.set_hop(t2, 48, 46, [0, 0, 1])
my_model.set_hop(t1, 48, 47, [0, 0, 1])
my_model.set_hop(t3, 48, 49, [0, 0, 1])
my_model.set_hop(t2, 48, 50, [0, 0, 1])
my_model.set_hop(t1, 48, 51, [0, 0, 1])
my_model.set_hop(t3, 48, 53, [0, 0, 1])
my_model.set_hop(t3, 48, 55, [0, 0, 1])
my_model.set_hop(t1, 48, 49, [0, 0, 0])
my_model.set_hop(t2, 48, 50, [0, 0, 0])
my_model.set_hop(t3, 48, 51, [0, 0, 0])
my_model.set_hop(t2, 48, 52, [0, 0, 0])
my_model.set_hop(t3, 48, 53, [0, 0, 0])
my_model.set_hop(t1, 49, 50, [0, 0, 0])
my_model.set_hop(t2, 49, 51, [0, 0, 0])
my_model.set_hop(t3, 49, 52, [0, 0, 0])
my_model.set_hop(t2, 49, 53, [0, 0, 0])
my_model.set_hop(t3, 49, 54, [0, 0, 0])
my_model.set_hop(t1, 50, 51, [0, 0, 0])
my_model.set_hop(t2, 50, 52, [0, 0, 0])
my_model.set_hop(t1, 50, 53, [0, 0, 0])
my_model.set_hop(t2, 50, 54, [0, 0, 0])
my_model.set_hop(t3, 50, 55, [0, 0, 0])
my_model.set_hop(t3, 51, 52, [0, 0, 0])
my_model.set_hop(t2, 51, 53, [0, 0, 0])
my_model.set_hop(t3, 51, 54, [0, 0, 0])
my_model.set_hop(t2, 51, 55, [0, 0, 0])
my_model.set_hop(t3, 52, 1, [0, 0, 1])
my_model.set_hop(t3, 52, 3, [0, 0, 1])
my_model.set_hop(t3, 52, 47, [0, 0, 1])
my_model.set_hop(t3, 52, 49, [0, 0, 1])
my_model.set_hop(t2, 52, 50, [0, 0, 1])
my_model.set_hop(t1, 52, 51, [0, 0, 1])
my_model.set_hop(t3, 52, 53, [0, 0, 1])
my_model.set_hop(t2, 52, 54, [0, 0, 1])
my_model.set_hop(t1, 52, 55, [0, 0, 1])
my_model.set_hop(t1, 52, 53, [0, 0, 0])
my_model.set_hop(t2, 52, 54, [0, 0, 0])
my_model.set_hop(t3, 52, 55, [0, 0, 0])
my_model.set_hop(t1, 53, 54, [0, 0, 0])
my_model.set_hop(t2, 53, 55, [0, 0, 0])
my_model.set_hop(t1, 54, 55, [0, 0, 0])

my_model.display()

path = 'fullc'
label = (r'$\pi/a$',r'$\Gamma $',r'$\pi/a$')
nk = 800

(k_vec, k_dist, k_node) = my_model.k_path(path, nk)

print('-'*20)
print('starting calculation')
print('-'*20)
print('Calculating bands . . .')

evals = my_model.solve_all(k_vec)

fig, ax = plt.subplots(figsize=(3,4))

# ax.set_xlim([0, k_node[-1]])
ax.set_xticks(k_node)
ax.set_xticklabels(label)

for n in range(len(k_node)):
	ax.axvline(x=k_node[n], linewidth=0.3, color='black')

ax.set_title('14-0 band structure')
ax.set_xlabel('Path in k-space')
ax.set_ylabel('Band energy')

for xband in range(56):
	ax.plot(k_dist, evals[xband], linewidth=.5, color='black')

# fig.tight_layout()
fig.savefig('14-0.eps')

print('Done.')