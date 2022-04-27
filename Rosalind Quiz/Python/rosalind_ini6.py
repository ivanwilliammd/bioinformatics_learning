f = raw_input("Enter the path and filename of the file: ")
f1 = open(f)

output = open('rosalind_ini6_output.txt', 'w+')

word_bag = {}

for word in str.split(f1.read().rstrip()) :
    if word.isalpha() :
        if word in word_bag:
            word_bag[word] += 1
        else:
            word_bag[word] = 1

for key, value in word_bag.items():
    print key, value
