numbers={23,34,2}
name={'firstname','lastname'}
print(name)
print(type(name))
print(numbers)


empty_Set=set()
set_from_list=set([1,2,34,5])


basket={"apple","orange","banana"}
print(len(basket))
basket.add("grapes")
basket.remove("apple")#raises keyerror if "elements" is not present
basket.discard("apple")# same as remove ,except no error
print(basket)
basket.discard("mango")
basket.pop()
print(basket)
basket.clear()
print(basket)



a=set("abcadefghijk")
b=set("alacazam")
print(a)
print(b)


diff=a-b
print(diff)

union=a|b
print(union)

intersection=a&b
print(intersection)

symmetric_difference=a^b   #(a-b)union(b-a)
print(symmetric_difference)


