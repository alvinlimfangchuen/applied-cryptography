#This function is called once the button "Decrypt Message" on GUI application is clicked and retrieve Key d and n for encrption
def decryptmessage(key_d,key_n):
        #Define Decryption Keys
        decrypt_d = int(key_d, 16)
        decrypt_n = int(key_n, 16)
        #Retrive Encrypted Text From Text File
        f = open("4_encrypted.txt","r")
        text = f.readline()
        f.close()
        #Define Variable For Decrypted String
        decrypted_string=""
        n = 12
        
       #Loop To Decrypt All Encoded Text
        for i in range(0, len(text), n):
            j = 0
            c12 = ""
            encrypted_value=""
            while j < n:
                if(c12 == ""):
                    #Concate 0x With  Firtst Letter Of Encoded Text To Indicate It As Hex Value
                    c12 = "0x" + text[i + j]
                else:
                    #Concate With Next Letter Text Then Convert it Back
                    c12 += text[i + j]
                j += 1
            encrypted_value = int(c12, 16)
            #decrypted_value = encrypted_value ** decrypt_d % decrypt_n
            decrypted_value=pow(encrypted_value,decrypt_d,decrypt_n)
            decrypted_string += format(decrypted_value,"X").zfill(12)
            
        #Write Decrypted Text Into Text File
        f = open("5_decrypted.txt","w")
        f.write(decrypted_string)
        f.close()
        #Return Encrypted Text To Display It On Screen
        return decrypted_string