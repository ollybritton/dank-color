import sys, xmltodict, collections

black = 30
red = 31
green = 32
yellow = 33
blue = 34
pink = 35
cyan = 36
white = 37

normal = 0
bright = 1
dim = 2
italic = 3
underline = 4

def sub(string, color = white, background = black, type = bright, end = ""):
    # sub() -> Returns a string which has color information assoiated with it.
    return "\x1b[" + str(type) + ";" + str(color) + ";" + str(background + 10) + "m" + string + "\x1b[0m" + end

def xsub(string, end = ""):
    # EG: "<red>Hello</red>"
    result = ""

    if string[0] != "<":
        string = "<white>" + string + "</white>"

    string = "<body>" + string + "</body>"
    string = dict(xmltodict.parse(string)["body"])

    print(string)

    # for key in string:
    #     if type(string[key]) == collections.OrderedDict:
    #         string[key] = dict(string[key])

    for key in string:
        curr = string[key]
        print(curr)
        if type(curr) == str:
            string[key] = {"@type": "bright", "@background": "black", "#text": curr}

    for key in string:
        curr = string[key]
        str_color = key

        try:
            str_type = curr["@type"]

        except:
            str_type = "bright"


        try:
            str_background = curr["@background"]

        except:
            str_background = "black"


        if str_color == "black":
            str_color = black

        elif str_color == "red":
            str_color = red

        elif str_color == "green":
            str_color = green

        elif str_color == "yellow":
            str_color = yellow

        elif str_color == "blue":
            str_color = blue

        elif str_color == "pink":
            str_color = pink

        elif str_color == "cyan":
            str_color = cyan

        elif str_color == "white":
            str_color = white

        else:
            str_color = white


        if str_background == "black":
            str_background = black

        elif str_background == "red":
            str_background = red

        elif str_background == "green":
            str_background = green

        elif str_background == "yellow":
            str_background = yellow

        elif str_background == "blue":
            str_background = blue

        elif str_background == "pink":
            str_background = pink

        elif str_background == "cyan":
            str_background = cyan

        elif str_background == "white":
            str_background = white

        else:
            str_background = black


        if str_type == "normal":
            str_type = normal

        elif str_type == "bright":
            str_type = bright

        elif str_type == "dim":
            str_type = dim

        elif str_type == "italic":
            str_type = italic

        elif str_type == "underline":
            str_type = underline

        else:
            str_type = bright

        result += sub(curr["#text"], color = str_color, background = str_background, type = str_type)


    return result + end

def display(string, end = "\r\n"):
    print(xsub(string), end = end)

def xinput(start, typed, end = "\r\n"):
    # start -> starting text, eg: "How are you today >>>".
    # ---
    # typed -> an array containg formatting info for the input.
    #   # [color, background, type]
    # ---
    # end -> end text
    try:
        color = typed[0]

    except:
        color = white


    try:
        background = typed[1]

    except:
        background = black


    try:
        type = typed[2]

    except:
        type = bright


    if color == "black":
        color = black

    elif color == "red":
        color = red

    elif color == "green":
        color = green

    elif color == "yellow":
        color = yellow

    elif color == "blue":
        color = blue

    elif color == "pink":
        color = pink

    elif color == "cyan":
        color = cyan

    elif color == "white":
        color = white

    else:
        color = white


    if background == "black":
        background = black

    elif background == "red":
        background = red

    elif background == "green":
        background = green

    elif background == "yellow":
        background = yellow

    elif background == "blue":
        background = blue

    elif background == "pink":
        background = pink

    elif background == "cyan":
        background = cyan

    elif background == "white":
        background = white

    else:
        background = black


    if type == "normal":
        type = normal

    elif type == "bright":
        type = bright

    elif type == "dim":
        type = dim

    elif type == "italic":
        type = italic

    elif type == "underline":
        type = underline

    else:
        type = bright


    display(start, end = "")


    print("\x1b[" + str(type) + ";" + str(color) + ";" + str(background + 10) + "m", end = "")
    input()
    print("\x1b[0m", end = end)


# xinput("<red>Hey There!</red>", ["pink", "red", "italic"])
