
vowels = ['a', 'e', 'i','o', 'u', 'y']

def split(word):
    return list(word)
     
# Driver code
word = input("Enter your desier sentence :")
word_split = split(word)
# print(word_split)  



for i in range(len(word_split)):
    for j in range (len(vowels)):
        if  word_split[i]== vowels[j]:
             word_split[i]='^-^'

# print(word_split)
# convert list to string 
print(''.join([str(elem) for elem in word_split]))
