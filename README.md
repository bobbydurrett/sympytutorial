# sympytutorial
My Python scripts working through SymPy Tutorial

https://docs.sympy.org/latest/tutorial/index.html

Next section:

https://docs.sympy.org/latest/tutorial/solvers.html

Made myprint.py to output latex as matplotlib plot.
Also ascii pretty print with extra line.

Installed MiKTeX on Windows 10 laptop.

Had an Oracle Linux source intall of Python 3.8.1.

As root did this to get LaTex installed:

yum install texlive

yum install texlive*

second yum command was needed to get dvipng

Linux console c7.py unicode and LaTex works
but not in Putty or Windows console without
LaTex installed.

Got rid of lprint using matplotlib

Might rewrite to call latex command line utilities directly
and generate a pdf

Need to generate something like example2.tex and run the 
utility to make the pdf. Maybe some standard template.
I.e. write my own lprint that makes the pdf and then opens it.

Or forget all this and just print(latex(xxx)) and put in tex 
document myself.

pdflatex test.tex

then open test.pdf seems to work.

have to delete test.aux and test.log files

could do

startlatex - creates .tex file with header

addlatexline - converts one sympy object to latex and writes to file
               between $$ $$
               
finishlatex - writes rest of .tex file and converts to .pdf and opens

onelatexline - calls startlatex, addlatexline, finishlatex for one sympy 
               object
               
put this in myprint.py

or I could just print out the latex and edit manually.

