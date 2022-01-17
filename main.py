import sys

sequence = input("Enter the DNA Sequence: ")

if len(sequence) < 1:
    sequence = "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC   C"
    print(f"Since you didn't choose any DNA sequence, you will be use the default sequence: {sequence}")

sequence = sequence.strip()
sequence = sequence.replace(" ", "")
sequence = sequence.upper()
sequence = "".join(sequence)

invalidLetters = ["B", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "W", "X", "Y", "Z"]

for letter in invalidLetters:
    if letter in sequence:
        print(f"Invalid characters detected in DNA sequence: {letter}")    
        sys.exit()

baseDict = {
    "A": sequence.count("A"),
    "T": sequence.count("T"),
    "G": sequence.count("G"),
    "C": sequence.count("C")
}

print("In your given DNA structure...")
print(f"There are {baseDict['A']} adenine.")
print(f"There are {baseDict['T']} thymine.")
print(f"There are {baseDict['G']} guanine.")
print(f"There are {baseDict['C']} cytosine.")