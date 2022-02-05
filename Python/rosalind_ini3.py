def sliceword(word, a, b, c, d):
    return word[a:b+1] + ' ' + word[c:d+1]


print "Input Word"
word = raw_input()

print "Input A"
a = input()

print "Input B"
b = input()

print "Input C"
c = input()

print "Input D"
d = input()

res = sliceword(word, a, b, c, d)
print res