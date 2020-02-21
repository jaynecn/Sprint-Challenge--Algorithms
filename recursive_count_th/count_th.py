'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    lower = word.lower()
    
    # base case
    if len(lower) < 2:
        return 0
    
    elif lower[0] == 't' and lower[1] == 'h':
        return count_th(lower[1:]) + 1
    
    else:
        return count_th(lower[1:])   
    
    pass

print(count_th('OOOOTHOOOOOTH'))

