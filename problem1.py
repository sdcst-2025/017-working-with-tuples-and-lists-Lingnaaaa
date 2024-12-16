#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
mylist=[]

for i in range(2):
    i=input('Enter a word:')

    mylist.append(i)
print(f"The original list is, {mylist}")

x=input('Enter a number that you want to replace:')
y=input('Enter a new word:')

if x in mylist:
    index=mylist.index(x)
    mylist[index]=y
    print(mylist)
else:
    print(f"{x} is npt on the list")
