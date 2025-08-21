import numpy as np
a= np.array([1,2,3])
b= np.array([4,5,6])
print(a+b)

a= np.array([40,50,"60"])
print(a)

# slicing
a= np.array([[1,2,3,4],[5,6,7,8]])
print(a[0:4,0:4])

a= np.array([[1,2,3,4],[5,6,7,8]])
print(a[0,2:4])

a= np.array([[1,2,3,4],[5,6,7,8]])
print(a[1,1:4])

a= np.array([[1,2,3,4],[5,6,7,8],[9,10,22,11]])
print(a[2,2])

#functions
a= np.array([[1,2,3,4],[5,6,7,8],[9,10,22,11]])
print(np.shape(a))
print(np.size(a))
print(np.ndim(a))
print(a.dtype)

a=np.array([1,2,3,4,5,6])
s=np.array(a)
print(s.size)
print(len(a))
print(type(a))
print(s.dtype)
print(s.astype(float))
print(s.astype(str))
# mathematical operation and function
a= np.array([11,22,3,33,44])
b= np.array([55,66,77,8,99])
print(a+b)

a= np.array([11,22,3,33,44])
b= np.array([55,66,77,8,99])
print(np.add(a,b))

a= np.array([11,22,3,33,44])
b= np.array([55,66,77,8,99])
print(np.subtract(a,b))
print(a-b)


a= np.array([11,22,3,33,44])
b= np.array([55,66,77,8,99])
print(np.multiply(a,b))
print(a*b)


a= np.array([11,22,3,33,44])
b= np.array([55,66,77,8,99])
print(np.divide(a,b))
print(a/b)



a= np.array([11,22,3,33,44])
b= np.array([2])
print(np.power(a,b))

a= np.array([121 , 484  ,  9, 1089, 1936])
print(np.sqrt(a))

#concatenate
a= np.array([11,22,3,33,44])
b= np.array([55,66,77,8,99])
print(np.concatenate([a,b]))

a= np.array([11,22,3,33,44])
b= np.array_split(a,3)
print(b)

# adding and removing element in array 
a= np.array([11,22,3,33,44])
print(np.append(a,[34]))
print(np.insert(a,1,[99]))
print(np.delete(a,1))

# numpy sort filter and search
a= np.array([76,89,11,22,3,33,44])
print(np.sort(a))

a= np.array([[11,22,3,33,44],[55,56,78,65,34]])
print(np.sort(a))

a= np.array([11,22,3,33,44])
s= np.where(a%2==0)
print(s)

a= np.array([11,22,3,33,44])
s= a>25
new=a[s]
print(new)

# Aggregating function in numpy
a= np.array([11,22,3,33,44])
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print(np.size(a))
print(np.cumsum(a))
print(np.mean(a))
print(np.cumprod(a))

a= np.array([11,22,3,33,44])
b= np.array([6,7,8,9,0])
print(a,b)
print(np.sum([a,b],axis=1))

# # statistical function
# import numpy as np
# import statistics as stats
# a= np.array([11,22,3,33,44])
# print(np.mean(a))
# print(np.median(a))
# print(np.mode(a))