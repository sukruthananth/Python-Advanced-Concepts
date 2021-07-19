'''f = open('data.txt','r+')

print(f.newlines("a new line"))
f.close()
'''
#context manager
'''
with open('data.txt', 'r') as f:
    for line in f:
        print(line, end="")
    pass
'''
'''with open('data.txt', 'r') as f:
    size_to_read = 5
    file_content = f.read(size_to_read)
    while len(file_content) > 0:
        print(file_content,end="")
        #f.seek(0)
        #print(f.tell())
        file_content = f.read(size_to_read)

    pass
'''

'''with open('dataw.txt', 'w') as f:
    f.write('first line')
    print(f.tell())
    f.write('second line')
    pass'''

'''with open('data.txt', 'r') as rf:
    with open('copydata.txt', 'w') as wf:
        for line in rf:
            wf.write(line)'''


## rb and wb lets you do te same thing in a binary file. We cannot read a jpg type of file with above code so convert it into b

with open('puppy.jpg', 'rb') as rf:
    with  open('puppy_copy.jpg','wb') as wf:
        chunk_size = 4096
        chunk = rf.read(chunk_size)
        while len(chunk) >0:
            wf.write(chunk)
            chunk = rf.read(chunk_size)