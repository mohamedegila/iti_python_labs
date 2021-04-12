#problem #4 reads all the text, split them and calculate the 20
# Most used words in the file and then write them to a file
import sys
def most_frequent(list):
    '''
    Function that count word in file content
    and return number of counted words into file
    '''
    word_counter = {}
    for word in list.split(" "):
        if len(word) > 0 and word != '\r\n':
            if word not in word_counter:
                word_counter[word]  = 1
            else:
                word_counter[word] += 1

    for i, word in enumerate(sorted(word_counter, key=word_counter.get,reverse=True)[:20]):
        print("{}: {} ({}) ".format(i+1,word,word_counter[word]))
        file_out = open("popular_words.txt","a")
        file_out.write(word + " (" + str(word_counter[word]) + ")" +"\n")

    file_out.close()

with open(sys.argv[1]) as f:
    contents = f.read()

most_frequent(contents)