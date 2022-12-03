# Sort a string basis on count of characters
def frequencySort(s) -> str:
    count = collections.Counter(s)
    tup = sorted(count.items(), key = lambda x:x[1], reverse = True)
    res = []
    for char, cnt in tup:
        res.append(char*cnt)
    return ''.join(res)