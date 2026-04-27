  #  file_i_o
file=open("file.txt","w")
file.write("Hello, World!")
file.close()
with open("file.txt","r") as file:
    content=file.read()
    print(content)

    