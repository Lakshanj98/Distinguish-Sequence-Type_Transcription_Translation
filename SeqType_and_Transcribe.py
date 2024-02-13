"""A program which distinguishes between DNA sequences and protein sequences.
If the sequence type is DNA, transcribe the DNA sequence to RNA.
Then writes the transcribed RNA to a fasta file.

Input - a fasta file containing both DNA sequences and protein sequences.
Output - A fasta file containing the transcribed RNA
Author -Lakshan Jayasinghe
"""

MyDict = {}
MySeq = {}
header = ""
sequence = ""
mRNAheader = ""
mRNA = ""
amino_acids = ["K", "N", "R", "S", "I", "M", "Q", "H", "P", "R", "L", "E", "D", "V", "Y", "S", "W", "F"]
flag = False


with open("mRNA&p.fasta") as file:

    # separating the header and sequences using the ">" symbol at the beginning of fast sequence.
    for line in file:
        if ">" in line:
            line = line.strip()
            header = line
            sequence = ""
        elif line != "\n":
            line = line.strip()
            sequence += line
        MyDict[header] = sequence


for key in MyDict:
    # checking whether any amino acid is present in the sequence
    # if amino acids are not present, it is a DNA sequence
    for aa in amino_acids:

        # if any amino acid is in the current dictionary value, set the flag true
        if aa in MyDict.get(key):
            flag = True

    print(MyDict.get(key))
    print(flag)

    # if the flag is false, this sequence is a DNA sequence
    if not flag:
        mRNAheader = key
        mRNA = ""

        # transcribing the DNA sequence to RNA
        for base in MyDict[key]:
            if base == "T":
                mRNA += "U"
            else:
                mRNA += base

        # inserting all transcribed sequences to the MySeq dictionary
        MySeq[mRNAheader] = mRNA

    # Open the file for writing all sequences
    with open("OSDREB1A_mRNA.fasta", "w") as file:

        # writing the transcribed mRNA headers and mRNA sequences in to a new fasta file.
        for mRNAheader in MySeq:
            print("")
            print(mRNAheader)

            file.writelines(mRNAheader + " transcribed\n")
            file.writelines(mRNA+"\n")

    # set the flag to default(False) condition
    flag = False
