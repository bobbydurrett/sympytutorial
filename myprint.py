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

"""

def write_tex_file(tex_file, text_string):
   """
   Writes one line to tex_file and 
   closes file
   """
   file_handle = open(tex_file, 'a')
   file_handle.write(text_string+"\n")
   file_handle.close()   

def startl(tex_file):
   """
   Writes header information
   to file_name_no_type.tex
   Clear existing file
   """
   
   file_handle = open(tex_file, 'w')
   file_handle.close()   
      
   write_tex_file(tex_file,"\\documentclass{article}")
   write_tex_file(tex_file,"\\usepackage{amsfonts}")
   write_tex_file(tex_file,"\\begin{document}")
   
def addlt(tex_file, text_string):
    """
    Writes some text
    skipping a big line.
    """  
    
    write_tex_file(tex_file,text_string)
    write_tex_file(tex_file," ")
    write_tex_file(tex_file,"\\bigskip")
    
def addlm(tex_file, sympy_object):
    """
    Converts sympy object to latex
    and writes to tex file
    """
    
    addlt(tex_file,"$"+latex(sympy_object)+"$")

    
def endl(tex_file):
    """
    Finishes writing to tex file and 
    converts to pdf
    """
    
    write_tex_file(tex_file,"\\end{document}")
        
    run(["pdflatex", tex_file])

def onel(tex_file, sympy_object):
    """
    Writes one sympy object
    converts to latex then
    pdf
    """
    startl(tex_file)
    addlt(tex_file, str(sympy_object))
    addlm(tex_file, sympy_object)
    endl(tex_file)

if __name__ == "__main__":

    init_printing(use_unicode=False)

    x = symbols('x')

    spprint(Integral(cos(x)**2, (x, 0, pi)))

    onel("myprint.tex",Integral(cos(x)**2, (x, 0, pi)))
    
