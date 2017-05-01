"""
    __author__ = Prosunjit Biswas
    __email__ = prosun.csedu@gmail.com
    __date__ = 04/30/2017
    Experimenting with python regular expression.
    named camturing  group (syntax (?P<name>...)) is used here.


"""
import re

def replacefun(mob):
    """
    :param mob (match object)
    :return evaluate an expression and return the evaluated value
    : if operator: + , operator1: 10, operator2: 20, returns 30 == (10 + 20)
    """
    mobDict = mob.groupdict()
    if mobDict.has_key('operator') and mob.group('operator') == "+":
        s =  int ( mob.group("operand1") ) + int ( mob.group("operand2") )
        return str(s)
    elif mobDict.has_key('operator') and mob.group('operator') == "-":
         s = int ( mob.group("operand1") ) - int ( mob.group("operand2") )
         return str(s)
    elif mobDict.has_key('single_num'):
        return mob.group('single_num')

def calc(input):
    """
    :param input (string) - string containing '(', ')', "+", "-" and numbers
    :return: evaluted expression.
    """
    input = "(" + input + ")"
    while  True:
        # find patterns like 'x+y or x-y and return evaluated value of 'x+y'/'x-y'
        result1 = re.sub(r'(?P<operand1>[-]?\d+)(?P<operator>[+]|[-])(?P<operand2>[-]?\d+)', replacefun, input)
        # find pattern like (x) and return x
        result2 = re.sub(r'[(](?P<single_num>([-]?\d+))[)]', replacefun, result1)
        if result2 == input:
            return result2
        input = result2
    return input

assert int(calc("2-(5-6)")) == 3
assert int(calc("(1+(4+5+2)-3)+(6+8)")) == 23
