#kisi bhi collection ko freez krne k liye ise use krte hai 
# fset1= frozenset({'monkey','10,20','tanisha'})
# fset2= frozenset({'tanisha','10,20','monkey'})
# print(id(fset1),id(fset2))             #True       

#frozenset is immutable  
# collection of uniqe elemnt 
# frees any collection (list,set,tuple,string)
# not indexing support 
# not slicing support 
#unorderd

#_______________ methods_________________________
# s='tanisha'
# fs=frozenset(s)
# print(fs)
# print(type(fs))

# s={10,20,30,40,50}
# l={2,4,8,30,4,20}
# x=frozenset(s)
# y=frozenset(l)
# print(x.union(y))
# print(y.intersection(x))
# print(x.difference(y))

# s1='tanisha'
# s2='bamne'
# x=frozenset(s1)
# print(x)
# y=frozenset(s2)
# print(y)

x={1,2,3,4,5,6}
y={1,2,3,4,6,7,8,0}
print(y.issuperset(x))
print(x.issubset(y))
