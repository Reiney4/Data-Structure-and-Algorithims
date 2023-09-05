"""
--------------------------- Question 1 ----------------------

 Implement a function is_balanced(expression) that takes a string 
containing parentheses, curly braces, and square brackets,and determines whether 
the expression is balanced. 

An expression is considered balanced if each opening bracket has a corresponding closing 
bracket in the correct order.

sample input = 

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False """


def is_balanced(brackets):
    stack = []
    open_brackets = "([{"
    close_brackets = []

    for b in brackets:
        if b in open_brackets:
            stack.append(b)
            print(stack)
        if b not in open_brackets:
            # check if stack is empty
            close_brackets.append(b)
            if len(stack) > 0:
                if (
                    stack[-1] == "("
                    and b == ")"
                    or stack[-1] == "["
                    and b == "]"
                    or stack[-1] == "{"
                    and b == "}"
                ):
                    poped = stack.pop()
                    close_brackets.pop()
                else:
                    return False

    return True if len(stack) == 0 and len(close_brackets) == 0 else False


s = "([]{})"
print(is_balanced(s))


# def is_balanced(brackets):
#     stack = []
#     open_brackets = {"(": ")", "{": "}", "[": "]"}

#     for char in open_brackets:
#         if char in open_brackets:
#             stack.append(char)
#         elif char not in open_brackets:
#             #  check if the stack is empty

#             print("==", char)
#         else:
#             return False

"""    # return len(stack) == 0

#receive the input 
# create an empty stack -- stack []
#loop thru the string 
# see if the bracket exist in the open_brackets
        # if yess 
            #append it to stack 
        # if no 
        #  check the last element of the stack
        
        """


# s = "([]{})"
# print(is_balanced(s))