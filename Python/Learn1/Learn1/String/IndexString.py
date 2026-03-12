text = "Hello World"
print(len(text)) #Return total Index of text
print(text[0]) #Return First index from left to right
print(text[-11]) #Return Frist Index from Rigth to Left
print(text[ : 5]) #Return Index from 0-5
print(text[-11 : -5]) #Return Index from -11 - -5 

for Index in text:
    print(Index)

if text[0] == "H":
    print("Correct!")
else:
    print("Incorrect!")