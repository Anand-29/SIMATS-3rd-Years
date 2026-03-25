#create a set
s1={10,20,30,40}
print(s1)
#add data to set:
s1.add(50)
print(s1)
#remove data from set:
s1.remove(20)
print(s1)
#find union of 2 sets:
s2={30,40,50,60}
print(s1.union(s2))
#find intersection:
print(s1.intersection(s2))
#find difference:
print(s1.difference(s2))
#find symmetric difference:
print(s1.symmetric_difference(s2))
#find subset:
subset={10,20}
print(subset<={10,20,30,40})
print(subset.issubset({20,30,40}))
#remove duplicate form list:
print(set([10,10,20,20,]))
#convert set to list:
print(list(s1))
