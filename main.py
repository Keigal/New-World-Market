import os
import csv
from readPrices import readPrices
    
# Printing results to csv
with open('results/buy_orders.csv', mode='w') as buy_orders:

    order_writer = csv.writer(buy_orders, delimiter=',')

    # Rather than hardcoding items, we just read each screenshot in the buy-orders cache file
    for filename in os.listdir('cache/buy-orders'):

        # Specifying the whole item path to read
        itemPath = 'cache/buy-orders/' + filename

        # Dropping the file extension from name of item
        item = os.path.splitext(filename)[0]

        # Reading screenshot and writing results
        order_writer.writerow([item, readPrices(itemPath)])