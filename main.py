introduction = input("Enter your Introduction ")
#print(introduction)
characterCount=0
wordCount=1

for character in introduction:
    characterCount=characterCount+1
    if(character == " "):
        wordCount=wordCount+1
        
print("The no of Words in the Introduction are ",wordCount)
print("The no of letters in the Introduction string are ",characterCount)