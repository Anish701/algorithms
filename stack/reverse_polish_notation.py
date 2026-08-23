from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(t)
                continue
            
            second = int(stack.pop())
            first = int(stack.pop())

            if t == '+':
                stack.append(first + second)
            elif t == '-':
                stack.append(first - second)
            elif t == '*':
                stack.append(first * second)
            elif t == '/':
                stack.append(first / second)
            
        return int(stack.pop())