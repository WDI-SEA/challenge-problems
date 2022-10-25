# find common characters

# split each its own array
# compare each letter in the word to see if its in the other words
# put that letter into return array
# edge case - duplicate letters

def common_characters(words):
    word_dict = {}
    common_chars = []
    for word in words:
        word_dict[word] = list(word)
    
    for key in word_dict:
        for letter in word_dict[key]:
            common = True
            for key_two in word_dict:
                if letter not in word_dict[key_two]:
                    common = False
            if common == True:
                common_chars.append(letter)

    return print(common_chars)

def common_characters_taketwo(words):
    common_chars = list(words[0])
    for i in range(1, len(words)):
        print(common_chars)
        for char in common_chars:
            if char not in words[i]:
                common_chars.remove(char)
    
    return print(common_chars)


# common_characters_taketwo(["bella","label","roller"])
common_characters_taketwo(["cool","lock","cook"])
# common_characters_taketwo(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"])