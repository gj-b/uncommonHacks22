# source: https://isquared.digital/visualizations/2020-06-26-julia-set/

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

def julia_quadratic(zx, zy, cx, cy, threshold):
    """Calculates whether the number z[0] = zx + i*zy with a constant c = x + i*y belongs
    to the Julia set. In order to belong, the sequence z[n + 1] = z[n]**2 + c, 
    must not diverge after 'threshold' number of steps. The sequence diverges
    if the absolute value of z[n+1] is greater than 4.
    
    :param float zx: the x component of z[0]
    :param float zy: the y component of z[0]
    :param float cx: the x component of the constant c
    :param float cy: the y component of the constant c
    :param int threshold: the number of iterations to considered it converged
    """
    # initial conditions
    z = complex(zx, zy)
    c = complex(cx, cy)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  # it diverged
            return i
        
    return threshold - 1  # it didn't diverge

x_start, y_start = -2, -2  # an interesting region starts here
width, height = 4, 4  # for 3 units to the left and to the right
density_per_unit = 200  # how many pixles per unit

re = np.linspace(x_start, x_start + width, width * density_per_unit )  # real axis
im = np.linspace(y_start, y_start + height, height * density_per_unit)  # imaginary axis

X = np.empty((len(re), len(im)))  # the initial array-like image

threshold = 20  # max allowed iterations

# we represent c as c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
r = 0.7885
a = 2 * np.pi / 4.
cx, cy = r * np.cos(a), r * np.sin(a)

# fill-in the image with the number of interations
for i in range(len(re)):
    for j in range(len(im)):
        X[i, j] = julia_quadratic(zx=re[i], zy=im[j], cx=cx, cy=cy, threshold=threshold)

fig = plt.figure(figsize=(10, 10))

# formatting options: remove ticks
ax = plt.axes()
ax.set_xticks([], [])
ax.set_yticks([], [])

ax.imshow(X.T, interpolation="hanning", cmap='magma')
plt.gcf().text(0.15, 0.1, 'by Vladimir Ilievski', fontsize=18, fontfamily='Verdana')
plt.savefig('julia_Set.png', dpi=300, bbox_inches='tight')