dna = input("Enter a DNA sequence: ").upper()

valid_bases = {"A", "T", "G", "C"}

if not all(base in valid_bases for base in dna):
    print("Error: Invalid DNA sequence!")
else:
    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    length = len(dna)
    gc_content = ((g + c) / length) * 100

    print("\nDNA Analysis")
    print("------------")
    print("Length:", length)
    print("A:", a)
    print("T:", t)
    print("G:", g)
    print("C:", c)
    print(f"GC Content: {gc_content:.2f}%")