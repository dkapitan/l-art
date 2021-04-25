"""
Pythonic implementation of L-system with recursion.
https://en.wikipedia.org/wiki/L-system
alphabet:
    variables: A, B
    constants: none
axiom: A
rules: A —> AB
       B —> A
       
Ultimately we want to have context-aware parametric stochastic grammar.

Links:
  - [Understanding recursion with Python](https://understanding-recursion.readthedocs.io/en/latest/16%20L-System%20Solution.html)
  - [Wikipedia:L-system](https://en.wikipedia.org/wiki/L-system)
"""


def lSysGenerate(axiom, order):
    if order == 0:
        return axiom
    else:
        return lSysCompute(lSysGenerate(axiom, order - 1))

def lSysCompute(s):
    d = {'A': 'AB', 'B': 'A'}
    sequence.append(''.join([d.get(c) or c for c in s]))
    return sequence[-1]

axiom = 'A'
sequence = [axiom]
order = 4
lSysGenerate(axiom, order)
print(sequence)
