word = input("Enter the text to convert to morse code : ")
text = word.upper()

converter = {
    "text" : ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"],
    "code" : [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]
             }
answer = ""

for letter in text:
    if letter in converter["text"]:
        index = converter["text"].index(letter)
        answer = answer + converter["code"][index] + " "

print(f"Morse code for {word} is : {answer}")