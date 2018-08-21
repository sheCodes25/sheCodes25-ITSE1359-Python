import Proj06Runner

str = 'The lazy brown fox jumped over the fence.'
sep = ' ' #a space character

print('I certify that this program is my own work')
print('and is not the work of others. I agree not')
print('to share my solution with others.')

result = Proj06Runner.run(str,sep)
for word in result:
    print(word)

print()
str = 'The lazy brown fox jumped over the fence.'
sep = 'o' #This is a lower-case O character

result = Proj06Runner.run(str,sep)
for word in result:
    print(word)




