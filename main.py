meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            
            "LOL": "Una risposta comune a qualcosa di divertente",
            
            "SHEESH": "leggera disapprovazione",

            "CREEPY": "spaventoso, inquietante",

            "PARA": "preoccuparsi per qualcosa, paranoiarsi",
    
            "PROLLY": "versione accorciata di probably",
        
            "GG": "significa buon gioco"
    
    
            }


print("Buongiorno,abbiamo alcune parole del lessico di internet che la")
print("potrebbero interessare.Per adesso sono limitate,ma si accontenti.")





for i in range(5):


    questionWord = input("Inserisca parole che non conosce(in lettere maiuscole): ")

    if questionWord in meme_dict.keys():

        if questionWord == "CRINGE":
            
            print(meme_dict["CRINGE"])   
        
        elif questionWord == "LOL":
            
            print(meme_dict["LOL"])
        
        elif questionWord == "SHEESH":
            
            print(meme_dict["SHEESH"])
        
        elif questionWord == "CREEPY":
            
            print(meme_dict["CREEPY"])
        
        elif questionWord == "PARA":
            
            print(meme_dict["PARA"])
    
        elif questionWord == "PROLLY":
            
            print(meme_dict["PROLLY"])
    
    
        elif questionWord == "GG":
            
            print(meme_dict["GG"])
    
    
    else:
        
        print("O la parola non faceva parte del nostro dizionario,o ha sbagliato tasti ")
        
        
        
print("i suoi tentativi sono finiti, aspettate la ricarica")










































