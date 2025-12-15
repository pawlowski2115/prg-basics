import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   stack = queue.LifoQueue()
   bracket_pairs = {
      ")":"(",
      "}":"{",
      "]":"["
   }
   opening_bracket = set(bracket_pairs.values())

   for char in expression:
      if char in opening_bracket


   return #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print(...)
else
   ...

if brackets_ok(expression2):
...
...