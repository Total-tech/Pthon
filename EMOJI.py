message = input(">>>")
words=message.split(' ')
dict1 = {
    ":)":"😊",
    ":(":"😒",
    ":|":"🤐"
}
output=""
for word in words:
    output+=dict1.get(word,word) + " "
print(output)