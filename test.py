
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

list_switch = [test(), test2()]

print(list_switch[1])