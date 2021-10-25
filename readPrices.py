# Provides function which takes in two images, and outputs a list of prices.
# Function takes in two file paths as strings, the needle then haystack.

# Using OpenCV template matching to find each individual market line
import cv2
import numpy as np
import pytesseract as tess
from PIL import Image as im

# Config
threshold = 0.95

# Offsets to line box up with order line
# Calculated by hand by finding coords of order boxes when found with open-cv and dash boxes, drawing it out, then subtracting differences.
x_offset = 555
y_offset = 32

def readPrices(haystack):

    # Initializing variables
    prices = []
    found_orders = []

    # Importing images
    haystack = cv2.imread(haystack)
    needle = cv2.imread('resources/general/dashes.png')
    order_img = cv2.imread('resources/general/order_green_wood.png')

    # Seartching for orders in market image
    result = cv2.matchTemplate(haystack, needle, cv2.TM_CCOEFF_NORMED)

    # Size of box to draw around matches
    w = order_img.shape[1]
    h = order_img.shape[0]

    # Drawing a box around all matching objects?
    yloc, xloc = np.where(result >= threshold)

    # Drawing box around each found location, also cropping found boxes and adding to found_orders array
    for (x, y) in zip(xloc, yloc):

        # Applying offset to coords
        x -= x_offset
        y -= y_offset
    
        # Specifying coords for each corner of box
        top_corner = (x, y)
        bottom_corner = (x+w, y+h)
        
        # Drawing box
        cv2.rectangle(haystack, top_corner, bottom_corner, (255,0,0), 2)

        # Extracting orders found in image
        found_orders.append(haystack[y:y+h, x:x+w])

    for order in found_orders:
    
        # Changing data type from array to PIL Image object
        img = im.fromarray(order)

        # Getting the size of the current object
        w, h = img.size

        # Upscaling the image at same aspect ratio to improve tesseract accuracy
        w *= 2
        h *= 2

        # Creating tuple that must be passed into resize function
        newsize = (w, h)

        # Resizing image using Bicubic upscaling
        # https://pillow.readthedocs.io/en/stable/handbook/concepts.html#PIL.Image.BICUBIC
        img = img.resize(newsize, resample=3)

        # Extracting text from upscaled image
        text_df = tess.image_to_data(img, output_type=tess.Output.DATAFRAME)
        
        # Extracting price from the dataframe
        # This may be a problematic solution, as it only gets the first value that's true. By limiting lower end we limit the range in which a false positive can appear.
        # As long as this is balanced to still be below where price consistently appears everything should work.
        price = text_df.loc[text_df['left'] > 810, ['text']]
        
        # Takes extracted price and converts from dataframe/string to float
        price = float(price.iat[0, 0])
        
        # Adding found price to list of prices
        prices.append(price)

        # Dropping any rows with a null value extracted
        text_df = text_df.dropna()

    # Dropping any nan values that got into prices list
    prices = [price for price in prices if price == price]

    return prices
