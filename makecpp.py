### #!/usr/bin/python3
import re

Lines = [
    '#include <iostream>\n',
    '                   \n',
    'int main(){        \n',
    '  return 0;        \n',
    '}                  \n'
]

file1=open('/home/andrey/Desktop/test_dir/check.cpp', 'w+')
file1.write('HELL!')
file1.close()

print("GONE VERSION={}".format(1))

with open('/home/andrey/Desktop/test_dir/o.cpp', 'w+') as file1:
    # Writing data to a file
    file1.write('fear')

with open('/home/andrey/Desktop/test_dir/o.cpp', 'w+') as file1:
    # Writing data to a file
    file1.writelines(Lines)
###



