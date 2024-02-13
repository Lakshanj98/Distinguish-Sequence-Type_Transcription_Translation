'''
This program translates the RNA into a protein and write it to a fasta file.

Inputs: codon table, RNA sequence
Output: a fasta file containing the protein
author: Lakshan Jayasinghe
'''

codon_table = {}
RNA = ""
codon = ""
number = 0
protein = ""

# entering codon table mappings to the dictionary
with open("codon_table.txt", "r") as file:
    data = file.readlines()
    for line in data[2:]:
        line = line.strip().split()
        if "\n" not in line:
            key = line[0]
            AminoAcid = line[2]
            codon_table[key] = AminoAcid


# Reading mRNA sequence and getting the sequence in to "RNA" variable
with open("OSDREB1A_mRNA.fasta", "r") as file1:
    file_data = file1.readlines()
    for elements in file_data[1:]:
        elements = elements.strip()
        for letter in elements:
            RNA += letter


# Translating the RNA sequence to an amino acid sequence.
# taking first reading frame codons.
while range(len(RNA)):

    codon = RNA[number] + RNA[number + 1] + RNA[number + 2]
    number += 3

    # adding the relevant amino acid for the codon to protein
    protein += codon_table[codon]
    # If any of the stop codons is met, break the loop. Finish the translation process
    if codon == "UAA" or codon == "UAG" or codon == "UGA":
        break


print(len(protein))

# writing the protein sequence in to a fasta file
file3 = open("OSDREB1A_Protein.fasta", "w")
file3.writelines(protein)

file3.close()
