'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # fail-safe if you are not provided correct data
    if (type(word) != str):
        return(f"Not recognised. Please enter a string")
    
    # create a base case 
    elif len(word) <= 1:
        return 0
    
    # moving across the word to check for 'th'
    elif word[0] == 't' and word[1] == 'h':
        return count_th(word[1:]) + 1
    
    else:
        return count_th(word[1:])   

print(count_th('ooooTHoooooth'))
print(count_th('aalkjdlkjlkjthljljljljthljljljljthj'))
print(count_th(12))
