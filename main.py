#!/usr/bin/python
import validator
import RPN


def solve(expression):
    result = RPN.run(validator.split_expression(validator.refactor(expression)))
    print(result)


def main():
    while 1:
        expression = input("EXPRESSION: ")
        solve(expression)


if '__main__' == __name__:
    main()
