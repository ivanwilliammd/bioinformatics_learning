def countoddsum(a,b):
    sum=0
    for i in range(a-1,b+1):
        if i % 2 == 1:
            sum += i
    return sum

print "Input"
dataset = raw_input()
a = dataset.split()[0]
b = dataset.split()[1]

sum = countoddsum(int(a),int(b))
print sum