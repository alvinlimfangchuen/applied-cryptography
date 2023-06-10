"""TAC3121 Applied Cryptography Assignment

This is the main file of the RSA python GUI Application. by using tkinter python library to create GUI application for this assignment.
This Python Application consist of 6 files:

1 - rsa.py is the main file for the application. (Button, Label, User Input Text Box)
2 - encode.py is the file for encoding plaintext function.
3 - decode.py is the file for decoding message function.
4 - encrypt.py is the file for encrypting encoded message function.
5 - decrypt.py is the file for decrypting encrypted message function.
6 - generateKey is the file for generate keys for encryptinon and decryption.

"""

from tkinter import *
import  random, sys, os, generateKey, encode, encrypt, decrypt, decode

root = Tk()
root.geometry("850x450")
root.title("Applied Crypto Assignment 1161204339_AlvinLimFangChuen")


#Generate Key
def button_keygen():
    #Generate Key by calling function from generateKey.py
    key   = generateKey.keygen(24)
    key_n = generateKey.key_n
    key_e = generateKey.key_e
    key_d = generateKey.key_d
    #Display Generated Keys On Screen.
    label_key_n = Label(topFrame, text="N: "+key_n, font="Times 10 bold", fg="red")
    label_key_n.grid(row=0, column=2)
    label_key_e = Label(topFrame, text="E: "+key_n, font="Times 10 bold", fg="green")
    label_key_e.grid(row=0, column=3)
    label_key_d = Label(topFrame, text="D: "+key_n, font="Times 10 bold", fg="blue")
    label_key_d.grid(row=0, column=4)

#Encode Message
def button_encode():
    #Retrieve And Store User Input(Plaintext) input in text file
    text = entry_plaintext.get()
    f = open("2_message.txt","w")
    f.write(text)
    #Encode Plaintext by calling encodeMessage Fucntion From encode.py
    encoded = encode.encodeMessage(text)
    #Display The Encoded Message On The Screen
    entry_encode.delete(0, END)
    entry_encode.insert(0, encoded)

#Encrypt Message
def button_encrypt():
    #retrieve 2 key which is key n & e for Encryption
    key_n = generateKey.key_n
    key_e = generateKey.key_e
    #Encrypt The Encoded Message By calling encryptmessage Function From encrypt.py And Send Key n & e As Parameter.
    encrypted = encrypt.encryptmessage(key_e,key_n)
    #Display The Encrytped Message On  The Screen
    entry_encrypt.delete(0,END)
    entry_encrypt.insert(0,encrypted)

#Decrypt Message
def button_decrypt():
    #retrieve 2 key which is key d & n for Decryption
    key_d = generateKey.key_d
    key_n = generateKey.key_n
    #Decrypt The Encrypted Message By calling decryptmessage Function From decrypt.py And Send Key d & n As Parameter.
    decrypted = decrypt.decryptmessage(key_d,key_n)
    #Display The Decrypted Message On The Screen
    entry_decrypt.delete(0,END)
    entry_decrypt.insert(0,decrypted)
    
#Decode Message
def button_decode():
    #Retrive Decoded Message By Calling decodemessage Function From decode.py
    decoded = decode.decodemessage()
    #Display Decoded Message on The Screen
    entry_decode.delete(0,END)
    entry_decode.insert(0,decoded)

#Reset Text On Screen
def button_reset():
    #Reset All Text On Screen to Empty.
    entry_decode.delete(0,END)
    entry_decrypt.delete(0,END)
    entry_encode.delete(0,END)
    entry_encrypt.delete(0,END)
    entry_plaintext.delete(0,END)
    

#Define Frame For Display Location
topFrame = Frame(root)
topFrame.pack()
leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


#Define Label
label_key       = Label(topFrame, text="Key            :", font="Times 12 bold", fg="black")
label_plaintext = Label(topFrame, text="Plain text     :", font="Times 12 bold", fg="black")
label_encode    = Label(topFrame, text="Encoded Text   :", font="Times 12 bold", fg="black")
label_encrypt   = Label(topFrame, text="Encrypted Text :", font="Times 12 bold", fg="black")
label_decrypt   = Label(topFrame, text="Decrypted Text :", font="Times 12 bold", fg="black")
label_decode    = Label(topFrame, text="Decoded Text   :", font="Times 12 bold", fg="black")

#Define Entry(Textboxt)
entry_plaintext = Entry(topFrame, width=50, fg="black")
entry_encode    = Entry(topFrame, width=50, fg="red")
entry_encrypt   = Entry(topFrame, width=50, fg="blue")
entry_decrypt   = Entry(topFrame, width=50, fg="red")
entry_decode    = Entry(topFrame, width=50, fg="black")

#Define Button
button_keygen  = Button(bottomFrame, text="1 - Generate Key", font="Times 10 bold", padx=10, pady=10, command=button_keygen)
button_encode  = Button(bottomFrame, text="2 - Encode Message", font="Times 10 bold", padx=10, pady=10, command=button_encode)
button_encrypt = Button(bottomFrame, text="3 - Encrypt Message", font="Times 10 bold", padx=10, pady=10, command=button_encrypt)
button_decrypt = Button(bottomFrame, text="4 - Decrypt Message", font="Times 10 bold", padx=10, pady=10, command=button_decrypt)
button_decode  = Button(bottomFrame, text="5 - Decode Message", font="Times 10 bold", padx=10, pady=10, command=button_decode)
button_reset   = Button(bottomFrame, text="# - Reset", font="Times 10 bold", padx=10, pady=10, command=button_reset)

#Display Label 
#-- Display Label On The GUI Application --#
label_key.grid(row=0, sticky=E)
label_plaintext.grid(row=1, sticky=E)
label_encode.grid(row=2, sticky=E)
label_encrypt.grid(row=3, sticky=E)
label_decrypt.grid(row=4, sticky=E)
label_decode.grid(row=5, sticky=E)

#Display Entry(Textbox)
#-- Display Entry On The GUI Application --#
entry_plaintext.grid(row=1, column=1)
entry_encode.grid(row=2, column=1)
entry_encrypt.grid(row=3, column=1)
entry_decrypt.grid(row=4, column=1)
entry_decode.grid(row=5, column=1)

#Display Button
#-- Display Button On The GUI Application --#
button_keygen.pack(side=LEFT)
button_encode.pack(side=LEFT)
button_encrypt.pack(side=LEFT)
button_decrypt.pack(side=LEFT)
button_decode.pack(side=LEFT)
button_reset.pack(side=LEFT)


#Display The Application Continously
#-- without this the application will close immediately once it run. --#
root.mainloop()