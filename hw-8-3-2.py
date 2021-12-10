def count_odds(lst): 
    odd = 0
    X = 0
    while X < len(lst):
        if lst[X] % 2 != 0:
           odd += 1 
        X  += 1 
    else:
        X += 1 
    
    return odd 

print(count_odds([1, 2, 3, 4, 5, 6]) == 9)
print(count_odds([1, 3, 5, 7, 9]) == 25)
print(count_odds([2, 4, 6, 8, 10]) == 0)