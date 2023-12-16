with open('WriteThisFile.txt', 'w') as somefile:
    # 'w' is for write mode, 'r' is for read mode, 'a' is for append mode
    # 'w+' is for read and write mode, 'r+' is for read and write mode, 'a+' is for read and append mode
    somefile.write('This is how we write in a file.\n')

    somefile.seek(0) # this will move the cursor to the beginning of the file

    somefile.write('This is the second line.\n') # this will overwrite the the text in the first line but not all of it, but only till the point it needs the space for it,