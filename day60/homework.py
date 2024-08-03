def invert(lst):
    return [-x for x in lst]

print(invert([1, 2, 3, 4, 5]))
print(invert([1, -2, 3, -4, 5]))
print(invert([]))







def inclusive_range(a, b):
    return list(range(a, b + 1))

print(inclusive_range(1, 4))
print(inclusive_range(5, 10))
print(inclusive_range(-3, 2))






def dna_to_rna(dna):
    return dna.replace('T', 'U')

print(dna_to_rna("GCAT"))
print(dna_to_rna("GATTACA"))
print(dna_to_rna(""))
print(dna_to_rna("GTCA"))







