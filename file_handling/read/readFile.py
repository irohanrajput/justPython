import os
with open('ReadThisFile.txt', 'r+') as f:

    # 'w' is for write mode, 'r' is for read mode, 'a' is for append mode. 'w+' is for read and write mode, 'r+' is for read and write mode, 'a+' is for read and append mode

    print(f.read()) # Read the whole file
    print(f.readline()) # Read the first line
    print(f.readlines()) # Read all lines and return a list
    print(f.tell()) # Get the current position
    print(f.seek(10)) # Set the current position to 10
    print(f.close()) # Close the file
    print(f.closed) # Check if the file is closed    with open('ReadThisFile.txt', 'r+') as f:
    with open('ReadThisFile.txt', 'a+') as f:
        f.write("This is some appended content.")
