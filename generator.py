# A function having yeild keyword instead of using return keyword is called generator function
# When we call the generator function it will return one object is called generator object

# Normal Function
'''def fun():
    return 1
    return 2
    return 3
nor_fun=fun()
print(nor_fun) #1
nor_fun2=fun()
print(nor_fun2) #1
nor_fun3=fun()
print(nor_fun3) #1'''

# genarator function
'''def fun():
    yield 1
    yield 2
    yield 3
gen_fun1=fun()
print(gen_fun1) #<generator object fun at 0x0000021641808A90>
print(next(gen_fun1)) #1
print(next(gen_fun1)) #2
print(next(gen_fun1)) #3
print(next(gen_fun1)) #StopIteration'''

# Generationg employee id
'''def emp_id(company_code):
    val=1
    while True:
        yield company_code+str(val)
        val+=1
e1=emp_id('TYP')
print(e1)
print(next(e1)) #TYP1
print(next(e1)) #TYP2
print(next(e1)) #TYP3
print(next(e1)) #TYP4'''

# Fibonacy no using generator
def fun(n):
    a,b=0,1
    while a<5:
        yield a
        a,b=b,a+b
fib1=fun(5)
print(fib1)
print(next(fib1)) #0
print(next(fib1)) #1
print(next(fib1)) #1
print(next(fib1)) #2
print(next(fib1)) #3
print(next(fib1)) #StopIteration
    




