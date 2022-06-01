####################
#                  #
# kazei's c64 demo #
#                  #
####################

from cmu_graphics import *

print("WELCOME TO KAZEI'S C64 DEMAKE\nTYPE \"?\" OR \"HELP\" TO SEE A LIST OF COMMANDS")
print("NO EXTERNAL TAPES EXIST AT THIS TIME")
print("HOWEVER A 3D GAME IS CURRENTLY IN THE WORKS, STAY TUNED FOR: ZERK!")


cDarkBlue = rgb(80,69,155)
cLightBlue = rgb(136,126,203)

app.background = cLightBlue
app.screen = Rect(40,40,320,320,fill=cDarkBlue)
app.screenBorder = Rect(0,0,400,400,border=cLightBlue,borderWidth=40,fill=None)
app.stepsPerSecond = 4

cursor = Rect(40,40,20,20,fill=cLightBlue,visible=False)
cursor.lineNumber = 0


rasterBars = Group()
color = 'black'

for i in range(0,400,20):
    if color == 'black':
        color = 'white'
        rasterBars.add(Rect(0, i, 400, 20, fill=color))
    elif color == 'white':
        color = 'black'
        rasterBars.add(Rect(0, i, 400, 20, fill=color))
rasterBars.visible = False


def cursorBlink():
    if cursor.visible == False:
        cursor.visible = True
    else:
        cursor.visible = False


#lineNumber = 0
# goes to beginning of line
def cursorReturn():
    cursor.centerX = 50
    cursor.centerY += 20
    cursor.lineNumber += 1
    
# goes to end of line    
def cursorRetract():
    cursor.centerX = 350
    cursor.centerY -= 20
    cursor.lineNumber -= 1
    
    

characters = Group(
    )
characters.lineValue = ""


def deleteChar():
    for char in characters.children:
        if cursor.hitsShape(char):
            characters.remove(char)
            #print("debug")


#lineCounter = Label(cursor.lineNumber,20,20,size=21,fill='white',bold=True,border='white',borderWidth=2)
   
skipKey = ['tab','escape','delete','up','down','left','right','insert','home',
'end','pageup','pagedown']   
   
def onKeyPress(key):
    if key in skipKey:
        pass
    elif key == 'space' and cursor.right != 360:
        cursor.centerX += 20
    elif key == 'space' and cursor.right == 360:
        cursorReturn()
        
    elif key == 'backspace' and cursor.left != 40:
        cursor.centerX -= 20
        # deletes characters
        deleteChar()
        characters.lineValue = characters.lineValue[:-1]
    elif key == 'backspace' and cursor.left == 40:
        # wraps around if at beginning of line
        cursorRetract()
        deleteChar()
        characters.lineValue = characters.lineValue[:-1]
    elif key == 'enter':
        
        
        #######################
        # COMMAND INTERPRETER #
        #######################   
        if characters.lineValue == "load":
            cursorReturn()
            for i in range(2):
                onKeyPress('space')
                
            onKeyPress("   LOADING...")
            rasterBars.visible = True
        
        elif characters.lineValue == "reset":
            
            characters.clear()
            
            cursor.centerX = 50
            cursor.centerY = 50
            bootMessage()
            cursorRetract()
            
        elif characters.lineValue == "?" or characters.lineValue == "help":
            cursorReturn()
            for i in range(6):
                onKeyPress('space')
            onKeyPress(" ? : SHOWS THIS SCREEN")
            cursorReturn()
            for i in range(4):
                onKeyPress('space')
            onKeyPress("     HELP : ALIAS FOR ?")
            cursorReturn()
            for i in range(6):
                onKeyPress('space')
            onKeyPress("  RESET : RESETS SCREEN")
            cursorReturn()
            for i in range(6):
                onKeyPress('space')
            onKeyPress("    LOAD : LOADS FROM TAPE")
            
        elif characters.lineValue != "":
            cursorReturn()
            for i in range(4):
                onKeyPress('space')
            onKeyPress("    ?SYNTAX     ERROR")
        #check previous line for commands
        #if command, execute. elif no command, syntax error. else, return.
        #reset characters.lineValue 
        characters.lineValue = ""
        cursorReturn()
        
        if cursor.centerY >= 350:
            characters.centerY -= 20
            app.screenBorder.toFront()
            cursor.centerY -= 20
    
    else:
        characters.lineValue += key
        #print(characters.lineValue)
        if cursor.left >= 358:
            cursorReturn()
        elif cursor.centerY >= 360:
            characters.centerY -= 20
            app.screenBorder.toFront()
            cursor.centerY -= 20
        
        
        characters.add(Label(key.upper(),cursor.left+10,cursor.centerY,size=21,fill='white',bold=True,border='white',borderWidth=2))
        #this cursor.centerX must be after the characters.add() because otherwise
        #the character will be where the cursor will be instead of where it
        # was when you typed it.
        cursor.centerX += 20
        if cursor.left >= 358:
            cursorReturn()
        
        
    #lineCounter.value = cursor.lineNumber
    pass

def bootMessage():
    for i in range(7):
        onKeyPress('space')
    onKeyPress("    ****  K BASIC V2  ****")
    cursorReturn()
    for i in range(7):
        onKeyPress('space')
    onKeyPress("   64K RAM  38911 BYTES FREE")
    for i in range(2):
        cursorReturn()
    onKeyPress("          READY.")
    characters.lineValue = ""
    onKeyPress('enter')


bootMessage()


def flashRaster():
    app.stepsPerSecond = 20
    for bar in rasterBars.children:
        if bar.fill == 'black':
            bar.fill = 'white'
        else:
            bar.fill = 'black'

    
app.steps = 0


def onStep():
    app.steps += 1
    
    cursorBlink()
    if rasterBars.visible:
        app.screen.toFront()
        characters.toFront()
        app.screenBorder.toBack()
        for char in characters.children:
            if char.centerY <= 40:
                characters.remove(char)
        
        flashRaster()



cmu_graphics.run()
    