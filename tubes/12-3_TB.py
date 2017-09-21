# Greg Stewart 2017

from __future__ import print_function
from pythtb import *
import numpy as np
import pylab as plt

lat = [[14.1359996796, 0.0000000000, 0.0000000000], \
	[0.0000000000, 14.1359996796, 0.0000000000], \
	[0.0000000000, 0.0000000000, 6.5149998665]]

orb = [[0.881642342, 0.500000000, 0.500053763], \
	[0.879732311, 0.537987351, 0.071377039], \
	[0.877327204, 0.556804240, 0.857092440], \
	[0.851648569, 0.648271024, 0.785561919], \
	[0.843796372, 0.665531576, 0.571430802], \
	[0.869828701, 0.594084203, 0.428415686], \
	[0.864664674, 0.612405837, 0.214284614], \
	[0.825686932, 0.698920846, 0.142754078], \
	[0.815358937, 0.714908123, 0.928622961], \
	[0.752541780, 0.786143303, 0.857092440], \
	[0.737969398, 0.798310578, 0.642807841], \
	[0.656901300, 0.847828567, 0.571277261], \
	[0.792368412, 0.745184839, 0.499946237], \
	[0.779847443, 0.759474277, 0.285661638], \
	[0.707126737, 0.820522964, 0.214131102], \
	[0.690856516, 0.830426574, 0.000000000], \
	[0.603351116, 0.867352843, 0.928469479], \
	[0.584958732, 0.872021675, 0.714338362], \
	[0.490450114, 0.881500840, 0.642807841], \
	[0.639569998, 0.855185509, 0.357192159], \
	[0.547537267, 0.878671229, 0.285661638], \
	[0.528578937, 0.880510449, 0.071377039], \
	[0.433787346, 0.875841618, 0.999846518], \
	[0.415111989, 0.872092426, 0.785715401], \
	[0.325908870, 0.839552045, 0.714184880], \
	[0.309214234, 0.830497265, 0.500053763], \
	[0.471633255, 0.880581200, 0.428569227], \
	[0.378539413, 0.861764312, 0.357038677], \
	[0.360642195, 0.855256259, 0.142907575], \
	[0.277239740, 0.809841216, 0.071377039], \
	[0.262101382, 0.798381329, 0.857092440], \
	[0.195817977, 0.730400205, 0.785561919], \
	[0.184711844, 0.714978874, 0.571430802], \
	[0.233593166, 0.773268580, 0.428415686], \
	[0.220364779, 0.759615779, 0.214284614], \
	[0.164904624, 0.682579935, 0.142754078], \
	[0.156203598, 0.665602326, 0.928622961], \
	[0.125926882, 0.575621068, 0.857092440], \
	[0.122672826, 0.556874990, 0.642807841], \
	[0.120267689, 0.461941868, 0.571277261], \
	[0.141418964, 0.630586028, 0.499946237], \
	[0.135406047, 0.612618089, 0.285661638], \
	[0.118852884, 0.519099772, 0.214131102], \
	[0.118357688, 0.500070751, 0.000000000], \
	[0.130171269, 0.405845046, 0.928469479], \
	[0.135335296, 0.387523413, 0.714338362], \
	[0.174383759, 0.301008403, 0.642807841], \
	[0.122602105, 0.443266511, 0.357192159], \
	[0.148351461, 0.351799697, 0.285661638], \
	[0.156132847, 0.334468424, 0.071377039], \
	[0.207631588, 0.254744411, 0.999846518], \
	[0.220223308, 0.240454942, 0.785715401], \
	[0.292944014, 0.179406315, 0.714184880], \
	[0.309214234, 0.169502735, 0.500053763], \
	[0.184641063, 0.285162628, 0.428569227], \
	[0.247458220, 0.213927418, 0.357038677], \
	[0.261959910, 0.201689422, 0.142907575], \
	[0.343027949, 0.152171433, 0.071377039], \
	[0.360500723, 0.144814461, 0.857092440], \
	[0.452533454, 0.121328771, 0.785561919], \
	[0.471491784, 0.119418800, 0.571430802], \
	[0.396578133, 0.132647187, 0.428415686], \
	[0.414970517, 0.127978355, 0.214284614], \
	[0.509479165, 0.118499160, 0.142754078], \
	[0.528437495, 0.119418800, 0.928622961], \
	[0.621531308, 0.138235658, 0.857092440], \
	[0.639428556, 0.144743741, 0.642807841], \
	[0.722831011, 0.190158784, 0.571277261], \
	[0.566141903, 0.124158353, 0.499946237], \
	[0.584817290, 0.127907574, 0.285661638], \
	[0.674020410, 0.160377264, 0.214131102], \
	[0.690715075, 0.169502735, 0.000000000], \
	[0.766477585, 0.226802111, 0.928469479], \
	[0.779706001, 0.240384191, 0.714338362], \
	[0.835166097, 0.317490816, 0.642807841], \
	[0.737827897, 0.201547951, 0.357192159], \
	[0.804182053, 0.269529104, 0.285661638], \
	[0.815288186, 0.284950405, 0.071377039], \
	[0.858581066, 0.369484693, 0.999846518], \
	[0.864664674, 0.387452662, 0.785715401], \
	[0.881147146, 0.480970949, 0.714184880], \
	[0.843796372, 0.334326923, 0.428569227], \
	[0.874002397, 0.424308181, 0.357038677], \
	[0.877327204, 0.443054289, 0.142907575]]

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
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta, delta, \
	delta, delta, delta, delta])

