from sympy import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.usetex'] = True

def lprint(sympy_objects):
    """
    Print the passed Sympy object using LaTex in Matplotlib.
    """
    txte = "$"+latex(sympy_objects)+"$"
    
    plt.figure("LaTex Output",(16,2),100)
    plt.text(-.1, 0.4, txte, fontsize=30)
    ax = plt.gca()
    ax.axis('off')
    plt.show()

def spprint(o):
    pprint(o)
    print(' ')

if __name__ == "__main__":

    x = symbols('x')

    lprint(Integral(cos(x)**2, (x, 0, pi)))

