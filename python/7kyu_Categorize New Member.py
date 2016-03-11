def openOrSenior(data):
    answer = []
    for i in data:
        if i[0] > 54 and i[1] > 7:  answer.append('Senior')
        else:                       answer.append('Open')
    return answer

print(openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]))