import scrape_nba
import json
from pandas import DataFrame


class NBA_Data:

    def __init__(self):
        self.data = DataFrame(None)
        self.season_data = DataFrame(None)
        self.lastgame_data = DataFrame(None)

    def retrieve_data(self):
        self.season_data = scrape_nba.scrape()
        self.lastgame_data = scrape_nba.scrape(LAST_GAME=True)
        self.data = self.season_data

    def sort_points(self):
        self.data.sort_values(by='PTS',inplace=True, ascending=False)
    
    def sort_assists(self):
        self.data.sort_values(by='AST',inplace=True, ascending=False)
    
    def sort_rebounds(self):
        self.data.sort_values(by='REB',inplace=True, ascending=False)

    def show_season_stats(self):
        self.data = self.season_data

    def show_lastgame_stats(self):
        self.data = self.lastgame_data

    def printData(self):
        print(self.data)








# d = NBA_Data()
# d.retrieve_data()
# with open('dataframe.json', mode='w') as f:
#     f.write(d.data.to_json())


# datadict = {} 
# with open('dataframe.json', mode='r') as f:
#     datadict = json.load(f)
#     f.close()

# testo = DataFrame.from_dict(datadict)

# print(testo['AST']['Mikal Bridges'])
