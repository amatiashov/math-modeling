import numpy
from methods import *
import EasyTables


def ctan(x):
    return 1 / numpy.tan(x)

dichotomy = dichotomy_solver(ctan, 1, 2)
chord = chord_method(ctan, 1, 2)

table = EasyTables.EasyTables(['Method name', 'Function','Result', 'Number of iterations'])

table.add_row(['Dichotomy method', 'ctan',dichotomy[0], dichotomy[1]])
table.add_row(['Chord method', 'ctan', chord[0], chord[1]])

table.display()