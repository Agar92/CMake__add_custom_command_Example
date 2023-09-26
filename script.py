### #!/usr/bin/python3
import re

string='Hello, from the hell...'
string += "123\n"

with open("./myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Helloooooooooooo \n")
    file1.write(string)

print(string)
