from sympy import *
import matplotlib.pyplot as plt
from subprocess import run

def spprint(o):
    pprint(o)
    print(' ')
    
"""
Code to write a latex file and generate a pdf

startl - creates .tex file with header

addlm - converts one sympy object to latex and writes to file
        between $$ $$
          
addlt - adds plain text line for a comment
               
endl - writes rest of .tex file and converts to .pdf and opens

onel - calls startl, addlm, endl for one sympy object

global variable myprint.tex_file

"""

tex_file = ""

def write_tex_file(text_string):
   """
   Writes one line to tex_file and 
   closes file
   """
   file_handle = open(tex_file, 'a')
   file_handle.write(text_string+"\n")
   file_handle.close()   

def startl():
   """
   Writes header information
   to file_name_no_type.tex
   Clear existing file
   """
   
   file_handle = open(tex_file, 'w')
   file_handle.close()   
      
   write_tex_file("\\documentclass{article}")
   write_tex_file("\\usepackage{amsfonts}")
   write_tex_file("\\begin{document}")
   
def addlt(text_string):
    """
    Writes some text
    skipping a big line.
    """  
    
    write_tex_file(text_string)
    write_tex_file(" ")
    write_tex_file("\\bigskip")
    
def addlm(sympy_object):
    """
    Converts sympy object to latex
    and writes to tex file
    """
    
    addlt("$"+latex(sympy_object)+"$")

    
def endl():
    """
    Finishes writing to tex file and 
    converts to pdf
    """
    
    write_tex_file("\\end{document}")
        
    run(["pdflatex", tex_file])

def onel(sympy_object):
    """
    Writes one sympy object
    converts to latex then
    pdf
    """
    startl()
    addlt(str(sympy_object))
    addlm(sympy_object)
    endl()

if __name__ == "__main__":

    init_printing(use_unicode=False)

    x = symbols('x')

    spprint(Integral(cos(x)**2, (x, 0, pi)))
    
    tex_file = "myprint.tex"

    onel(Integral(cos(x)**2, (x, 0, pi)))
    
