Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='hello bob'
>>> try:
...     i=int(a)
... except:
...     i=-1
... print('first')
SyntaxError: invalid syntax
>>> print('first',i)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('first',i)
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> astr='hello bob')
SyntaxError: unmatched ')'
>>> astr='hello bob'
>>> try:
...     istr=int(astr)
... except:
...     istr=-1
... print('first',istr)
SyntaxError: invalid syntax
>>> try:
...     istr=int(astr)
... except:
...     istr=-1
... print('first',istr)
SyntaxError: invalid syntax
