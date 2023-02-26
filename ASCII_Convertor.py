from tkinter import*

root = Tk()
root.title("Encryption with ASCII Code")
root.geometry("400x400")

text_input = Entry(root)
text_input.place(relx = 0.5, rely = 0.4, anchor = CENTER)

name = Label(root, text = "Name in ASCII: ")
encrypted_name = Label(root, text = "Encrypted Name: ")

def asciiConverter():
    input_word = str(text_input.get())
    
    for letter in input_word:
        name["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        encrypted_name["text"] += str(chr(encrypted))
        
btn = Button(root, text = "Generate the ASCII Code & Encrypted value", command = asciiConverter)

btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
name.place(relx = 0.5, rely = 0.6, anchor = CENTER)
encrypted_name.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()

