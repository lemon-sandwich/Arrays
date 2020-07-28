#Bubble Sort

numbers = [4,3,2,5,67,64,1] # Enclosing in square brackets makes a list
n = len(numbers)    # For the length of array
for i in range(n-1):    # range takes two intgers, first is the starting and the other is the ending
    for j in range(0,n-i-1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp     # this could also be done using the swap function numbers[j],numbers[j+1] = numbers[j+1] ,numbers[j]

for n in range(len(numbers)):
    print(str(numbers[n]) + " ")

# -------------------------------------------------------------------- #
# Using a return-type funciton

def BubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
    return arr

arr = [4,5,23,1,7,8,4,23,76,83,23,546]
arr = BubbleSort(arr)
length = len(arr)
print("Sorted Array :- ")
for n in range(length):
    print(arr[n] , end = " ")   # If you want to display something in one line


# ---------------------------------------------------------------------- #
# Exercise
def cls():
    for i in range(100):
        print('\n')
input("\nPress And Enter Any Key To Start Next Program\n")
cls()
expenses = [
    ['January',2200],
    ['February',2350],
    ['March',2600],
    ['April',2130],
    ['May',2190]
]

print("\n\n1. In Feb, how many dollars you spent extra compare to January?")
extra = expenses[1][1] - expenses[0][1]
print(f"Answer = {extra}")
print("2. Find out your total expense in first quarter (first three months) of the year.")
i = 2
sum = 0
while i > -1:
    sum += expenses[i][1]
    i -= 1
print(f"Answer = {sum}")
print("3. Find out if you spent exactly 2000 dollars in any month")
spent = False
print("Answer = ",end= " ")
for n in range(len(expenses)):
    if expenses[n][1] == 2000:
        print(f"{expenses[n][0]}", end = " ")
        spent = True
if spent != True:
    print("No.")
print("4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list")
expenses.append(['June',1980])
print("Answer = Added")
print("5. You returned an item that you bought in a month of April and" , end=" ")
print("got a refund of 200$. Make a correction to your monthly expense list" , end=" ")
print("based on this")
for n in range(len(expenses)):
    if expenses[n][0] == "April":
        expenses[n][1] -= 200
print("Done")

# ---------------------------------------------------------- #
# Insertion and Deletion
input("\nPress And Enter Any Key To Start Next Program\n")

heros = ['spider man','thor','hulk','iron man','captain america']
print("1. Length of the list")
print(f"Answer: {len(heros)}")
print("2. Add 'black panther' at the end of this list")
heros.append('black panther')
print(heros)
print("3. You realize that you need to add 'black panther' after 'hulk',",end = "")
print("so remove it from the list first and then add it after 'hulk'")
if 'black panther' in heros:
    heros.remove('black panther')
for i in range(len(heros)):
    if heros[i] == 'hulk':
        heros.insert(i+1,'black panther')
        break
print(heros)
print("4. Now you don't like thor and hulk because they get angry easily :)")
print("So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).")
print("Do that with one line of code.")
heros[1:3] = ['doctor strange']     # Starting index and till which length, replaces with the str or int written
print(heros)
print("5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)")

def Ascii(word1,word2):     #Function To Sort String Through Ascii Characters
    ascii1 = ascii2 = 0
    for n in range(len(word1)) or range(len(word2)):
        if ord(word1[n]) > ord(word2[n]):
            return True
        elif ord(word2[n]) > ord(word1[n]):
            return False
        ascii1 += ord(word1[n])
        ascii2 += ord(word2[n])
    if ascii1 > ascii2:
        return True
    else: return False

for i in range(len(heros) - 1):
    for j in range(len(heros) - i - 1):
        if Ascii(heros[j],heros[j+1]):
            heros[j],heros[j+1] = heros[j+1],heros[j]
print(heros)

# ---------------------------------------------------------- #
# Odd Numbers
input("\nPress And Enter Any Key To Start Next Program\n")

print("Create a list of all odd numbers between 1 and a max number. ",end= "")
print("Max number is something you need to take from a user using input() function")
Max = int(input("Select A Max Number: "))
Odd_Numers = []
if Max > 0:
    for n in range(Max):
        if n % 2 == 1:
            Odd_Numers.append(n)
else: print("Max Number is smaller than zero :(")
print(Odd_Numers)