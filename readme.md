# dank-color
`dank-color` is a Python package for printing colors to the terminal. Many packages already exist with the same purpose, but have a weird syntax that isn't neat or easy to read. `dank-color` tries to end this by using an xml-like syntax.

For example, classical packages may have a syntax like this:

`print(package.colors.red + "Hello, " + package.colors.end + package.colors.blue + "Visitor." + package.colors.end)`

However, with `dank-color`, the same effect can be achieved in a much nicer looking way:

`display("<red>Hello, </red><blue>Visitor.</blue>")`

## Syntax
Within `dank-color`, an xml-like syntax is used to color strings. The tag color is just the name of the tag, so red text just becomes `<red></red>`. There are only two attributes that these tags can have, `type` & `background`. Surprisingly, `background` changes the background of the text, however `type` controls the display mode of the text. The display modes are listed below.

### Colors
- black
- red
- green
- yellow
- blue
- pink
- cyan
- white

### Display Modes, or `types`
- normal
- bright
- dim
- italic
- underline

### Examples
- Pink text with a blue background: `<pink background='blue'>TEXT</pink>`

- Italic red text atop a white background: `<red type="italic" background="white">TEXT</red>`

## Functions
In `dank-color`, there are 3 functions, `sub(), xsub(), display()`.

- `sub(string, color = white, background = black, type = bright, end = "")`
`sub()` is the main building block for the package. It simply generates a string containing the color, background and type information. For example, `sub("Hey", red, black, dim)` creates the string `\x1b[2;31;40mHey\x1b[0m`. Inside a terminal, printing this string tells the program that it should be red, have a black background and be dim.

- `xsub(string, end)`
`xsub()` is much like the `sub()` function, but this time it uses the xml syntax and then generates a string from that. For example, the result from the previous example can be achieved by doing `xsub("<red type='dim'>Hey</red>")` which too produces `\x1b[2;31;40mHey\x1b[0m`.

- `display(string, end)`
`display()` is just the print function, but using the xml syntax for colour. The literal code for it is `print(xsub(string), end = end)`.

## Features Wanted
- I don't know how to make packages, but if this was a pip package that would be awesome.
- I want a way to make tables, and pipe them to the console.
- Inputs that use xml-like parsing.

## Known Bugs
- Text is stripped automatically of trailing and leading whitespace. Something to do with how `xmltodict` parses it.
- Text not contained in a tag doesn't throw an error, but instead is pushed to the end of the message.
