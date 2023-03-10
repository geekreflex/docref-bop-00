def cheeseshop(kind, *arguments, **keywords):
  print("-- Do you have any", kind, "?")
  print("-- I'm sorry, we're all out of", kind)
  for arg in arguments:
    print(arg)
  print("-" * 40)
  for kw in keywords:
    print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny sir.", "It's really very, VERY runny, sir.", shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")

def my_function():
  """Do nothing, but document it.
  
  No, really, it doesn't do anything.
  """
  pass

print(my_function.__doc__)

def f(ham:str, eggs:str="eggs") -> str:
  print("Annotations:", f.__annotations__)
  print("Arguments:", ham, eggs)
  return ham + ' and ' + eggs


print(f('spam'))