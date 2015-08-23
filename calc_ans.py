x = float(raw_input())
op = raw_input()
y = float(raw_input())

n = 0
if op == '+':
    n = x + y
elif op == '-':
    n = x - y
elif op == '*':
    n = x * y
elif op == '/':
    n = x / y
print(n)
