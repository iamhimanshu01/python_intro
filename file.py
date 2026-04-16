#opening a file in python
#open (file_name,mode to open)
#modes: "r",'x',w,r,a,t,b

# file_handler = open("practice.txt",'rt')
# print(file_handler)
# file_handler.close()

#how to create a file in file handling
# x mode=> create a file
# fh =open("file1.txt",'xt')


# fh.write("this file is created using the 'x' mode in python.\n")
# fh.write("next line.\n")
# fh.write("this is my code and also want to improve my coding journey.\n ")
# fh.close()

# w mode -open the file for writting overwrite the file
# 'w' mode delete all values in in file file and to write the new line in there

# fh =open("file1.txt",'wt')
# fh.write("this is my new line is used to write this in python.\n")
# fh.write("have a nice day.\n")
# fh.write("this is new line of code .\n")
# fh.write("bihar is most popular state in india.\n")
# fh.close()


#'r' mode: r mode read the line by line 
# file_handler = open("file1.txt",'rt')
# # line1 = file_handler.readline()
# line2 = file_handler.readlines()
# content = file_handler.read()




# file_handler.close()

# # print(f"line1: {line1}")
# print(f"line2:{line2}")


#'a' mode : append mode
# if the file does not exist 'a' mode creates the file 

fh = open ("file1.txt",'at')
fh.write("this file has been created using 'a'mode.\n")
fh.write(" 'a' mode creates the files if not already existing.\n")
fh.write("good bye")
fh.close()