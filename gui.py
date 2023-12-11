import scrape_nba
import sort_data

import tkinter as tk
from tkinter import ttk


data_obj = sort_data.NBA_Data()
NUM_PLAYERS_TO_DISPLAY = 10

# MAIN WINDOW
root = tk.Tk()
root.title('NBA Leaders!')
root.geometry('1000x500')

content = ttk.Frame(root)
content.grid()
# content.columnconfigure(0, weight=1)

#
# STYLES
#

# FRAME STYLES

data_style = ttk.Style()
data_style.configure('data.TFrame', background='red')

options_style = ttk.Style()
options_style.configure('options.TFrame',background='#DCC7DC')

name_frame_style = ttk.Style()
name_frame_style.configure('name_frame.TFrame', background='#5FD5EA')

stats_frame_style = ttk.Style()
stats_frame_style.configure('stats_frame.TFrame', background='#5FEACF')



# INNER FRAMES
data_display_frame = ttk.Frame(content)
data_display_frame.grid(column=0, row=0, sticky='w')
data_display_frame.configure(style='data.TFrame')

options_frame = ttk.Frame(content)
options_frame.grid(column=4, row=0, sticky= 'e')
options_frame.configure(style='options.TFrame')


name_frame = ttk.Frame(data_display_frame)
name_frame.grid(column=0, row=0)
name_frame.configure(style='name_frame.TFrame')

stats_frame = ttk.Frame(data_display_frame)
stats_frame.grid(column=1, row=0)
stats_frame.configure(style='stats_frame.TFrame')

#
# WIDGETS
#

# PLAYER LABELS

player_label_list = []
for i in range(NUM_PLAYERS_TO_DISPLAY):
    player_label_list.append(ttk.Label(name_frame, text='Player '+ str(i+1), width=20))
    player_label_list[i].grid(row=i, column=0, padx=10, pady=10, sticky='w')



# STATS LABELS

points_label_list = []
for i in range(NUM_PLAYERS_TO_DISPLAY):
    points_label_list.append(ttk.Label(stats_frame, text='P' + str(i+1) + ' Pts', width=6))
    points_label_list[i].grid(row=i, padx=10, pady=10)

assists_label_list = []
for i in range(NUM_PLAYERS_TO_DISPLAY):
    assists_label_list.append(ttk.Label(stats_frame, text='P' + str(i+1) + ' Ast', width=6))
    assists_label_list[i].grid(row=i,column=1, padx=10, pady=10)

rebounds_label_list = []
for i in range(NUM_PLAYERS_TO_DISPLAY):
    rebounds_label_list.append(ttk.Label(stats_frame, text='P' + str(i+1) + ' Reb', width=6))
    rebounds_label_list[i].grid(row=i, column=3, padx=10, pady=10)


# COMBOBOX
games_choice = tk.StringVar()
games_selection = ttk.Combobox(options_frame,\
                                textvariable= games_choice,\
                                values=['Season Averages', 'Last Game'],\
                                state='readonly',justify='center', width=17)

games_selection.grid(row=0, column=4,sticky='e', padx=10, pady=10)
games_selection.current(0)


# 'SORT BY' LABEL AND RADIOBUTTONS
sort_by_label = ttk.Label(options_frame,text='Sort By...')
sort_by_label.grid(row=1,column=4,sticky='e', padx=10, pady=10)

sort_by_choice = tk.StringVar()

sort_by_points = ttk.Radiobutton(options_frame,text='Points', variable=sort_by_choice, state='selected')
sort_by_points.grid(row=2,column=4,sticky='e', padx=10, pady=10)

sort_by_assists = ttk.Radiobutton(options_frame,text='Assists', variable=sort_by_choice)
sort_by_assists.grid(row=3, column=4,sticky='e', padx=10, pady=10)

sort_by_rebounds = ttk.Radiobutton(options_frame,text='Rebounds', variable=sort_by_choice)
sort_by_rebounds.grid(row=4,column=4,sticky='e', padx=10, pady=10)


# 'LOAD DATA' BUTTON
load_data_button = ttk.Button(options_frame,text='Load Data')
load_data_button.grid(row = 5, column=4, sticky='e', padx=10, pady=10)


#
# EVENT HANDLERS
#


# BUTTON FUNC
def on_load_data_click():
    if data_obj.data.empty:
        data_obj.retrieve_data()  
        load_data_button.configure(text='Data Loaded')
    else:
        print('data already loaded')

load_data_button.configure(command=on_load_data_click)

# COMBOBOX FUNC
def show_games(event):
    choice = games_selection.get()
    if choice == 'Last Game':
        data_obj.show_lastgame_stats()
        update_players_display()
    elif choice == 'Season Averages':
        data_obj.show_season_stats()
        update_players_display()
        
games_selection.bind('<<ComboboxSelected>>', show_games)



# RADIOBUTTONS FUNC
def show_points_sorted():
    if not data_obj.data.empty:    
        data_obj.sort_points()
        update_players_display()
sort_by_points.configure(command=show_points_sorted)

def show_assists_sorted():
    if not data_obj.data.empty:
        data_obj.sort_assists()
        update_players_display()
sort_by_assists.configure(command=show_assists_sorted)

def show_rebounds_sorted():
    if not data_obj.data.empty:
        data_obj.sort_rebounds()
        update_players_display()
sort_by_rebounds.configure(command=show_rebounds_sorted)



#
# Display Functions
#

def update_players_display():
    for i in range(NUM_PLAYERS_TO_DISPLAY):
        name = data_obj.data.index[i]
        pts = data_obj.data['PTS'][name]
        ast = data_obj.data['AST'][name]
        reb = data_obj.data['REB'][name]

        player_label_list[i].configure(text=name)
        points_label_list[i].configure(text=pts)
        assists_label_list[i].configure(text=ast)
        rebounds_label_list[i].configure(text=reb)

    


root.mainloop()
