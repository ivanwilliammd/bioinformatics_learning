dna = raw_input("Enter the DNA: ")

adenine = 0
cytosine = 0
guanine = 0
thymine = 0

for word in range(len(dna)) :
    if dna[word] == "A" :
        adenine += 1
    elif dna[word] == "C" :
        cytosine += 1
    elif dna[word] == "G" :
        guanine += 1
    elif dna[word] == "T" :
        thymine += 1

print adenine, cytosine, guanine, thymine