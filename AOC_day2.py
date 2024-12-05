###PART 1###
import pandas as pd

levels = pd.read_csv("input.txt", header = None, names = ["level"])

#Create the method to check for when safe, pass in level (a line from levels list)
def is_safe(level):
    numbers = list(map(int, level.strip().split()))

    #checking inc/dec criteria
    #MUST use i: to refer to index, if use another variable then it checks actual number not indices.
    increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    #checking adjacent criteria 
    adjacency = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))
                    
    return (increasing or decreasing) and adjacency
    

levels["is_safe"] = levels["level"].apply(is_safe)
safe_count = levels["is_safe"].sum()
    
#print(levels)
#print(safe_count)

### PART 2 ###
def problem_dampener(level):
    numbers = list(map(int, level.strip().split()))

    #Handling if already safe by passing to prior is_safe method
    if is_safe(level):
        return True 
    
    for i in range(len(numbers)):
        #creates new list by removing the element at index i from the list
        new_numbers = numbers[:i] + numbers[i + 1:]
        #concats two slices together skipping the ith element
        new_levels = " ".join(map(str, new_numbers))
        #passing new levels to is_safe
        if is_safe(new_levels):
            return True

    return False

#apply problem_dampender to each level
levels["problem_dampener"] = levels["level"].apply(problem_dampener)
#sum safe levels
safe_with_dampener_count = levels["level"].apply(problem_dampener).sum()
print(f"Total safe {safe_with_dampener_count}")