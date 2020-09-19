def findWinner(votes):
    d = {}
    for vote in votes:
        if vote in d:
            d[vote] += 1
        else:
            d[vote] = 1
    maxVotes = max(d.values())
    l = [x for x in d.keys() if d[x] == maxVotes]
    return sorted(l)[0]

a = ['john','johnny','jackie','johnny','john','jackie', 'jamie','jamie','john','johnny','jamie','johnny','john']
print findWinner(a)
