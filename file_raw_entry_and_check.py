#file entry and check

filename = raw_entry('Enter file: ')
if (len(filename) < 3) : filename = 'default.txt'  