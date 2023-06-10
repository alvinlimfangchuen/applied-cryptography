"""Example:
    1-The plain text is "Hello World", the total length of the text is 11 instead of 10 because "space" is also considered a character.
    2-The algorithm will split the the text to five-character block so it will split into 3 part for "Hello World".
    3-Convert string to hex value letter by letter. 
    4-so first the variable "hex_value_size5" will first store the hex value of letter(h) until it reach 5th letter which is letter(o), then loop will again to convert string to hex untill all the text is converted.
      (0, len(text),character_blocksize) = (0,11(Text Lenght),5(Charater_blocksize)) 
                        1st part - Hello        = 0068656C6C6F
                        2nd part - "space"Worl  = 0020776F726C
                        3rd part - d            = 000000000064
    5-Each time the converted string reach to 5th-Character, it will store in variable "encoded_text".(will store all 3 part)
      #the first 5 character loop            #the second 5 character loop                        #the second third character loop
      hex_value_size5 = 0068656C6C6F         encoded_text    = 0068656C6C6F0020776F726C          encoded_text    = 0068656C6C6F0020776F726C000000000064
      encoded_text    = ""
      encoded_text += hex_value_size5 
      encoded_text    = 0068656C6C6F

    @ zfill() is a python built-in function to up character to intended number of digit(12)
      Example: the hex value is d is "64", using zfill() function to fill it up to 12-digit-000000000064
        
"""

#This function is called once the button "Encode Message" on GUI application is clicked and retrieve plaintext as parameter for encoding
def encodeMessage(text):
        encoded_text=""
        character_blocksize = 5
        #Split the strings by five-character block then convert it to hexadecimal value
        for i in range(0, len(text), character_blocksize ):
            j = 0
            while j < character_blocksize :
                if i + j < len(text):
                    hex_value=format(ord(text[i + j]), "X").zfill(2)

                    if(j == 0):
                        hex_value_size5 = "00"
                        hex_value_size5  += hex_value
                    elif (j == character_blocksize -1):
                        hex_value_size5  += hex_value
                        encoded_text += hex_value_size5 
                        hex_value_size5 =""
                    else:
                        hex_value_size5  += hex_value

                    j+=1
                else:
                    #Once each 5th-character block string is converted hex value it all store in "encoded_text", then loop again untill all string is converted to hex
                    if(hex_value_size5  == ""):
                        break
                    else:
                        hex_value_size5  = hex_value_size5 .zfill(12)
                        encoded_text += hex_value_size5 
                        break
      
        #Write The Encoded Text To Text File
        f = open("3_encoded.txt","w")
        f.write(encoded_text)
        f.close()
        #return Encoded Text To Display It On Screen
        return encoded_text