text ="hello,this is a sample text to be saved in a notepad file"
#specify the file path where you want to save the text
file_path="sample_text.txt"

#open the file in write mode and write the text
with open (file_path,'w')as file:file.write(text)

print("text saved sucessfully in the notepad file")