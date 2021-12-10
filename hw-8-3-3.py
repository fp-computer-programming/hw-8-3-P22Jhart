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

print(count_odds([2, 4, 6, 8, 9]) == 20
print(count_odds([13, 12, 10]) == 0
print(count_odds([14, 16, 32]) == 62