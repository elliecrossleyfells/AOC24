###PART 1###

#get the locations into list form
with open('input.txt', 'r') as locations:
    list1 = []
    list2 = []
    for number in locations:
        parts = number.split() #split by space delimiter
        if len(parts) >= 2:
            list1.append(int(parts[0])) #Col 1 in list1
            list2.append(int(parts[1])) #Col2 in list2 and using int to convert the lists from strings to integers

#Sort in ascending order
list1.sort()
list2.sort()

#apply subtraction
subtraction = [abs(a - b) for a, b in zip(list1, list2)] #taking |a-b|
#print(subtraction)

sum = sum(subtraction)
print(sum)

###PART TWO###

#empty dictionary to store where int is in both lists and how many times e.g 1000: 5
count = {}

for number in list1:
    count[number] = list2.count(number)
print(count)

from collections import Counter

# Count the occurrences of each number in list2
counter_list2 = Counter(list2)

# Calculate the similarity score
similarity_score = 0
for number in list1:
    occurrences = counter_list2[number]  # Get how many times the number appears in list2
    similarity_score += number * occurrences  # Multiply by the number itself and add to the score

# Output the result
print(f"Similarity Score: {similarity_score}")