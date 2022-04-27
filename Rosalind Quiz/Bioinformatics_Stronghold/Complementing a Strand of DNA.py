dna = raw_input("Enter the DNA: ")
complement_dictionary = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

reverse_complement = ""

for i in range(len(dna)) :
    reverse_complement += complement_dictionary[dna[-(i+1)]]

print reverse_complement