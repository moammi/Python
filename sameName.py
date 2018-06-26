Python 3.6.5 (default, Mar 29 2018, 18:20:46) 
[GCC 8.0.1 20180317 (Red Hat 8.0.1-0.19)] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
======================== RESTART: /home/ammi/test.py ========================
HelloWorld
>>> print('cats','dogs','mice')
cats dogs mice
>>> sep?
SyntaxError: invalid syntax
>>> sep
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sep
NameError: name 'sep' is not defined
>>> print('cats','dogs','mice', sep=',
	  
SyntaxError: EOL while scanning string literal
>>> print('cats','dogs','mice', sep=','_)
	  
SyntaxError: invalid syntax
>>> print('cats','dogs','mice', sep=',')
	  
cats,dogs,mice
>>> print('cats','dogs','mice', sep='....')
	  
cats....dogs....mice
>>> 
======================== RESTART: /home/ammi/test.py ========================
>>> 
======================== RESTART: /home/ammi/test.py ========================
Traceback (most recent call last):
  File "/home/ammi/test.py", line 4, in <module>
    print(eggs)
NameError: name 'eggs' is not defined
>>> 
======================== RESTART: /home/ammi/test.py ========================
>>> 
======================== RESTART: /home/ammi/test.py ========================
>>> 
======================== RESTART: /home/ammi/test.py ========================
99
>>> 
======================== RESTART: /home/ammi/test.py ========================
0
99
>>> 
======================== RESTART: /home/ammi/test.py ========================
<function spam at 0x7fc8e9de3c80>
0
99
>>> 
	  
>>> 
======================== RESTART: /home/ammi/test.py ========================
42
42
>>> 
======================== RESTART: /home/ammi/test.py ========================
42
42

>>> 
======================== RESTART: /home/ammi/test.py ========================
bacon local
spam local
bacon local
global
>>> 
