import scrape_nba
import unused.old_sort_stats as old_sort_stats 

players = scrape_nba.get_players()
headers = scrape_nba.get_headers()

statDict = {}

def createKey():
    hNum = 0
    for h in headers:
        statDict[h] = hNum
        hNum+=1

def sortedByPoints():
    print("Top 5 Season Scorers:")
    for pNum in range(5):
        print(players[pNum][1] + " -- " + players[pNum][8])

def sortedByAssists():
    arr = old_sort_stats.sort(players, statDict['AST'])

    for pNum in range(5):
        print(arr[pNum][1] + " -- " + arr[pNum][statDict['AST']])

def displayMenu():
    createKey()
    sortedByPoints()

    choice = -1
    while True:
        print("Choices: ")
        print("1: sort by points")
        print("2: sort by assists")
        print("3: quit")
        choice = int(input("\nenter choice: "))
        
        if choice == 1:
            sortedByPoints()

        elif choice==2:
            sortedByAssists()

        elif choice==3:
            break






