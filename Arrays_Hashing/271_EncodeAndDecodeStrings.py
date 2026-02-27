def encode(strs) -> str:
    res = ""

    # add "length of word + '#' + word" to resulting string
    for s in strs:
        n = len(s)
        res += str(n) + '#' + s

    return res

def decode(s):

    i = j = 0
    n = len(s)
    res = []

    while i < n:
        
        # get length of word
        while s[j] != '#':
            j += 1
        length = int(s[i:j])

        i = j + 1       # word start index
        j = i + length  # word end index
        
        res.append(s[i:j])
        i = j

    return res

    # Time:  O(n)
    # Space: O(n)

strs = ["neet","code","love","you"]
s = encode(strs)
print(s)
print(decode(s))