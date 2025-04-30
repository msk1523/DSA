def noOfWords(sentence):
    words=sentence.split(" ")
    count=0
    for word in words:
    
        if word[0] == '0' or word[0] == '1' or word[0] == '2' or word[0] == '3' or word[0] == '4' or word[0] == '5' or word[0] == '6' or word[0] == '7' or word[0] == '8' or word[0] == '9':
        # if word[0].isnumeric():
            count-=1
    for i in range(len(words)):
        count+=1
    return count

print(noOfWords("This is a test sentence with 3"))
print(noOfWords("This is a test sentence with 3 words 0")) # 7