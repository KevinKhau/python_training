# Functional Python: Reducing Duplication with Higher-Order Functions

def make_adder(n):
  def adder(x):
    return x + n
  return adder

add_two = make_adder(2)
add_four = make_adder(4)

print(add_two(2)) #4
print(add_two(4)) #6
print(add_four(4)) #8

# Direct call
res = make_adder(3)(9)
print(res) #12
