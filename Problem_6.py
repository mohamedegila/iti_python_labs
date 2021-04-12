
#problem #6 find the locations that a given character was found in the given string
def find_char_postion(input_word,input_char):
    res = []
    for i in range(0, len(input_word)):
    
        if input_word[i] == input_char:
            res.append(i)
    return res

word = input("enter your string: ")
ch   = input("enter your char you want to search on the entered string: ")


res = find_char_postion(word, ch)

if not res:
    print ("charater '{}' not found in word '{}'".format(ch, word))
else:
    print ("Character '{}' is present at {}".format(ch, str(res)))