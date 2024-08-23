#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
numbers = []
while True:
    user_input = input("Enter an Integer(or type 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an Integer.")
total_sum = sum(numbers)
print(f"The sum of the entered numbers is: {total_sum}")

#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
books =("rome and Julient","Animal Farm","Darkness at noon","Lord of the Rings","Lord of the flies")
for book in books:
   print(book)
   
#Write a program that uses a dictionary to store information about a person, 
# such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.
dict = {}
dict ['name'] = input("Enter your name:")
dict['age'] = input("Enter your age:")
dict ['favorite color'] = input("Enter your favorite color:")

print("\nperson Information:")
print(dict)

#Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
set1 = set()
set2 =set()
print("Enter integers for the first set(type 'done' to finish):")
while True:
    user_input = input("Enter an Integer:")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        set1.add(number)
    except ValueError:
        print("Invalid input. Please enter an Integer.")
        
print("\nEnter integers for the second set(type 'done' to finish):")
while True:
    user_input = input("Enter an Integer:")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        set2.add(number)
    except ValueError:
        print("Invalid input. Please enter an Integer.")
        
common_elements = set1.intersection(set2)

print(f"\nCommon elements between the two sets are: {common_elements}")

#Create a program that stores a list of words. 
#Then, use list comprehension to create a new list that contains only the words that have an odd number of characters

words =[]
print("Enter th words to store in list(type 'done' to finish):")

while True:
    word = input("Enter word:")
    if word.lower() == 'done':
        break
    words.append(word)
odd_length_words = [word for word in words if len(word)%2 != 0]
print(f"\noriginl list of words: {words}")
print(f"words with an odd number of characters: {odd_length_words}")
