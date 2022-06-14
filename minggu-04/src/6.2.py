>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')