# set hopping parameters for connected orbitals
# (amplitude, i, j, [lattice vector to cell containing j])
my_model.set_hop(t3, 0, 1, [0, 0, 0])
my_model.set_hop(t2, 0, 2, [0, 0, 0])
my_model.set_hop(t3, 0, 3, [0, 0, 0])
my_model.set_hop(t2, 0, 4, [0, 0, 0])
my_model.set_hop(t1, 0, 5, [0, 0, 0])
my_model.set_hop(t2, 0, 6, [0, 0, 0])
my_model.set_hop(t3, 0, 7, [0, 0, 0])
my_model.set_hop(t3, 0, 12, [0, 0, 0])
my_model.set_hop(t3, 0, 74, [0, 0, 0])
my_model.set_hop(t3, 0, 76, [0, 0, 0])
my_model.set_hop(t3, 0, 78, [0, 0, 0])
my_model.set_hop(t2, 0, 79, [0, 0, 0])
my_model.set_hop(t1, 0, 80, [0, 0, 0])
my_model.set_hop(t2, 0, 81, [0, 0, 0])
my_model.set_hop(t1, 0, 82, [0, 0, 0])
my_model.set_hop(t2, 0, 83, [0, 0, 0])
my_model.set_hop(t3, 1, 4, [0, 0, 0])
my_model.set_hop(t2, 1, 5, [0, 0, 0])
my_model.set_hop(t1, 1, 6, [0, 0, 0])
my_model.set_hop(t2, 1, 7, [0, 0, 0])
my_model.set_hop(t3, 1, 13, [0, 0, 0])
my_model.set_hop(t3, 1, 77, [0, 0, 0])
my_model.set_hop(t3, 1, 81, [0, 0, 0])
my_model.set_hop(t2, 1, 82, [0, 0, 0])
my_model.set_hop(t1, 1, 83, [0, 0, 0])
my_model.set_hop(t1, 2, 1, [0, 0, 1])
my_model.set_hop(t3, 2, 5, [0, 0, 1])
my_model.set_hop(t2, 2, 6, [0, 0, 1])
my_model.set_hop(t3, 2, 7, [0, 0, 1])
my_model.set_hop(t3, 2, 82, [0, 0, 1])
my_model.set_hop(t2, 2, 83, [0, 0, 1])
my_model.set_hop(t1, 2, 3, [0, 0, 0])
my_model.set_hop(t2, 2, 4, [0, 0, 0])
my_model.set_hop(t3, 2, 5, [0, 0, 0])
my_model.set_hop(t2, 2, 8, [0, 0, 0])
my_model.set_hop(t3, 2, 9, [0, 0, 0])
my_model.set_hop(t3, 2, 12, [0, 0, 0])
my_model.set_hop(t3, 2, 74, [0, 0, 0])
my_model.set_hop(t3, 2, 78, [0, 0, 0])
my_model.set_hop(t2, 2, 79, [0, 0, 0])
my_model.set_hop(t1, 2, 80, [0, 0, 0])
my_model.set_hop(t3, 2, 82, [0, 0, 0])
my_model.set_hop(t1, 3, 4, [0, 0, 0])
my_model.set_hop(t2, 3, 5, [0, 0, 0])
my_model.set_hop(t3, 3, 6, [0, 0, 0])
my_model.set_hop(t1, 3, 8, [0, 0, 0])
my_model.set_hop(t2, 3, 9, [0, 0, 0])
my_model.set_hop(t3, 3, 10, [0, 0, 0])
my_model.set_hop(t2, 3, 12, [0, 0, 0])
my_model.set_hop(t3, 3, 13, [0, 0, 0])
my_model.set_hop(t3, 3, 79, [0, 0, 0])
my_model.set_hop(t2, 3, 80, [0, 0, 0])
my_model.set_hop(t1, 4, 5, [0, 0, 0])
my_model.set_hop(t2, 4, 6, [0, 0, 0])
my_model.set_hop(t3, 4, 7, [0, 0, 0])
my_model.set_hop(t2, 4, 8, [0, 0, 0])
my_model.set_hop(t3, 4, 9, [0, 0, 0])
my_model.set_hop(t2, 4, 10, [0, 0, 0])
my_model.set_hop(t3, 4, 11, [0, 0, 0])
my_model.set_hop(t1, 4, 12, [0, 0, 0])
my_model.set_hop(t2, 4, 13, [0, 0, 0])
my_model.set_hop(t3, 4, 14, [0, 0, 0])
my_model.set_hop(t3, 4, 80, [0, 0, 0])
my_model.set_hop(t3, 4, 82, [0, 0, 0])
my_model.set_hop(t1, 5, 6, [0, 0, 0])
my_model.set_hop(t2, 5, 7, [0, 0, 0])
my_model.set_hop(t3, 5, 8, [0, 0, 0])
my_model.set_hop(t3, 5, 10, [0, 0, 0])
my_model.set_hop(t2, 5, 12, [0, 0, 0])
my_model.set_hop(t3, 5, 13, [0, 0, 0])
my_model.set_hop(t3, 5, 79, [0, 0, 0])
my_model.set_hop(t2, 5, 80, [0, 0, 0])
my_model.set_hop(t3, 5, 81, [0, 0, 0])
my_model.set_hop(t2, 5, 82, [0, 0, 0])
my_model.set_hop(t3, 5, 83, [0, 0, 0])
my_model.set_hop(t1, 6, 7, [0, 0, 0])
my_model.set_hop(t3, 6, 12, [0, 0, 0])
my_model.set_hop(t2, 6, 13, [0, 0, 0])
my_model.set_hop(t3, 6, 14, [0, 0, 0])
my_model.set_hop(t3, 6, 80, [0, 0, 0])
my_model.set_hop(t3, 6, 82, [0, 0, 0])
my_model.set_hop(t2, 6, 83, [0, 0, 0])
my_model.set_hop(t3, 7, 10, [0, 0, 0])
my_model.set_hop(t2, 7, 12, [0, 0, 0])
my_model.set_hop(t1, 7, 13, [0, 0, 0])
my_model.set_hop(t2, 7, 14, [0, 0, 0])
my_model.set_hop(t3, 7, 15, [0, 0, 0])
my_model.set_hop(t3, 7, 19, [0, 0, 0])
my_model.set_hop(t3, 7, 83, [0, 0, 0])
my_model.set_hop(t3, 8, 1, [0, 0, 1])
my_model.set_hop(t3, 8, 5, [0, 0, 1])
my_model.set_hop(t2, 8, 6, [0, 0, 1])
my_model.set_hop(t1, 8, 7, [0, 0, 1])
my_model.set_hop(t3, 8, 12, [0, 0, 1])
my_model.set_hop(t2, 8, 13, [0, 0, 1])
my_model.set_hop(t3, 8, 14, [0, 0, 1])
my_model.set_hop(t2, 8, 15, [0, 0, 1])
my_model.set_hop(t1, 8, 9, [0, 0, 0])
my_model.set_hop(t2, 8, 10, [0, 0, 0])
my_model.set_hop(t3, 8, 11, [0, 0, 0])
my_model.set_hop(t3, 8, 12, [0, 0, 0])
my_model.set_hop(t3, 8, 16, [0, 0, 0])
my_model.set_hop(t3, 8, 80, [0, 0, 0])
my_model.set_hop(t3, 9, 6, [0, 0, 1])
my_model.set_hop(t2, 9, 7, [0, 0, 1])
my_model.set_hop(t3, 9, 13, [0, 0, 1])
my_model.set_hop(t2, 9, 14, [0, 0, 1])
my_model.set_hop(t1, 9, 15, [0, 0, 1])
my_model.set_hop(t3, 9, 19, [0, 0, 1])
my_model.set_hop(t3, 9, 21, [0, 0, 1])
my_model.set_hop(t1, 9, 10, [0, 0, 0])
my_model.set_hop(t2, 9, 11, [0, 0, 0])
my_model.set_hop(t2, 9, 12, [0, 0, 0])
my_model.set_hop(t3, 9, 13, [0, 0, 0])
my_model.set_hop(t2, 9, 16, [0, 0, 0])
my_model.set_hop(t3, 9, 17, [0, 0, 0])
my_model.set_hop(t3, 9, 19, [0, 0, 0])
my_model.set_hop(t1, 10, 11, [0, 0, 0])
my_model.set_hop(t1, 10, 12, [0, 0, 0])
my_model.set_hop(t2, 10, 13, [0, 0, 0])
my_model.set_hop(t3, 10, 14, [0, 0, 0])
my_model.set_hop(t3, 10, 16, [0, 0, 0])
my_model.set_hop(t2, 10, 17, [0, 0, 0])
my_model.set_hop(t3, 10, 18, [0, 0, 0])
my_model.set_hop(t2, 10, 19, [0, 0, 0])
my_model.set_hop(t3, 10, 20, [0, 0, 0])
my_model.set_hop(t2, 11, 12, [0, 0, 0])
my_model.set_hop(t3, 11, 13, [0, 0, 0])
my_model.set_hop(t2, 11, 14, [0, 0, 0])
my_model.set_hop(t3, 11, 15, [0, 0, 0])
my_model.set_hop(t2, 11, 16, [0, 0, 0])
my_model.set_hop(t1, 11, 17, [0, 0, 0])
my_model.set_hop(t2, 11, 18, [0, 0, 0])
my_model.set_hop(t1, 11, 19, [0, 0, 0])
my_model.set_hop(t2, 11, 20, [0, 0, 0])
my_model.set_hop(t3, 11, 21, [0, 0, 0])
my_model.set_hop(t3, 11, 23, [0, 0, 0])
my_model.set_hop(t3, 11, 26, [0, 0, 0])
my_model.set_hop(t1, 12, 13, [0, 0, 0])
my_model.set_hop(t2, 12, 14, [0, 0, 0])
my_model.set_hop(t3, 12, 15, [0, 0, 0])
my_model.set_hop(t3, 12, 17, [0, 0, 0])
my_model.set_hop(t3, 12, 19, [0, 0, 0])
my_model.set_hop(t1, 13, 14, [0, 0, 0])
my_model.set_hop(t2, 13, 15, [0, 0, 0])
my_model.set_hop(t2, 13, 19, [0, 0, 0])
my_model.set_hop(t3, 13, 20, [0, 0, 0])
my_model.set_hop(t1, 14, 15, [0, 0, 0])
my_model.set_hop(t3, 14, 17, [0, 0, 0])
my_model.set_hop(t1, 14, 19, [0, 0, 0])
my_model.set_hop(t2, 14, 20, [0, 0, 0])
my_model.set_hop(t3, 14, 21, [0, 0, 0])
my_model.set_hop(t3, 14, 26, [0, 0, 0])
my_model.set_hop(t2, 15, 19, [0, 0, 0])
my_model.set_hop(t3, 15, 20, [0, 0, 0])
my_model.set_hop(t2, 15, 21, [0, 0, 0])
my_model.set_hop(t3, 16, 13, [0, 0, 1])
my_model.set_hop(t2, 16, 14, [0, 0, 1])
my_model.set_hop(t1, 16, 15, [0, 0, 1])
my_model.set_hop(t3, 16, 19, [0, 0, 1])
my_model.set_hop(t2, 16, 20, [0, 0, 1])
my_model.set_hop(t1, 16, 21, [0, 0, 1])
my_model.set_hop(t3, 16, 26, [0, 0, 1])
my_model.set_hop(t3, 16, 28, [0, 0, 1])
my_model.set_hop(t1, 16, 17, [0, 0, 0])
my_model.set_hop(t2, 16, 18, [0, 0, 0])
my_model.set_hop(t3, 16, 19, [0, 0, 0])
my_model.set_hop(t2, 16, 22, [0, 0, 0])
my_model.set_hop(t3, 16, 23, [0, 0, 0])
my_model.set_hop(t3, 16, 26, [0, 0, 0])
my_model.set_hop(t1, 17, 18, [0, 0, 0])
my_model.set_hop(t2, 17, 19, [0, 0, 0])
my_model.set_hop(t3, 17, 20, [0, 0, 0])
my_model.set_hop(t3, 17, 22, [0, 0, 0])
my_model.set_hop(t2, 17, 23, [0, 0, 0])
my_model.set_hop(t3, 17, 24, [0, 0, 0])
my_model.set_hop(t2, 17, 26, [0, 0, 0])
my_model.set_hop(t3, 17, 27, [0, 0, 0])
my_model.set_hop(t3, 18, 19, [0, 0, 0])
my_model.set_hop(t2, 18, 20, [0, 0, 0])
my_model.set_hop(t3, 18, 21, [0, 0, 0])
my_model.set_hop(t2, 18, 22, [0, 0, 0])
my_model.set_hop(t1, 18, 23, [0, 0, 0])
my_model.set_hop(t2, 18, 24, [0, 0, 0])
my_model.set_hop(t3, 18, 25, [0, 0, 0])
my_model.set_hop(t1, 18, 26, [0, 0, 0])
my_model.set_hop(t2, 18, 27, [0, 0, 0])
my_model.set_hop(t3, 18, 28, [0, 0, 0])
my_model.set_hop(t3, 18, 30, [0, 0, 0])
my_model.set_hop(t1, 19, 20, [0, 0, 0])
my_model.set_hop(t2, 19, 21, [0, 0, 0])
my_model.set_hop(t2, 19, 26, [0, 0, 0])
my_model.set_hop(t3, 19, 27, [0, 0, 0])
my_model.set_hop(t1, 20, 21, [0, 0, 0])
my_model.set_hop(t3, 20, 23, [0, 0, 0])
my_model.set_hop(t3, 20, 25, [0, 0, 0])
my_model.set_hop(t1, 20, 26, [0, 0, 0])
my_model.set_hop(t2, 20, 27, [0, 0, 0])
my_model.set_hop(t3, 20, 28, [0, 0, 0])
my_model.set_hop(t2, 21, 26, [0, 0, 0])
my_model.set_hop(t3, 21, 27, [0, 0, 0])
my_model.set_hop(t2, 21, 28, [0, 0, 0])
my_model.set_hop(t3, 21, 29, [0, 0, 0])
my_model.set_hop(t3, 22, 15, [0, 0, 1])
my_model.set_hop(t3, 22, 19, [0, 0, 1])
my_model.set_hop(t2, 22, 20, [0, 0, 1])
my_model.set_hop(t1, 22, 21, [0, 0, 1])
my_model.set_hop(t3, 22, 25, [0, 0, 1])
my_model.set_hop(t3, 22, 26, [0, 0, 1])
my_model.set_hop(t2, 22, 27, [0, 0, 1])
my_model.set_hop(t1, 22, 28, [0, 0, 1])
my_model.set_hop(t2, 22, 29, [0, 0, 1])
my_model.set_hop(t3, 22, 34, [0, 0, 1])
my_model.set_hop(t1, 22, 23, [0, 0, 0])
my_model.set_hop(t2, 22, 24, [0, 0, 0])
my_model.set_hop(t3, 22, 25, [0, 0, 0])
my_model.set_hop(t3, 22, 26, [0, 0, 0])
my_model.set_hop(t3, 22, 30, [0, 0, 0])
my_model.set_hop(t1, 23, 24, [0, 0, 0])
my_model.set_hop(t2, 23, 25, [0, 0, 0])
my_model.set_hop(t2, 23, 26, [0, 0, 0])
my_model.set_hop(t3, 23, 27, [0, 0, 0])
my_model.set_hop(t2, 23, 30, [0, 0, 0])
my_model.set_hop(t3, 23, 31, [0, 0, 0])
my_model.set_hop(t3, 23, 33, [0, 0, 0])
my_model.set_hop(t1, 24, 25, [0, 0, 0])
my_model.set_hop(t3, 24, 26, [0, 0, 0])
my_model.set_hop(t2, 24, 27, [0, 0, 0])
my_model.set_hop(t3, 24, 28, [0, 0, 0])
my_model.set_hop(t1, 24, 30, [0, 0, 0])
my_model.set_hop(t2, 24, 31, [0, 0, 0])
my_model.set_hop(t3, 24, 32, [0, 0, 0])
my_model.set_hop(t2, 24, 33, [0, 0, 0])
my_model.set_hop(t3, 24, 34, [0, 0, 0])
my_model.set_hop(t3, 24, 36, [0, 0, 0])
my_model.set_hop(t2, 25, 26, [0, 0, 0])
my_model.set_hop(t1, 25, 27, [0, 0, 0])
my_model.set_hop(t2, 25, 28, [0, 0, 0])
my_model.set_hop(t3, 25, 29, [0, 0, 0])
my_model.set_hop(t2, 25, 30, [0, 0, 0])
my_model.set_hop(t3, 25, 31, [0, 0, 0])
my_model.set_hop(t2, 25, 32, [0, 0, 0])
my_model.set_hop(t1, 25, 33, [0, 0, 0])
my_model.set_hop(t2, 25, 34, [0, 0, 0])
my_model.set_hop(t3, 25, 35, [0, 0, 0])
my_model.set_hop(t3, 25, 40, [0, 0, 0])
my_model.set_hop(t1, 26, 27, [0, 0, 0])
my_model.set_hop(t2, 26, 28, [0, 0, 0])
my_model.set_hop(t3, 26, 29, [0, 0, 0])
my_model.set_hop(t3, 26, 33, [0, 0, 0])
my_model.set_hop(t1, 27, 28, [0, 0, 0])
my_model.set_hop(t2, 27, 29, [0, 0, 0])
my_model.set_hop(t3, 27, 30, [0, 0, 0])
my_model.set_hop(t3, 27, 32, [0, 0, 0])
my_model.set_hop(t2, 27, 33, [0, 0, 0])
my_model.set_hop(t3, 27, 34, [0, 0, 0])
my_model.set_hop(t1, 28, 29, [0, 0, 0])
my_model.set_hop(t3, 28, 33, [0, 0, 0])
my_model.set_hop(t2, 28, 34, [0, 0, 0])
my_model.set_hop(t3, 28, 35, [0, 0, 0])
my_model.set_hop(t3, 29, 32, [0, 0, 0])
my_model.set_hop(t2, 29, 33, [0, 0, 0])
my_model.set_hop(t1, 29, 34, [0, 0, 0])
my_model.set_hop(t2, 29, 35, [0, 0, 0])
my_model.set_hop(t3, 29, 41, [0, 0, 0])
my_model.set_hop(t3, 30, 27, [0, 0, 1])
my_model.set_hop(t2, 30, 28, [0, 0, 1])
my_model.set_hop(t1, 30, 29, [0, 0, 1])
my_model.set_hop(t3, 30, 33, [0, 0, 1])
my_model.set_hop(t2, 30, 34, [0, 0, 1])
my_model.set_hop(t3, 30, 35, [0, 0, 1])
my_model.set_hop(t1, 30, 31, [0, 0, 0])
my_model.set_hop(t2, 30, 32, [0, 0, 0])
my_model.set_hop(t3, 30, 33, [0, 0, 0])
my_model.set_hop(t2, 30, 36, [0, 0, 0])
my_model.set_hop(t3, 30, 37, [0, 0, 0])
my_model.set_hop(t3, 30, 40, [0, 0, 0])
my_model.set_hop(t1, 31, 32, [0, 0, 0])
my_model.set_hop(t2, 31, 33, [0, 0, 0])
my_model.set_hop(t3, 31, 34, [0, 0, 0])
my_model.set_hop(t1, 31, 36, [0, 0, 0])
my_model.set_hop(t2, 31, 37, [0, 0, 0])
my_model.set_hop(t3, 31, 38, [0, 0, 0])
my_model.set_hop(t2, 31, 40, [0, 0, 0])
my_model.set_hop(t3, 31, 41, [0, 0, 0])
my_model.set_hop(t1, 32, 33, [0, 0, 0])
my_model.set_hop(t2, 32, 34, [0, 0, 0])
my_model.set_hop(t3, 32, 35, [0, 0, 0])
my_model.set_hop(t2, 32, 36, [0, 0, 0])
my_model.set_hop(t3, 32, 37, [0, 0, 0])
my_model.set_hop(t2, 32, 38, [0, 0, 0])
my_model.set_hop(t3, 32, 39, [0, 0, 0])
my_model.set_hop(t1, 32, 40, [0, 0, 0])
my_model.set_hop(t2, 32, 41, [0, 0, 0])
my_model.set_hop(t3, 32, 42, [0, 0, 0])
my_model.set_hop(t1, 33, 34, [0, 0, 0])
my_model.set_hop(t2, 33, 35, [0, 0, 0])
my_model.set_hop(t3, 33, 36, [0, 0, 0])
my_model.set_hop(t3, 33, 38, [0, 0, 0])
my_model.set_hop(t2, 33, 40, [0, 0, 0])
my_model.set_hop(t3, 33, 41, [0, 0, 0])
my_model.set_hop(t1, 34, 35, [0, 0, 0])
my_model.set_hop(t3, 34, 40, [0, 0, 0])
my_model.set_hop(t2, 34, 41, [0, 0, 0])
my_model.set_hop(t3, 34, 42, [0, 0, 0])
my_model.set_hop(t3, 35, 38, [0, 0, 0])
my_model.set_hop(t2, 35, 40, [0, 0, 0])
my_model.set_hop(t1, 35, 41, [0, 0, 0])
my_model.set_hop(t2, 35, 42, [0, 0, 0])
my_model.set_hop(t3, 35, 43, [0, 0, 0])
my_model.set_hop(t3, 35, 47, [0, 0, 0])
my_model.set_hop(t3, 36, 29, [0, 0, 1])
my_model.set_hop(t3, 36, 33, [0, 0, 1])
my_model.set_hop(t2, 36, 34, [0, 0, 1])
my_model.set_hop(t1, 36, 35, [0, 0, 1])
my_model.set_hop(t3, 36, 40, [0, 0, 1])
my_model.set_hop(t2, 36, 41, [0, 0, 1])
my_model.set_hop(t3, 36, 42, [0, 0, 1])
my_model.set_hop(t2, 36, 43, [0, 0, 1])
my_model.set_hop(t1, 36, 37, [0, 0, 0])
my_model.set_hop(t2, 36, 38, [0, 0, 0])
my_model.set_hop(t3, 36, 39, [0, 0, 0])
my_model.set_hop(t3, 36, 40, [0, 0, 0])
my_model.set_hop(t3, 36, 44, [0, 0, 0])
my_model.set_hop(t3, 37, 34, [0, 0, 1])
my_model.set_hop(t2, 37, 35, [0, 0, 1])
my_model.set_hop(t3, 37, 41, [0, 0, 1])
my_model.set_hop(t2, 37, 42, [0, 0, 1])
my_model.set_hop(t1, 37, 43, [0, 0, 1])
my_model.set_hop(t3, 37, 47, [0, 0, 1])
my_model.set_hop(t3, 37, 49, [0, 0, 1])
my_model.set_hop(t1, 37, 38, [0, 0, 0])
my_model.set_hop(t2, 37, 39, [0, 0, 0])
my_model.set_hop(t2, 37, 40, [0, 0, 0])
my_model.set_hop(t3, 37, 41, [0, 0, 0])
my_model.set_hop(t2, 37, 44, [0, 0, 0])
my_model.set_hop(t3, 37, 45, [0, 0, 0])
my_model.set_hop(t3, 37, 47, [0, 0, 0])
my_model.set_hop(t1, 38, 39, [0, 0, 0])
my_model.set_hop(t1, 38, 40, [0, 0, 0])
my_model.set_hop(t2, 38, 41, [0, 0, 0])
my_model.set_hop(t3, 38, 42, [0, 0, 0])
my_model.set_hop(t3, 38, 44, [0, 0, 0])
my_model.set_hop(t2, 38, 45, [0, 0, 0])
my_model.set_hop(t3, 38, 46, [0, 0, 0])
my_model.set_hop(t2, 38, 47, [0, 0, 0])
my_model.set_hop(t3, 38, 48, [0, 0, 0])
my_model.set_hop(t2, 39, 40, [0, 0, 0])
my_model.set_hop(t3, 39, 41, [0, 0, 0])
my_model.set_hop(t2, 39, 42, [0, 0, 0])
my_model.set_hop(t3, 39, 43, [0, 0, 0])
my_model.set_hop(t2, 39, 44, [0, 0, 0])
my_model.set_hop(t1, 39, 45, [0, 0, 0])
my_model.set_hop(t2, 39, 46, [0, 0, 0])
my_model.set_hop(t1, 39, 47, [0, 0, 0])
my_model.set_hop(t2, 39, 48, [0, 0, 0])
my_model.set_hop(t3, 39, 49, [0, 0, 0])
my_model.set_hop(t3, 39, 51, [0, 0, 0])
my_model.set_hop(t3, 39, 54, [0, 0, 0])
my_model.set_hop(t1, 40, 41, [0, 0, 0])
my_model.set_hop(t2, 40, 42, [0, 0, 0])
my_model.set_hop(t3, 40, 43, [0, 0, 0])
my_model.set_hop(t3, 40, 45, [0, 0, 0])
my_model.set_hop(t3, 40, 47, [0, 0, 0])
my_model.set_hop(t1, 41, 42, [0, 0, 0])
my_model.set_hop(t2, 41, 43, [0, 0, 0])
my_model.set_hop(t2, 41, 47, [0, 0, 0])
my_model.set_hop(t3, 41, 48, [0, 0, 0])
my_model.set_hop(t1, 42, 43, [0, 0, 0])
my_model.set_hop(t3, 42, 45, [0, 0, 0])
my_model.set_hop(t1, 42, 47, [0, 0, 0])
my_model.set_hop(t2, 42, 48, [0, 0, 0])
my_model.set_hop(t3, 42, 49, [0, 0, 0])
my_model.set_hop(t3, 42, 54, [0, 0, 0])
my_model.set_hop(t2, 43, 47, [0, 0, 0])
my_model.set_hop(t3, 43, 48, [0, 0, 0])
my_model.set_hop(t2, 43, 49, [0, 0, 0])
my_model.set_hop(t3, 44, 41, [0, 0, 1])
my_model.set_hop(t2, 44, 42, [0, 0, 1])
my_model.set_hop(t1, 44, 43, [0, 0, 1])
my_model.set_hop(t3, 44, 47, [0, 0, 1])
my_model.set_hop(t2, 44, 48, [0, 0, 1])
my_model.set_hop(t1, 44, 49, [0, 0, 1])
my_model.set_hop(t3, 44, 54, [0, 0, 1])
my_model.set_hop(t3, 44, 56, [0, 0, 1])
my_model.set_hop(t1, 44, 45, [0, 0, 0])
my_model.set_hop(t2, 44, 46, [0, 0, 0])
my_model.set_hop(t3, 44, 47, [0, 0, 0])
my_model.set_hop(t2, 44, 50, [0, 0, 0])
my_model.set_hop(t3, 44, 51, [0, 0, 0])
my_model.set_hop(t3, 44, 54, [0, 0, 0])
my_model.set_hop(t1, 45, 46, [0, 0, 0])
my_model.set_hop(t2, 45, 47, [0, 0, 0])
my_model.set_hop(t3, 45, 48, [0, 0, 0])
my_model.set_hop(t3, 45, 50, [0, 0, 0])
my_model.set_hop(t2, 45, 51, [0, 0, 0])
my_model.set_hop(t3, 45, 52, [0, 0, 0])
my_model.set_hop(t2, 45, 54, [0, 0, 0])
my_model.set_hop(t3, 45, 55, [0, 0, 0])
my_model.set_hop(t3, 46, 47, [0, 0, 0])
my_model.set_hop(t2, 46, 48, [0, 0, 0])
my_model.set_hop(t3, 46, 49, [0, 0, 0])
my_model.set_hop(t2, 46, 50, [0, 0, 0])
my_model.set_hop(t1, 46, 51, [0, 0, 0])
my_model.set_hop(t2, 46, 52, [0, 0, 0])
my_model.set_hop(t3, 46, 53, [0, 0, 0])
my_model.set_hop(t1, 46, 54, [0, 0, 0])
my_model.set_hop(t2, 46, 55, [0, 0, 0])
my_model.set_hop(t3, 46, 56, [0, 0, 0])
my_model.set_hop(t3, 46, 58, [0, 0, 0])
my_model.set_hop(t1, 47, 48, [0, 0, 0])
my_model.set_hop(t2, 47, 49, [0, 0, 0])
my_model.set_hop(t2, 47, 54, [0, 0, 0])
my_model.set_hop(t3, 47, 55, [0, 0, 0])
my_model.set_hop(t1, 48, 49, [0, 0, 0])
my_model.set_hop(t3, 48, 51, [0, 0, 0])
my_model.set_hop(t3, 48, 53, [0, 0, 0])
my_model.set_hop(t1, 48, 54, [0, 0, 0])
my_model.set_hop(t2, 48, 55, [0, 0, 0])
my_model.set_hop(t3, 48, 56, [0, 0, 0])
my_model.set_hop(t2, 49, 54, [0, 0, 0])
my_model.set_hop(t3, 49, 55, [0, 0, 0])
my_model.set_hop(t2, 49, 56, [0, 0, 0])
my_model.set_hop(t3, 49, 57, [0, 0, 0])
my_model.set_hop(t3, 50, 43, [0, 0, 1])
my_model.set_hop(t3, 50, 47, [0, 0, 1])
my_model.set_hop(t2, 50, 48, [0, 0, 1])
my_model.set_hop(t1, 50, 49, [0, 0, 1])
my_model.set_hop(t3, 50, 53, [0, 0, 1])
my_model.set_hop(t3, 50, 54, [0, 0, 1])
my_model.set_hop(t2, 50, 55, [0, 0, 1])
my_model.set_hop(t1, 50, 56, [0, 0, 1])
my_model.set_hop(t2, 50, 57, [0, 0, 1])
my_model.set_hop(t3, 50, 62, [0, 0, 1])
my_model.set_hop(t1, 50, 51, [0, 0, 0])
my_model.set_hop(t2, 50, 52, [0, 0, 0])
my_model.set_hop(t3, 50, 53, [0, 0, 0])
my_model.set_hop(t3, 50, 54, [0, 0, 0])
my_model.set_hop(t3, 50, 58, [0, 0, 0])
my_model.set_hop(t1, 51, 52, [0, 0, 0])
my_model.set_hop(t2, 51, 53, [0, 0, 0])
my_model.set_hop(t2, 51, 54, [0, 0, 0])
my_model.set_hop(t3, 51, 55, [0, 0, 0])
my_model.set_hop(t2, 51, 58, [0, 0, 0])
my_model.set_hop(t3, 51, 59, [0, 0, 0])
my_model.set_hop(t3, 51, 61, [0, 0, 0])
my_model.set_hop(t1, 52, 53, [0, 0, 0])
my_model.set_hop(t3, 52, 54, [0, 0, 0])
my_model.set_hop(t2, 52, 55, [0, 0, 0])
my_model.set_hop(t3, 52, 56, [0, 0, 0])
my_model.set_hop(t1, 52, 58, [0, 0, 0])
my_model.set_hop(t2, 52, 59, [0, 0, 0])
my_model.set_hop(t3, 52, 60, [0, 0, 0])
my_model.set_hop(t2, 52, 61, [0, 0, 0])
my_model.set_hop(t3, 52, 62, [0, 0, 0])
my_model.set_hop(t3, 52, 64, [0, 0, 0])
my_model.set_hop(t2, 53, 54, [0, 0, 0])
my_model.set_hop(t1, 53, 55, [0, 0, 0])
my_model.set_hop(t2, 53, 56, [0, 0, 0])
my_model.set_hop(t3, 53, 57, [0, 0, 0])
my_model.set_hop(t2, 53, 58, [0, 0, 0])
my_model.set_hop(t3, 53, 59, [0, 0, 0])
my_model.set_hop(t2, 53, 60, [0, 0, 0])
my_model.set_hop(t1, 53, 61, [0, 0, 0])
my_model.set_hop(t2, 53, 62, [0, 0, 0])
my_model.set_hop(t3, 53, 63, [0, 0, 0])
my_model.set_hop(t3, 53, 68, [0, 0, 0])
my_model.set_hop(t1, 54, 55, [0, 0, 0])
my_model.set_hop(t2, 54, 56, [0, 0, 0])
my_model.set_hop(t3, 54, 57, [0, 0, 0])
my_model.set_hop(t3, 54, 61, [0, 0, 0])
my_model.set_hop(t1, 55, 56, [0, 0, 0])
my_model.set_hop(t2, 55, 57, [0, 0, 0])
my_model.set_hop(t3, 55, 58, [0, 0, 0])
my_model.set_hop(t3, 55, 60, [0, 0, 0])
my_model.set_hop(t2, 55, 61, [0, 0, 0])
my_model.set_hop(t3, 55, 62, [0, 0, 0])
my_model.set_hop(t1, 56, 57, [0, 0, 0])
my_model.set_hop(t3, 56, 61, [0, 0, 0])
my_model.set_hop(t2, 56, 62, [0, 0, 0])
my_model.set_hop(t3, 56, 63, [0, 0, 0])
my_model.set_hop(t3, 57, 60, [0, 0, 0])
my_model.set_hop(t2, 57, 61, [0, 0, 0])
my_model.set_hop(t1, 57, 62, [0, 0, 0])
my_model.set_hop(t2, 57, 63, [0, 0, 0])
my_model.set_hop(t3, 57, 69, [0, 0, 0])
my_model.set_hop(t3, 58, 55, [0, 0, 1])
my_model.set_hop(t2, 58, 56, [0, 0, 1])
my_model.set_hop(t1, 58, 57, [0, 0, 1])
my_model.set_hop(t3, 58, 61, [0, 0, 1])
my_model.set_hop(t2, 58, 62, [0, 0, 1])
my_model.set_hop(t3, 58, 63, [0, 0, 1])
my_model.set_hop(t1, 58, 59, [0, 0, 0])
my_model.set_hop(t2, 58, 60, [0, 0, 0])
my_model.set_hop(t3, 58, 61, [0, 0, 0])
my_model.set_hop(t2, 58, 64, [0, 0, 0])
my_model.set_hop(t3, 58, 65, [0, 0, 0])
my_model.set_hop(t3, 58, 68, [0, 0, 0])
my_model.set_hop(t1, 59, 60, [0, 0, 0])
my_model.set_hop(t2, 59, 61, [0, 0, 0])
my_model.set_hop(t3, 59, 62, [0, 0, 0])
my_model.set_hop(t1, 59, 64, [0, 0, 0])
my_model.set_hop(t2, 59, 65, [0, 0, 0])
my_model.set_hop(t3, 59, 66, [0, 0, 0])
my_model.set_hop(t2, 59, 68, [0, 0, 0])
my_model.set_hop(t3, 59, 69, [0, 0, 0])
my_model.set_hop(t1, 60, 61, [0, 0, 0])
my_model.set_hop(t2, 60, 62, [0, 0, 0])
my_model.set_hop(t3, 60, 63, [0, 0, 0])
my_model.set_hop(t2, 60, 64, [0, 0, 0])
my_model.set_hop(t3, 60, 65, [0, 0, 0])
my_model.set_hop(t2, 60, 66, [0, 0, 0])
my_model.set_hop(t3, 60, 67, [0, 0, 0])
my_model.set_hop(t1, 60, 68, [0, 0, 0])
my_model.set_hop(t2, 60, 69, [0, 0, 0])
my_model.set_hop(t3, 60, 70, [0, 0, 0])
my_model.set_hop(t1, 61, 62, [0, 0, 0])
my_model.set_hop(t2, 61, 63, [0, 0, 0])
my_model.set_hop(t3, 61, 64, [0, 0, 0])
my_model.set_hop(t3, 61, 66, [0, 0, 0])
my_model.set_hop(t2, 61, 68, [0, 0, 0])
my_model.set_hop(t3, 61, 69, [0, 0, 0])
my_model.set_hop(t1, 62, 63, [0, 0, 0])
my_model.set_hop(t3, 62, 68, [0, 0, 0])
my_model.set_hop(t2, 62, 69, [0, 0, 0])
my_model.set_hop(t3, 62, 70, [0, 0, 0])
my_model.set_hop(t3, 63, 66, [0, 0, 0])
my_model.set_hop(t2, 63, 68, [0, 0, 0])
my_model.set_hop(t1, 63, 69, [0, 0, 0])
my_model.set_hop(t2, 63, 70, [0, 0, 0])
my_model.set_hop(t3, 63, 71, [0, 0, 0])
my_model.set_hop(t3, 63, 75, [0, 0, 0])
my_model.set_hop(t3, 64, 57, [0, 0, 1])
my_model.set_hop(t3, 64, 61, [0, 0, 1])
my_model.set_hop(t2, 64, 62, [0, 0, 1])
my_model.set_hop(t1, 64, 63, [0, 0, 1])
my_model.set_hop(t3, 64, 68, [0, 0, 1])
my_model.set_hop(t2, 64, 69, [0, 0, 1])
my_model.set_hop(t3, 64, 70, [0, 0, 1])
my_model.set_hop(t2, 64, 71, [0, 0, 1])
my_model.set_hop(t1, 64, 65, [0, 0, 0])
my_model.set_hop(t2, 64, 66, [0, 0, 0])
my_model.set_hop(t3, 64, 67, [0, 0, 0])
my_model.set_hop(t3, 64, 68, [0, 0, 0])
my_model.set_hop(t3, 64, 72, [0, 0, 0])
my_model.set_hop(t3, 65, 62, [0, 0, 1])
my_model.set_hop(t2, 65, 63, [0, 0, 1])
my_model.set_hop(t3, 65, 69, [0, 0, 1])
my_model.set_hop(t2, 65, 70, [0, 0, 1])
my_model.set_hop(t1, 65, 71, [0, 0, 1])
my_model.set_hop(t3, 65, 75, [0, 0, 1])
my_model.set_hop(t3, 65, 77, [0, 0, 1])
my_model.set_hop(t1, 65, 66, [0, 0, 0])
my_model.set_hop(t2, 65, 67, [0, 0, 0])
my_model.set_hop(t2, 65, 68, [0, 0, 0])
my_model.set_hop(t3, 65, 69, [0, 0, 0])
my_model.set_hop(t2, 65, 72, [0, 0, 0])
my_model.set_hop(t3, 65, 73, [0, 0, 0])
my_model.set_hop(t3, 65, 75, [0, 0, 0])
my_model.set_hop(t1, 66, 67, [0, 0, 0])
my_model.set_hop(t1, 66, 68, [0, 0, 0])
my_model.set_hop(t2, 66, 69, [0, 0, 0])
my_model.set_hop(t3, 66, 70, [0, 0, 0])
my_model.set_hop(t3, 66, 72, [0, 0, 0])
my_model.set_hop(t2, 66, 73, [0, 0, 0])
my_model.set_hop(t3, 66, 74, [0, 0, 0])
my_model.set_hop(t2, 66, 75, [0, 0, 0])
my_model.set_hop(t3, 66, 76, [0, 0, 0])
my_model.set_hop(t2, 67, 68, [0, 0, 0])
my_model.set_hop(t3, 67, 69, [0, 0, 0])
my_model.set_hop(t2, 67, 70, [0, 0, 0])
my_model.set_hop(t3, 67, 71, [0, 0, 0])
my_model.set_hop(t2, 67, 72, [0, 0, 0])
my_model.set_hop(t1, 67, 73, [0, 0, 0])
my_model.set_hop(t2, 67, 74, [0, 0, 0])
my_model.set_hop(t1, 67, 75, [0, 0, 0])
my_model.set_hop(t2, 67, 76, [0, 0, 0])
my_model.set_hop(t3, 67, 77, [0, 0, 0])
my_model.set_hop(t3, 67, 79, [0, 0, 0])
my_model.set_hop(t3, 67, 81, [0, 0, 0])
my_model.set_hop(t1, 68, 69, [0, 0, 0])
my_model.set_hop(t2, 68, 70, [0, 0, 0])
my_model.set_hop(t3, 68, 71, [0, 0, 0])
my_model.set_hop(t3, 68, 73, [0, 0, 0])
my_model.set_hop(t3, 68, 75, [0, 0, 0])
my_model.set_hop(t1, 69, 70, [0, 0, 0])
my_model.set_hop(t2, 69, 71, [0, 0, 0])
my_model.set_hop(t2, 69, 75, [0, 0, 0])
my_model.set_hop(t3, 69, 76, [0, 0, 0])
my_model.set_hop(t1, 70, 71, [0, 0, 0])
my_model.set_hop(t3, 70, 73, [0, 0, 0])
my_model.set_hop(t1, 70, 75, [0, 0, 0])
my_model.set_hop(t2, 70, 76, [0, 0, 0])
my_model.set_hop(t3, 70, 77, [0, 0, 0])
my_model.set_hop(t3, 70, 81, [0, 0, 0])
my_model.set_hop(t2, 71, 75, [0, 0, 0])
my_model.set_hop(t3, 71, 76, [0, 0, 0])
my_model.set_hop(t2, 71, 77, [0, 0, 0])
my_model.set_hop(t3, 72, 69, [0, 0, 1])
my_model.set_hop(t2, 72, 70, [0, 0, 1])
my_model.set_hop(t1, 72, 71, [0, 0, 1])
my_model.set_hop(t3, 72, 75, [0, 0, 1])
my_model.set_hop(t2, 72, 76, [0, 0, 1])
my_model.set_hop(t1, 72, 77, [0, 0, 1])
my_model.set_hop(t3, 72, 81, [0, 0, 1])
my_model.set_hop(t3, 72, 83, [0, 0, 1])
my_model.set_hop(t1, 72, 73, [0, 0, 0])
my_model.set_hop(t2, 72, 74, [0, 0, 0])
my_model.set_hop(t3, 72, 75, [0, 0, 0])
my_model.set_hop(t2, 72, 78, [0, 0, 0])
my_model.set_hop(t3, 72, 79, [0, 0, 0])
my_model.set_hop(t3, 72, 81, [0, 0, 0])
my_model.set_hop(t1, 73, 74, [0, 0, 0])
my_model.set_hop(t2, 73, 75, [0, 0, 0])
my_model.set_hop(t3, 73, 76, [0, 0, 0])
my_model.set_hop(t3, 73, 78, [0, 0, 0])
my_model.set_hop(t2, 73, 79, [0, 0, 0])
my_model.set_hop(t3, 73, 80, [0, 0, 0])
my_model.set_hop(t2, 73, 81, [0, 0, 0])
my_model.set_hop(t3, 73, 82, [0, 0, 0])
my_model.set_hop(t3, 74, 75, [0, 0, 0])
my_model.set_hop(t2, 74, 76, [0, 0, 0])
my_model.set_hop(t3, 74, 77, [0, 0, 0])
my_model.set_hop(t2, 74, 78, [0, 0, 0])
my_model.set_hop(t1, 74, 79, [0, 0, 0])
my_model.set_hop(t2, 74, 80, [0, 0, 0])
my_model.set_hop(t1, 74, 81, [0, 0, 0])
my_model.set_hop(t2, 74, 82, [0, 0, 0])
my_model.set_hop(t3, 74, 83, [0, 0, 0])
my_model.set_hop(t1, 75, 76, [0, 0, 0])
my_model.set_hop(t2, 75, 77, [0, 0, 0])
my_model.set_hop(t2, 75, 81, [0, 0, 0])
my_model.set_hop(t3, 75, 82, [0, 0, 0])
my_model.set_hop(t1, 76, 77, [0, 0, 0])
my_model.set_hop(t3, 76, 79, [0, 0, 0])
my_model.set_hop(t1, 76, 81, [0, 0, 0])
my_model.set_hop(t2, 76, 82, [0, 0, 0])
my_model.set_hop(t3, 76, 83, [0, 0, 0])
my_model.set_hop(t2, 77, 81, [0, 0, 0])
my_model.set_hop(t3, 77, 82, [0, 0, 0])
my_model.set_hop(t2, 77, 83, [0, 0, 0])
my_model.set_hop(t3, 78, 0, [0, 0, 1])
my_model.set_hop(t2, 78, 1, [0, 0, 1])
my_model.set_hop(t3, 78, 6, [0, 0, 1])
my_model.set_hop(t3, 78, 71, [0, 0, 1])
my_model.set_hop(t3, 78, 75, [0, 0, 1])
my_model.set_hop(t2, 78, 76, [0, 0, 1])
my_model.set_hop(t1, 78, 77, [0, 0, 1])
my_model.set_hop(t3, 78, 81, [0, 0, 1])
my_model.set_hop(t2, 78, 82, [0, 0, 1])
my_model.set_hop(t1, 78, 83, [0, 0, 1])
my_model.set_hop(t1, 78, 79, [0, 0, 0])
my_model.set_hop(t2, 78, 80, [0, 0, 0])
my_model.set_hop(t3, 78, 81, [0, 0, 0])
my_model.set_hop(t1, 79, 80, [0, 0, 0])
my_model.set_hop(t2, 79, 81, [0, 0, 0])
my_model.set_hop(t3, 79, 82, [0, 0, 0])
my_model.set_hop(t3, 80, 81, [0, 0, 0])
my_model.set_hop(t2, 80, 82, [0, 0, 0])
my_model.set_hop(t3, 80, 83, [0, 0, 0])
my_model.set_hop(t1, 81, 82, [0, 0, 0])
my_model.set_hop(t2, 81, 83, [0, 0, 0])
my_model.set_hop(t1, 82, 83, [0, 0, 0])

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

ax.set_title('12-3 band structure')
ax.set_xlabel('Path in k-space')
ax.set_ylabel('Band energy')

for xband in range(84):
	ax.plot(k_dist, evals[xband], linewidth=.5, color='black')

# fig.tight_layout()
fig.savefig('12-3.eps')

print('Done.')