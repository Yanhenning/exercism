stop = ['UAA', 'UAG', 'UGA']

protein_map = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan'
}


def proteins(strand):
    codons = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    proteins = []

    for codon in codons:
        if codon in stop:
            return proteins
        proteins.append(protein_map[codon])
    return proteins
