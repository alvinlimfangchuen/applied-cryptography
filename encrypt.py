#This function is called once the button "Encrypt Message" on GUI application is clicked and retrieve Key e and n for encrption
def encryptmessage(key_e,key_n):
        #Define Encryption Keys
        encrypt_e = int(key_e, 16)
        encrypt_n = int(key_n, 16)
        #Retrieve Encoded Text From Text File
        f = open("3_encoded.txt","r") 
        text = f.readline()
        f.close()
        #Define Variable For Encrypted String    
        encrypted_string=""
        n = 12

        #Loop To Encrypt All Encoded Text
        for i in range(0, len(text), n):
            j = 0
            c12 = ""
            encoded_value=""
            encrypted_value=""
            while j < n:
                if(c12 == ""):
                    #Concate 0x With  Firtst Letter Of Encoded Text To Indicate It As Hex Value
                    c12 = "0x" + text[i + j]
                else:
                    #Concate With Next Letter Text Then Convert it Back
                    c12 += text[i + j]
                j += 1
            encoded_value = int(c12, 16)
            encrypted_value = pow(encoded_value,encrypt_e,encrypt_n)
            encrypted_string += format(encrypted_value,"X").zfill(12)

        #Write Encrypted Text Into Text File
        f = open("4_encrypted.txt","w")
        f.write(encrypted_string)
        f.close()
        #Return Encrypted Text To Display It On Screen
        return encrypted_string
