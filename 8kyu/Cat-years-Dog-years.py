# // I have a cat and a dog.
# // I got them at the same time as kitten/puppy. That was humanYears years ago.
# // Return their respective ages now as [humanYears,catYears,dogYears]

# // NOTES:
# //     humanYears >= 1
# //     humanYears are whole numbers only

# // Cat Years
# //     15 cat years for first year
# //     +9 cat years for second year
# //     +4 cat years for each year after that

# // Dog Years
# //     15 dog years for first year
# //     +9 dog years for second year
# //     +5 dog years for each year after that


def human_years_cat_years_dog_years(human_years):
    dogYears = 0
    catYears = 0
    
    if human_years >= 1:
        #cat
        if human_years == 1:
            catYears += 15
        elif human_years == 2:
            catYears += (15 + 9)
        else:
            catYears += 15 + 9 + (4 * (human_years - 2))
            
        if human_years == 1:
            dogYears += 15
        elif human_years == 2:
            dogYears += (15 + 9)
        else:
            dogYears += 15 + 9 + (5 * (human_years - 2))

    return [human_years, catYears, dogYears]

#https://www.codewars.com/kata/reviews/5a67b10993f7627b99002ee6/groups/6465442885793c00016db5d5
