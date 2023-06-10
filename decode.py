
#This function is called once the button "Decode Message" on GUI application is clicked and retrieve encode text by reading 4_encoded.txt file
def decodemessage():
        #Retrieve encoded text from the text file
        f = open("5_decrypted.txt","r")
        text = f.readline()
        f.close()
        #Encoded Text Is in 12-Digit hexadecimal format, Set Decoded Size
        character_blocksize = 12
        decoded_text=""
        for i in range(0, len(text), character_blocksize):
            j = 0
            character_size2 = ""
            while j < character_blocksize:
                if(character_size2 == ""):
                    #Add 0x to each letters to indicate it as Hex Value
                    character_size2 = "0x" + text[i + j]
                else:
                    #Concate first and Second letter
                    character_size2 += text[i + j]
                    inttext = int(character_size2, 0)
                    if(inttext != 0):
                        decoded_text += chr(inttext)
                    character_size2 = ""
                j += 1
        #Write Decoded Text In Text File        
        f = open("6_decoded.txt","w")
        f.write(decoded_text)
        f.close()
        #Return Decoded Text To Display It On Screen
        return decoded_text

