# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!

# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

def better_than_average(class_points, your_points):
#     class_points = [12, 23, 34, 45, 56, 67, 78, 89, 90]
#     todays_points = [100, 40, 34, 57, 29, 72, 57, 88]
#   your_points = 5
    
    total = sum(class_points)
    count = len(class_points)
    average = total / count
    
    if your_points >= average:
        return True
    else:
        return False
    
    return