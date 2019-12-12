anusvara_consonants = u'''\
n\t\u0915 \u0916 \u0917 \u0918 \u0919 \u0924 \u0925 \u0926 \u0927 \u0928
nya\t\u091a \u091b \u091c \u091d \u091e
n\t\u091f \u0920 \u0921 \u0922 \u0923
m\t\u092a \u092b \u092c \u092d \u092e'''

#print(repr(anusvara_consonants))

anusvara_consonants, _anusvara_consonants = {}, anusvara_consonants
for row in _anusvara_consonants.split('\n'):
    char, consonants = row.split('\t')
    print(repr(char))
    print(repr(consonants))
    print('\n')
    for consonant in consonants.split(' '):
        anusvara_consonants[consonant] = char

