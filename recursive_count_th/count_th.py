'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    word.lower()
    
    # base case
    if len(word) == 2:
        return 0
    
    elif word[0] == 't' and word[1] == 'h':
        return count_th(word[1:]) + 1
    
    else:
        return count_th(word[1:])   
    
    pass

print(count_th('oothotho'))

