#kisi bhi collection ko freez krne k liye ise use krte hai 
fset1= frozenset({'monkey','10,20','tanisha'})
fset2= frozenset({'tanisha','10,20','monkey'})
print(id(fset1),id(fset2))             #True       

#frozenset is immutable                             