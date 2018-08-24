# tuples
name=("umang","mca","18/08/1996")
print(name)
print(name[0])
#name[0]="hina" # gives error beecoz it is immutable
print(len(name))



#argument packing and unpacking
t=1234,4567,'heelo'
print(t)
print(type(t))


x,y,z=t
print(x)
print(y)

#tupple packing
x=10
y=9
x=x^y
y=x^y
x=x^y
print(x,y)

