#!/usr/bin/python

'''ISO 15919 transliteration for devanagari text.

Simple usage:

    import iso15919
    romanised_unicode = iso15919.transliterate(indic_unicode)


Copyright (c) 2008 by Mublin <mublin@dealloc.org>
This module is free software, and you may redistribute it and/or modify
it under the same terms as Python itself, so long as this copyright message
and disclaimer are retained in their original form.

IN NO EVENT SHALL THE AUTHOR BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT,
SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF
THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.

THE AUTHOR SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS,
AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.


TODO

    * U+0904 = short a: transliteration?
    * nasalisation of inherent vowel?
    * check danda and double danda transliteration

Sources.

    * http://www.unicode.org/charts/PDF/U0900.pdf
    * http://transliteration.eki.ee/pdf/Hindi-Marathi-Nepali.pdf
    * http://homepage.ntlworld.com/stone-catend/triunico.htm'''

__author__ = "Mublin <mublin@dealloc.org>"
__date__ = "20 April 2008"
__version__ = "0.1.8"

class TransliterationError(Exception):
    pass

DEVANAGARI_START   = u'\u0901'
CANDRABINDU        = u'\u0901'
ANUSVARA           = u'\u0902'
VISARGA            = u'\u0903'
VOWEL_START        = u'\u0904'
VOWEL_END          = u'\u0914'
CONSONANT_START    = u'\u0915'
CONSONANT_END      = u'\u0939'
NUKTA              = u'\u093c'
AVAGRAHA           = u'\u093d'
MATRA_START        = u'\u093e'
MATRA_END          = u'\u094c'
VIRAMA             = u'\u094d'
OM                 = u'\u0950'
UDATTA             = u'\u0951'
ANUDATTA           = u'\u0952'
GRAVE              = u'\u0953'
ACUTE              = u'\u0954'
CONSONANT2_START   = u'\u0958'
CONSONANT2_END     = u'\u095f'
VOWEL2_START       = u'\u0960'
VOWEL2_END         = u'\u0961'
MATRA2_START       = u'\u0962'
MATRA2_END         = u'\u0963'
PUNCTUATION_START  = u'\u0964'
DANDA              = u'\u0964'
DOUBLEDANDA        = u'\u0965'
PUNCTUATION_END    = u'\u0965'
DIGIT_START        = u'\u0966'
DIGIT_END          = u'\u096f'
PUNCTUATION2_START = u'\u0970'
PUNCTUATION2_END   = u'\u0971'
VOWEL3             = u'\u0972'
CONSONANT3_START   = u'\u097b'
CONSONANT3_END     = u'\u097c'
GLOTTALSTOP        = u'\u097d'
CONSONANT4_START   = u'\u097e'
CONSONANT4_END     = u'\u097f'
DEVANAGARI_END     = u'\u097f'

iso15919 = u'''\
\u0901\tm
\u0902\tm
\u0903\th
\u0904\ta
\u0905\ta
\u0906\ta
\u0907\ti
\u0908\ti
\u0909\tu
\u090a\tu
\u090b\tri
\u090c\tli
\u090d\te
\u090e\te
\u090f\te
\u0910\tai
\u0911\to
\u0912\to
\u0913\to
\u0914\tau
\u0915\tk
\u0916\tkh
\u0917\tg
\u0918\tgh
\u0919\tn
\u091a\tch
\u091b\tchh
\u091c\tj
\u091d\tjh
\u091e\tn
\u091f\tt
\u0920\tth
\u0921\td
\u0922\tdha
\u0923\tn
\u0924\tt
\u0925\tth
\u0926\td
\u0927\tdh
\u0928\tn
\u0929\tn
\u092a\tp
\u092b\tph
\u092c\tb
\u092d\tbh
\u092e\tm
\u092f\ty
\u0930\tr
\u0931\tr
\u0932\tl
\u0933\tl
\u0934\tl
\u0935\tv
\u0936\tsh
\u0937\tsh
\u0938\ts
\u0939\th
\u093c\t
\u093d\t'
\u093e\ta
\u093f\ti
\u0940\ti
\u0941\tu
\u0942\tu
\u0943\tri
\u0944\tri
\u0945\te
\u0946\te
\u0947\te
\u0948\tai
\u0949\to
\u094a\to
\u094b\to
\u094c\tau
\u094d\t
\u0950\tom
\u0951\t
\u0952\t
\u0953\t
\u0954\t
\u0958\tq
\u0959\tkh
\u095a\tg
\u095b\tz
\u095c\tr
\u095d\trh
\u095e\tf
\u095f\ty
\u0960\tri
\u0961\tli
\u0962\tli
\u0963\tli
\u0964\t.
\u0965\t..
\u0966\t0
\u0967\t1
\u0968\t2
\u0969\t3
\u096a\t4
\u096b\t5
\u096c\t6
\u096d\t7
\u096e\t8
\u096f\t9
\u0970\t...
\u0971\t
\u0972\t
\u097b\t
\u097c\t
\u097d\t
\u097e\t
\u097f\t'''

