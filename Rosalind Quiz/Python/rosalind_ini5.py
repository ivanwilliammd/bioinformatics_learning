f = raw_input("Enter the path and filename of the file: ")
f1 = open(f)

i=1

output = open('rosalind_ini5_output.txt', 'w+')

for line in f1 :
    if i%2 == 0 :
        print line.rstrip()
        output.write(line.rstrip() + '\n')
    i+=1

output.close()