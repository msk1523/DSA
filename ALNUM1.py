def noOfWords(sentence):
    words=sentence.split(" ")
    count=0
    # I SCORED 300 MARKS IN MY EXAMSS! THIS IS AMAZING SINCE OUT OF 100 STUDENTS MY RANK WAS 2 -16
    for word in words:
        if word.isnumeric():
            count-=1
    for i in range(len(words)):
        count+=1
    return count

print(noOfWords("I SCORED 300 MARKS IN MY EXAMSS! THIS IS AMAZING SINCE OUT OF 100 STUDENTS MY RANK WAS 2"))
print(noOfWords("This is a test sentence with 3 words 0")) # 7