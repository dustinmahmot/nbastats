from setuptools import setup

setup(
    name='nbastats',
    version='0.1',
    install_requires=[
        "tkinter",
        "selenium",
        "ChromeDriverManager",
        "GeckoDriverManager", 
        "BeautifulSoup", 
        "pandas", 
        "json"
    ],
    description=  "Scrapes nba.com for player data, and displays the formatted data in a basic GUI",
    packages=["nbastats"]

)