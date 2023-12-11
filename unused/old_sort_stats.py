NUM_TO_RANK = 5

def sort(players, num):
    sortedArr = [0]*5

    

    for x in range(5):
        max = -9999999
        for p in players:
            if int(p[num]) > max:
                max = int(p[num])
                maxPlayer = p
        sortedArr[x] = maxPlayer
        players.remove(maxPlayer)

    return sortedArr