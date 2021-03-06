==========================
Python Arithmetics Library
==========================

Arithmetics is a Python library that allows adding, subtracting and multiplying **VERY** long numbers.

Python (like many programming languages) is bad at math. It can't represent very large numbers in the memory. It rounds up the decimal precision as if it doesn't matter. For instance, Python calculates ``4376531231238346534654738521343658334865834.8739879827913213`` times ``-123380950827290485196703213.8735298304756982704423`` as ``-5.399805846355196e+68``, which is only a sad approximation. According to Python, ``1 - 0.00000000000000001`` is still equal to ``1.0``, which is obviously wrong and can lead to serious bugs.

Arithmetics Library can add, subtract or multiply numbers AT ANY LENGTH with the exact precision. It doesn't suffer from integer overflow or floating point rounding problems because it takes numbers in string format. It can work with positive, negative and decimal numbers. Analytics Library can calculate the above multiplication precisely: ``-539980584635519517644606174820023097370977572779217236866897631496501.40991196066825563084376519821275241099``.

Setup
=====
Arithmetics Library is freely available on the Python Package Index PyPI at https://pypi.org/project/arithmetics ::

    pip install arithmetics

Usage
=====
``arithmetics.calculate(...)`` takes in 1 arithmetic operator (``+``, ``-``, or ``*``) and 2 numbers in string format, and returns the result as a string::

    from arithmetics import arithmetics

    arithmetics.calculate(arithmetics.OPERAND_ADD, '123', '-456.789')
    # returns '-333.789'
    arithmetics.calculate(arithmetics.OPERAND_SUBTRACT, '-1.0000000000000000000000000000000000001', '0.0000000000000000000000000000000000002')
    # returns '-0.9999999999999999999999999999999999999'
    arithmetics.calculate(arithmetics.OPERAND_MULTIPLY, '31352725584.2464', '-4389.999945479936')
    # returns '-137638463605489.0905724488802304'

You may need this library if...
===============================

* You do math with very large numbers (e.g. astrophysics)
* You don't want to lose decimal precision (e.g. financial applications)


Happy coding!

Ozan Eren Bilgen

* oebilgen@gmail.com
* http://linkedin.com/in/ozanerenbilgen/
