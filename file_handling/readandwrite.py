import os
with open('read/ReadThisFile.txt', 'r') as rf:
    with open('copied_one.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
            n = wf.tell()
            wf.seek(n-1)
            wf.write(" * copied * \n")

            
# That's it for now, to work with images, we need to use the binary mode, which we will see some other time.