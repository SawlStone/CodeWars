def spin_words(sentence):
    res = []
    for i in sentence.split():
        if len(i) > 4:
            res.append(i[::-1])
        else:
            res.append(i)
    return ' '.join(res)