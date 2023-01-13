#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Creeare unei liste cu toate numele


with open("./Input/Names/invited_names.txt", "r") as names:
    lista_nume = names.readlines()
    print(lista_nume)


def create_letter(name):
    with open("./Input/Letters/starting_letter.txt", "r") as letter:
        scrisoarea = letter.read()
        scrisoarea = scrisoarea.replace("[name]", name)
        scrisoarea = scrisoarea.replace("Angela", "Maryus")
    with open("./Output/ReadyToSend/letter_for_"+name, mode="w") as letter1:
        letter1.write(scrisoarea)

for num in lista_nume:
    new_name = num.strip()
    print(new_name)
    create_letter(name=new_name)







