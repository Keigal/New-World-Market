# Provides function which takes in two images, and outputs a list of prices.
# Function takes in two file paths as strings, the needle then haystack.

# Using OpenCV template matching to find each individual market line
import cv2
import numpy as np
import pytesseract as tess
from PIL import Image as im

# Config
threshold = 0.75

def readPrices(needle, haystack):

    # Initializing variables
    prices = []
    found_imgs = []

    # Importing images
    haystack = cv2.imread(haystack)
    needle = cv2.imread(needle)

    # Seartching for orders in market image

    # There are 6 comparison methods to choose from:
    # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
    # You can see the differences at a glance here:
    # https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
    result = cv2.matchTemplate(haystack, needle, cv2.TM_CCOEFF_NORMED)

    # Size of box to draw around matches
    w = needle.shape[1]
    h = needle.shape[0]

    # Drawing a box around all matching objects?
    yloc, xloc = np.where(result >= threshold)

    # Drawing box around each found location, also cropping found boxes and adding to found_imgs array
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(haystack, (x, y), (x + w, y + h), (0,255,255), 2)
        found_imgs.append(haystack[y:y+h, x:x+w])

    for img in found_imgs:
    
        # Changing data type from array to PIL Image object
        img = im.fromarray(img)

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
        price = text_df.loc[text_df['left'] == 817, ['text']]
        
        # Takes extracted price and converts from dataframe/string to float
        price = float(price.iat[0, 0])
        
        # Adding found price to list of prices
        prices.append(price)

        # Dropping any rows with a null value extracted
        text_df = text_df.dropna()

    return prices




