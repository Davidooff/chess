from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from check_is_whatching import is_watching
from pieces_logic import rook, queen, bishop, knight

dictionaryOfPices = {
}

browser = webdriver.Firefox()
browser.get('https://www.chess.com/play/computer')
youre_color = ''
# input("Press Enter to continue...")


def main():
    coordinates = browser.find_element(By.CLASS_NAME, "board")
    pieces = coordinates.find_elements(By.CLASS_NAME, "piece")

    def getCoordinates(pieces):
        tempDict = {}
        blackDict = {}
        whiteDict = {}
        for piece in pieces:
            # piece bp square-47 - exemple (4 - horizontal) (7 - vertical)
            temp = piece.get_attribute("class").split(" ")
            if temp[0] == 'element-pool':
                continue
            try:
                if temp[1][0] == "b":
                    blackDict[temp[2]] = temp[1][1]
                else:
                    whiteDict[temp[2]] = temp[1][1]
            except:
                print(temp)

        tempDict["black"] = blackDict
        tempDict["white"] = whiteDict
        return tempDict

    def isChanged(pieces):
        global dictionaryOfPices, youre_color
        compareDict = getCoordinates(pieces)

        if compareDict != dictionaryOfPices:
            dictionaryOfPices = compareDict
            return True
        else:
            return False

    def addHighlight(browser, x, y, color):
        data = 'var board1 = document.getElementsByClassName("board")[0]; '
        data += 'var el = document.createElement("div"); '
        data += 'el.className = "highlight square-' + \
            str(x) + str(y) + ' extra-highlight"; '
        data += 'el.style.opacity = "0.8"; '
        data += 'el.style.background = "' + color + '"; '
        data += 'board1.prepend(el); '
        browser.execute_script(data)

    def removeHighlights(browser):
        data = 'var elements = document.getElementsByClassName("extra-highlight"); '
        data += 'for (var i = 0; i < elements.length; i++) {'
        data += '    elements[i].parentNode.removeChild(elements[i]); }'
        browser.execute_script(data)

    while True:

        if isChanged(pieces):
            print('Changed')
            newHighlights = []
            removeHighlights(browser)
            list_of_colors_keys = list(dictionaryOfPices.keys())
            for color in list_of_colors_keys:
                list_of_keys = list(dictionaryOfPices[color].keys())
                for key in list_of_keys:
                    temp = key.split("-")
                    x = int(temp[1][0])
                    y = int(temp[1][1])
                    if dictionaryOfPices[color][key] == "r":
                        highlights = rook(x, y, color, dictionaryOfPices)
                        newHighlights.extend(highlights)
                    elif dictionaryOfPices[color][key] == "q":
                        highlights = queen(x, y, color, dictionaryOfPices)
                        newHighlights.extend(highlights)
                    elif dictionaryOfPices[color][key] == "b":
                        highlights = bishop(x, y, color, dictionaryOfPices)
                        newHighlights.extend(highlights)
                    elif dictionaryOfPices[color][key] == "n":
                        highlights = knight(x, y, color, dictionaryOfPices)
                        newHighlights.extend(highlights)
                for highlight in newHighlights:
                    if is_watching(highlight, color, dictionaryOfPices, youre_color) == False:
                        addHighlight(
                            browser, highlight['x'], highlight['y'], "red")
                        newHighlights.remove(highlight)
            for highlight in newHighlights:
                addHighlight(
                    browser, highlight['x'], highlight['y'], "yellow")
        sleep(0.5)


def setColor(color):
    global youre_color
    match color:
        case "w":
            youre_color = "white"
        case "b":
            youre_color = "black"
        case "":
            print(youre_color)
        case _:
            print("Invalid color")
            setColor(input("Enter yore color (w/b):"))


def getColor():
    global youre_color
    match youre_color:
        case "white":
            setColor(input("Enter yore color (W/b):"))
        case "black":
            setColor(input("Enter yore color (w/B):"))
        case _:
            setColor(input("Enter yore color (w/b):"))


getColor()
while True:
    try:
        main()
    except:
        print("Catch error")
        getColor()
