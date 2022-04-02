# Source: https://github.com/sepandhaghighi/samila#usage

import matplotlib.pyplot as plt
from samila import GenerativeImage, Projection

import random 
import math 

def f1(x, y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
def f2(x, y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

def simpleGeneration(): 
    g = GenerativeImage(f1, f2)
    g.generate()
    g.plot()

    plt.savefig('simple' + str(random.randint(0, 1000)) + '.png')

def polarGeneration(): 
    g = GenerativeImage(f1, f2)
    g.generate()
    g.plot(color='red', bgcolor='black', projection=Projection.POLAR)
    plt.savefig('polar' + str(random.randint(0, 1000)) + '.png')

def rangeGeneration():
    g = GenerativeImage(f1, f2)
    g.generate(start=-2*math.pi, step=0.01, stop=10)
    g.plot()
    plt.savefig('range' + str(random.randint(0, 1000)) + '.png')