# These are special transliterations for consonant triples which have
# a virama in the centre, as well as for some consonant-nukta pairs
# which are not equivalent to a single Unicode character.
clusters = u'''\
\u0939\u093c\tha
\u0938\u093c\tsa
\u0924\u093c\tta
\u0915\u094d\u0937\tksha
\u091c\u094d\u091e\tjnya
\u0924\u094d\u0930\ttra
\u0936\u094d\u0930\tshra'''

# These are combinations of consonant and nukta which are equivalent
# to a single Unicode character.
nukta_consonants = u'''\
\u0929\t\u0928\u093c
\u0931\t\u0930\u093c
\u0934\t\u0933\u093c
\u0958\t\u0915\u093c
\u0959\t\u0916\u093c
\u095a\t\u0917\u093c
\u095b\t\u091c\u093c
\u095c\t\u0921\u093c
\u095d\t\u0922\u093c
\u095e\t\u092b\u093c
\u095f\t\u092f\u093c'''

# This table specifies the transliteration of anusvara where followed
# by a consonant.
anusvara_consonants = u'''\
n\t\u0915 \u0916 \u0917 \u0918 \u0919 \u0924 \u0925 \u0926 \u0927 \u0928
nya\t\u091a \u091b \u091c \u091d \u091e
n\t\u091f \u0920 \u0921 \u0922 \u0923
m\t\u092a \u092b \u092c \u092d \u092e'''

iso15919 = [row.split('\t') for row in iso15919.split('\n')]
iso15919, _iso15919 = {}, iso15919
for char, trans in _iso15919:
    if trans:
        iso15919[char] = trans

clusters = dict(row.split('\t') for row in clusters.split('\n'))

clusterables = dict.fromkeys(cluster[0] for cluster in clusters)

nukta_consonants = dict(row.split('\t') for row in nukta_consonants.split('\n'))

anusvara_consonants, _anusvara_consonants = {}, anusvara_consonants
for row in _anusvara_consonants.split('\n'):
    char, consonants = row.split('\t')
    for consonant in consonants.split(' '):
        anusvara_consonants[consonant] = char

def transliterate(source):
    '''Transliterate Devanagari to the Latin alphabet (ISO 15919).

    transliterate(unicode) -> unicode

    If a unicode character from the Devanagari range cannot be
    transliterated, a TransliterationError is raised. If another
    unicode character cannot be transliterated, it is copied unchanged
    to the result string.'''

    # normalisation: replace consonant + nukta by equivalent
    # consonants
    orig = source
    for char, combination in nukta_consonants.items():
        source = source.replace(combination, char)

    # transliterate character by character
    result, i = [], 0
    while i < len(source):
        char = source[i]

        # anusvara + consonant?
        if char == ANUSVARA:
            try:
                next = source[i+1]
                result.append(anusvara_consonants[next])
                i += 1
                continue
            except (IndexError, KeyError):
                pass

        # vowel + anusvara/candrabindu?
        if i and char in (ANUSVARA, CANDRABINDU):
            prev = source[i-1]
            if VOWEL_START <= prev <= VOWEL_END \
                    or VOWEL2_START <= prev <= VOWEL2_END \
                    or VOWEL3 == prev \
                    or MATRA_START <= prev <= MATRA_END \
                    or MATRA2_START <= prev <= MATRA2_END:
                result.append(u'\u0303')
                i += 1
                continue

        # consonant + virama or matra?
        if i and (char == VIRAMA or
                  MATRA_START <= char <= MATRA_END or
                  MATRA2_START <= char <= MATRA2_END):
            prev = source[i-1]
            if prev != NUKTA or i > 1:
                if prev == NUKTA:
                    prev = source[i-2]
                if (CONSONANT_START <= prev <= CONSONANT_END or
                    CONSONANT2_START <= prev <= CONSONANT2_END):
                    consonant = result[-1]
                    if consonant.endswith('a'):
                        if char == VIRAMA:
                            result[-1] = consonant[:-1]
                        else:
                            result[-1] = consonant[:-1] + iso15919[char]
                        i += 1
                        continue

        # special transliteration for consonant cluster?
        if char in clusterables:
            try:
                next = source[i+1]
            except IndexError:
                pass
            else:
                try:
                    if next == VIRAMA:
                        result.append(clusters[source[i:i+3]])
                        i += 3
                        continue
                    elif next == NUKTA:
                        result.append(clusters[source[i:i+2]])
                        i += 2
                        continue
                except KeyError:
                    pass

        # vowel + nukta?
        if i and char == NUKTA:
            prev = source[i-1]
            if VOWEL_START <= prev <= VOWEL_END \
                    or VOWEL2_START <= prev <= VOWEL2_END \
                    or VOWEL3 == prev \
                    or MATRA_START <= prev <= MATRA_END \
                    or MATRA2_START <= prev <= MATRA2_END:
                result.append(u'\u2018')
                i += 1
                continue

        # default.
        try:
            result.append(iso15919[char])
        except KeyError:
            if DEVANAGARI_START <= char <= DEVANAGARI_END:
                start, end = i - 3, i + 3
                if start < 0:
                    start, end = 0, end - start
                raise TransliterationError('no transliteration for Devanagari %r (%r)' % (char, source[start:end]))
            result.append(char)

        i += 1

    return ''.join(result)