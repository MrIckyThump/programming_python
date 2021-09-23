import sys

s1 = 'Python is a programming language and an animal'

s2 = "this is a snake and it is " + str(5) + " metres long"

s3 = 'that is a ' + 'very '*3 + 'long animal'

print (s1)
print (s2)
print (s3)

s4 = 'This'
s5 = 'This'
s6 = 'this'

print(s4 == s5)
print(s4 == s6)
print(s4 is s5)
print(s4 is s4)


a = [1,2,3,4,5]
b = a
print('b is a? ' + str(b is a))
print('b is a? ' + str(b == a))

b = a[:]
print('b is a? ' + str(b is a))
print('b is a? ' + str(b == a))

#Python caches small integer and string objects, therefore is sometimes holds true for small values
#cf. slides
print('caching example:')
print(10000 == 10**4)
print(10000 is 10**4)

print('a' is 'a')
print('aa' is 'a'*2)
x = 'a'
print('aa' is x * 2)
print('aa' is sys.intern(x * 2))


#isinstance(s1, str)
#if type(s1) == str

#print ( 'The data file is ' + 5 + ' MB large') -- produces error
print ( 'The data file is ' + str(5) + ' MB large')


print ( '\nresult of intern experiment:')
stringA = sys.intern('myString'*1000)
stringB = sys.intern('myString'*1000)

print(stringA is stringB)

stringC = 'myNewString'*1000
stringD = 'myNewString'*1000

print(stringD is stringC)


#user_input = input("Enter a message... ")
#print('User entered: ' + user_input)