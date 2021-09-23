stringA = 'abc'
stringB = 'abcde'

print(stringA <= stringB)
print(len(stringB))

print(stringA == stringB[:-2])

stringC = 'abcdefghijkl'
print(stringC[::])
print(stringC[::2])

#stringA[0] = 'A' --> this leads to an error
print(id(stringA))


print('\nidentity example')
#identity example with a float
f = 7
print(id(f))
f = 8
print(id(f))

d1 =  'data'
print(id(d1))
d1 += ' science'
print(id(d1))

print(d1)

l1 = [1,2,3]
print(id(d1))
l1 += [4,5,6]
print(id(d1))
print (l1)


l2 = [1,2,3]
l3 = l2

l3 += [4,5]
print(l2)
print(l3)

print(id(l2))
print(id(l3))

#immutable objects

print('\nimmutable objects:')
s1 = 'this '
s2 = s1

print(s2 is s1)
print(id(s1))
print(id(s2))

s1 += 'is Python'

print('\nafter change')
print(s1)
print(s2)
print(s2 is s1)
print(id(s1))
print(id(s2))


#changing values in containers

print('\ncontainer example')
data = [1,2,3,4,5]
tup = ('someString', data)

print(data)
print(id(tup))

data[3] = 'change'

print(data)
print(id(tup))

#special case - updating values of immutable objects in an immutable container

print('\nspecial case\n')
str1 = 'myString'
int1 = 25
tup1 = ('a','b','c')
tup2 = (str1, int1, tup1)

print('id str1:' + str(id(str1)))
print('id int1:' + str(id(int1)))
print('id tup1:' + str(id(tup1)))
print(tup2)
print('id tup2:' + str(id(tup2)))


str1 += ' has changed'
int1 = 500
tup1 += ('d', 'e')

print('\nafter change:\n')

print('id str1:' + str(id(str1)))
print('id int1:' + str(id(int1)))
print('id tup1:' + str(id(tup1)))
print(tup2)
print('id tup2:' + str(id(tup2)))
