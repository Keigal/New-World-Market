# Collects screenshots of market data in New World

# Packages required
import pyautogui
import time

# Config
moveTime = 0.1          # Putting very little effort into making program seem like a human
sleepTime = 2        # Gives time for data to load before taking screenshot
minTimeToSearch = 2     # Ensures that program gives time for page to load before saying it couldn't find screenshot

# Paths to images used by program
buy_image = 'resources/general/buy_image.png'
sell_image = 'resources/genera/sell_image.png'
resources_image = 'resources/categories/resources.png'
raw_resources_image = 'resources/subcategories/raw_resources.png'
woods_image = 'resources/subcategories/woods.png'
green_wood_image = 'resources/items/green_wood.png'

#############################################################################
# Collecting data from the buy menu

# Finds Buy tab of market
buy_tab_coords = pyautogui.locateOnScreen(buy_image, confidence=0.9)

# # Clicking on the Buy tab to ensure we're in the right place
# # double-click to ensure we are in the window
pyautogui.moveTo(buy_tab_coords[0], buy_tab_coords[1], moveTime)      # x, y, time to move
pyautogui.click(clicks=2, interval=0.07)                          # num of clicks, interval between

# # Locates and clicks on the resources button
resources_coords = pyautogui.locateOnScreen(resources_image, minSearchTime=minTimeToSearch, confidence=0.6)
pyautogui.moveTo(resources_coords[0], resources_coords[1], moveTime)
pyautogui.click() 

# # Selects raw resources on menu
raw_resources_coords = pyautogui.locateOnScreen(raw_resources_image, grayscale=True, minSearchTime=minTimeToSearch, confidence=0.9)
pyautogui.moveTo(raw_resources_coords[0], raw_resources_coords[1], moveTime)
pyautogui.click() 

# # Selects woods
woods_coords = pyautogui.locateOnScreen(woods_image, grayscale=True, minSearchTime=minTimeToSearch, confidence=0.9)
pyautogui.moveTo(woods_coords[0], woods_coords[1], moveTime)
pyautogui.click() 

# Selects green wood item
green_wood_coords = pyautogui.locateOnScreen(green_wood_image, grayscale=True, minSearchTime=minTimeToSearch, confidence=0.9)
pyautogui.moveTo(green_wood_coords[0], green_wood_coords[1], moveTime)
pyautogui.click() 

# Takes screenshot of shop page
time.sleep(sleepTime)
pyautogui.screenshot('cache/buy-orders/green_wood.png')


#############################################################################
# Collecting data from the sell menu

# Returns a box object if images is found
# sell_tab_coords = pyautogui.locateOnScreen(sell_image, confidence=0.9)

# # Moving to the sell tab and clicking
# pyautogui.moveTo(sell_tab_coords[0], sell_tab_coords[1], 0.25)      # x, y, time to move
# pyautogui.click(clicks=2, interval=0.07)                            # num of clicks, interval between
