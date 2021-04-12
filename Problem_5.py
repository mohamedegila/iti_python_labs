
#problem #5 remove the vowels character from input word
def remove_vowel(input_char):
    
    '''
    Function to remove vowels from a given word 
    and return it back
    '''
    vowels = ('a', 'e', 'i', 'o', 'u')
    for ch in input_char.lower():
        if ch in vowels:
            input_char = input_char.replace(ch, "")        
    return input_char

input_word = input("Enter a word: ")

print("The word after remove vowels:   " ,remove_vowel(input_word))