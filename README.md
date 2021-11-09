# ebay-data-scraper
 ebay-dl.py

## What does this ebay-dl.py file do?
This file scrapes the following data off of ebay item listings: name, price, status, shipping, free returns, and number sold. This is helpful for finding certain information in the listings of your choice.


## How do you run the `ebay-dl.py` file?

In order to run this file, you must have it downloaded and opened in the code editing software of your choice. Enter the following line into your terminal to return a .json file

`python3 ebay-dl.py "search term" --csv=False'

For example, I ran

'python3 ebay-dl.py "headphones" --csv=False'

to find the 'headphones.json' file in this repo.

To get this file to return CSV files, enter the fllowing into the terminal: 

`python3 ebay-dl.py "search term" --csv=True`

To get the coresponding headphones.csv file in this repo, I ran

'python3 ebay-dl.py "headphones" --csv=False'

If you are searching up items that are multiple words, make sure to surround the search terms in quotation mark.

Here is the [**link to the course project** ](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03).