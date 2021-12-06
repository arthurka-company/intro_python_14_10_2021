
def foo(per=None):
    if per is None:
        per = []
    per.append(1)
    print(per)


print('1')
foo()

print('2')
foo()

print('3')
foo([34])

print('4')
foo()