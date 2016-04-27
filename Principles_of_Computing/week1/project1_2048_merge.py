"""
Merge function for 2048 game.
"""
def slide_left(line):
    """
    Function that slide not zero values to left for 2048 game.
    """
    result =[]
    for num in line:
        if num != 0:
            result.append(num)
    #check len
    if len(result) != len(line):
        result.extend([0] * (len(line) - len(result)))
    return result   
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    result = slide_left(line)
    
    for index in range(len(result)):
        if result[index] != 0: 
            if index+1 < len(result) and result[index] == result[index+1]:
                result[index] += result[index]
                result[index+1] = 0
    return slide_left(result)
    

print merge( [2, 0, 2, 4] ) #should return [4, 4, 0, 0]
print merge([0, 0, 2, 2] )#should return [4, 0, 0, 0]
print merge([2, 2, 0, 0] )#should return [4, 0, 0, 0]
print merge([2, 2, 2, 2, 2]) #should return [4, 4, 2, 0, 0]
print merge([8, 16, 16, 8] )#should return [8, 32, 8, 0]