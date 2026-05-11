# r -read
# w -write / overwrite
# a -append
# r+ -read and write
# x -exclusive creation (fails if file exists)
# a+ -append and read
# w+ -write and read (overwrites the file if it exists)
# x+ -exclusive creation and read (fails if file exists)
# to delete a file use os.remove('path to file')
# import os module to delete a file

import os
 
comp_file = open('C:/Users/user/Desktop/VSCode/My Python Tutorials/Trials/companies.txt', 'r')
print("File is readable: ", comp_file.readable()) # checks if the file is readable
print("File is readable: ", comp_file.readable()) # checks if the file is readable again
print(comp_file.readlines()) # prints all lines in the file as a list
for files in comp_file.readlines():
    print(files) # prints each line in the file as a list
comp_file.close()

comp_file = open('C:/Users/user/Desktop/VSCode/My Python Tutorials/Trials/companies.txt', 'w')
comp_file.write('Google ') 
comp_file.close()

comp_file = open('C:/Users/user/Desktop/VSCode/My Python Tutorials/Trials/companies.txt', 'a')
comp_file.write('Amazon ')
comp_file.write('Apple ')
comp_file.write('Tesla ')
comp_file.close()

comp_file = open('C:/Users/user/Desktop/VSCode/My Python Tutorials/Trials/newcomp.txt', 'a')
#os.remove('C:/Users/user/Desktop/VSCode/My Python Tutorials/Trials/newcomp.txt')comp_file.close()  