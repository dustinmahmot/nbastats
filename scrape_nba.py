from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.common import exceptions

from bs4 import BeautifulSoup

from pandas import DataFrame
import pandas



def clickLastGame(browser):
    season_segment_dropdown = Select(browser.find_element(By.CLASS_NAME,"SplitComboDropDown_select__G7wsG"))
    season_segment_dropdown.select_by_value('LastNGames=1')
    # for opt in season_segment_dropdown.options:
    #     print(opt.text)
    print('last game clicked')
    # need this after clickLastGame to get new stats
    browser.refresh()

def clickAllPlayers(browser):
    player_selection_dropdown = Select(browser.find_elements(By.CLASS_NAME, "DropDown_select__4pIg9")[-1])
    player_selection_dropdown.select_by_visible_text("All")
    print('all players clicked')
    


# accesses nba.com via selenium,
# returns pandas DataFrame containting player stats
def scrape(LAST_GAME=False,ALL_PLAYERS=True):
   
    url = "https://www.nba.com/stats/players/traditional?PerMode=PerGame&sort=PTS&dir=-1"

    print("loading website...")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    browser.get(url)
    browser.minimize_window()
    
    # else gets season averages
    if LAST_GAME:
        clickLastGame(browser)

    if ALL_PLAYERS:
        clickAllPlayers(browser)


    # get all html source code
    src = browser.page_source
    soup = BeautifulSoup(src, 'html.parser')


    #
    # HTML SCRAPING
    #

    # get table element
    statTable = soup.find(class_= 'Crom_table__p1iZz') 

    # separate head from body
    tHead = statTable.contents[0]  
    tBody = statTable.contents[1]



    # populate headers list (['Team', 'Age', etc.])
    headers_list = [] 
    for th in tHead.find_all('th')[2:30]:
        headers_list.append(th.text)
   

    # populate nested list of stats ([[ MIL, 29, ... ], [DEN, 29 ... ], etc.])
    # poplulate list of names to use as index
    rows_list = [] # stats
    names = []
    player_number=0
    for row in tBody.find_all('tr'):
        rows_list.append([])
        i=0
        for data in row.find_all('td')[1:]:
            if i==0:
                names.append(data.text)
            else:
                rows_list[player_number].append(data.text)
            i+=1
        player_number+=1


    #
    #   DATAFRAME WORK
    #

    # define dataframe
    data = DataFrame(data=rows_list,columns=headers_list, index=names)


    conv_to_int_list = ['Age','GP', 'W', 'L']
    conv_to_float_list = ['Min','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA',\
                     'FT%','OREB','DREB','REB','AST','TOV','STL','BLK','PF','FP', 'DD2','TD3']
    
    for key in conv_to_int_list:
        data[key] = data[key].astype(int)

    for key in conv_to_float_list:
        data[key] = data[key].astype(float)

    
    browser.close()
    return data



