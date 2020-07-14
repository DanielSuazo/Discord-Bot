
def test():
  return "killme"

def test2():
  return "killme2"

switch = {
  0: test,
  1: test2
}

def fun(i):
  fun = switch.get(i, "index out of bounds")

  return fun()

print(fun(0))