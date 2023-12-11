import scrape_nba
import gui


data = scrape_nba.scrape()

gui.launch_gui()

print(data)
