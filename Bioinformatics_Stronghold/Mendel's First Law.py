import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

number = "20 30 29"

homozygote = int(number.split()[0])
heterozygote = int(number.split()[1])
recessive = int(number.split()[2])
# print homozygote, heterozygote, recessive

# multiply 4 due to probability each organism may have 4 type of offspring
total_offspring = 4 * ncr(homozygote+heterozygote+recessive, 2)

# recessive phenotype due to 4 * recessive x recessive, 2 * recessive x heterozygote, 1 * heterozygote x heterozygote
recessive_phenotype = 4*ncr(recessive, 2) + 2*ncr(heterozygote,1)*ncr(recessive,1) + 1*ncr(heterozygote,2)
# print(recessive_phenotype)

dominant_phenotype = total_offspring - recessive_phenotype

print float(dominant_phenotype)/float(total_offspring)