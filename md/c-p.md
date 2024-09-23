- yy - yank (copy) a line
- 2yy - yank (copy) 2 lines
- yw - yank (copy) the characters of the word from the cursor position to the start of the next word
- yiw - yank (copy) word under the cursor
- yaw - yank (copy) word under the cursor and the space after or before it
- y$ or Y - yank (copy) to end of line
- p - put (paste) the clipboard after cursor
- P - put (paste) before cursor
- gp - put (paste) the clipboard after cursor and leave cursor after the new text
- gP - put (paste) before cursor and leave cursor after the new text
- dd - delete (cut) a line
- 2dd - delete (cut) 2 lines
- dw - delete (cut) the characters of the word from the cursor position to the start of the next word
- diw - delete (cut) word under the cursor
- daw - delete (cut) word under the cursor and the space after or before it
- :3,5d - delete lines starting from 3 to 5

**Tip** You can also use the following characters to specify the range:  
e.g.  

:.,$d - From the current line to the end of the file  
:.,1d - From the current line to the beginning of the file  
:10,1d - From the 10th line to the beginning of the file  

- :g/{pattern}/d - delete all lines containing pattern
- :g!/{pattern}/d - delete all lines not containing pattern
- d$ or D - delete (cut) to the end of the line
- x - delete (cut) character
