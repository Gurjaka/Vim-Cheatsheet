from options import *

def welcome():
    # Welcome box on top
    top, side, width = border()
    
    print(f'\n{top}\n{side}\n{txt('VIM CheatSheet')}\n{side}\n{top}')

def greet():
    '''
    Simple greet menu
    
    Simple greet with option menu, making easy to navigate.
    '''
    clear()

    welcome()

    top, side, width = border()

    items = [ 
        'Exit                             ',
        'Global                           ', 
        'Navigation (Cursor movement)     ', 
        'Insert (Inserting/appending text ', 
        'Editing                          ', 
        'Visual (Marking text/Visual mode)', 
        'VisualC (Visual Commands)        ', 
        'Registers                        ', 
        'MAP (Marks and Positions)        ', 
        'Macros                           ', 
        'C-p (Cut and paste)              ', 
        'Indent                           ', 
        'Exiting                          ', 
        'Search                           ', 
        'Search (Multiple files)          ', 
        'Tabs                             ', 
        'Files                            ', 
        'Diff                             ']

    print(f'{top}\n{side}\n{txt("Choose appropriate number")}\n{txt("")}')
    for i in range(len(items)):
        print(txt(f'{i}) {items[i]}'))
    print(f'{side}\n{top}')
    
    while True:
        try:
            opt = int(padding('Choose operation: '))
            if opt in range(0,len(items)):
                break
        except ValueError:
            continue 
    return opt

def readfile(name):
    clear()
    f = open(f'md/{name}.md', "r")
    top, side, width = border()

    for text in f:
        # Calculate stuff
        text_length = len(text)
        total_padding = (width - text_length - 2)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
      
        print(f'{" " * left_padding}{text}{" " * right_padding}')
    padding("Type anything to go back: ")

while True:
    match greet():
        case 0:
            clear()
            quit()
        case 1:
            readfile('global')
        case 2:
            readfile('navigation')
        case 3:
            readfile('insert')
        case 4:
            readfile('editing')
        case 5:
            readfile('visual')
        case 6:
            readfile('visualc')
        case 7:
            readfile('registers')
        case 8:
            readfile('map')
        case 9:
            readfile('macros')
        case 10:
            readfile('c-p')
        case 11:
            readfile('indent')
        case 12:
            readfile('exiting')
        case 13:
            readfile('search')
        case 14:
            readfile('searchmf')
        case 15:
            readfile('tabs')
        case 16:
            readfile('files')
        case 17:
            readfile('diff')

