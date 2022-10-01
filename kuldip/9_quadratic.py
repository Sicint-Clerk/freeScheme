import re

sample_file = open('data.txt')

text = sample_file.read()
numbers = re.findall('[0-9]+', text) #Match any combination of one or more digits

#Casting them to integers and getting the total sum
total = sum(int(num) for num in numbers)

print(total)

#Closing the file to avoid memory problems
sample_file.close()