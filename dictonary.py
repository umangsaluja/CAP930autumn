empty={}
type(empty)
empty==dict()


a=dict(one=1, two=2, three=3)
print(a)
b={"one":1,"two":2}
print(b)
print(a==b)



myself={"name":"umang","surname":"saluja","archievement":"got university position"}
print(myself)
print(myself['name'])
# raises key error
# print(myself['fathername'])


#how uh know dictornary is mutable to check there is new add items and update value 
myself['name']="umu"
myself['strenght']="good listener"
print(myself)



#dict using list
d={"cs":[106,107,110],"math":[90,30]}
print(d)
# raises key error print(d["eng"])


#using get
print(d.get("cs"))
print(d.get("math"))
print(d.get("eng")) # get method doesnot give key error


d.get("eng",[12,45])
print(d.get("eng"))


#DELETE
del d["math"]
print(d)

myself.pop("strenght")
print(myself)
d.popitem()
print(d)

#keys
print(myself.keys())
print(myself.values())
print(myself.items())



for value in myself.items():
      print(value)


