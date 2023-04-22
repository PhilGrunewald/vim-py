# Vim-Py

## 1. Introduction

Allows to break up a python script into blocks. Blocks are separated with

`#>`

Since the `#` renders the line as a comment, the script remains compatible to be run in any other environment.

`<S-ENTER>` opens the terminal in a split view to present the output of the current block.

All variables are stored ('shelved') and picked up when executing subsequent blocks.

The state of all stored variables can be inspected with this line:

`#<`

Any line starting with `>` (even if indented) gets converted into a print
statement. E.g.

  `>"bob"`

becomes

  print("bob")

after execution. This is just for laziness. It avoids having to type `print` and putting brackets around the statement (speaking like a disgruntled python2 user).

How it works
------------

On execution the python script file is processed using `vim.py`. A dot-file copy with the same name as the script and a leading `.` is created. This is the file that is executed with python. All lines outside the current block are commented out (except import statements and functions).

The variable storage is handled with the help of the `vimpy.py` script, which gets copied into the same folder, imported by the script's dot-file and afterwards hidden as a dot-file.


## 2. Key bindings

Normal mode
-----------

| Key         | Action            |
|-----------  |-------            |
|  `++`         | increment number, toggle 'True' and 'False'  |
|  `--`         | reverse of `++`   |
|  `<S-SPACE>`  | toggle comment  |
|  `<SPACE>`    | toggle folding  |
|  `<S-ENTER>`  | execute block   |
|  `<leader>k`  | look up help for word under cursor  |


Insert mode
-----------

| Key         | Action                       |
| ----------- | ------------                 |
| `//`          | comment (replaced with `#`)    |



## 3. Commands

| Command     | Action                       |
|-----------  |------------                  |
| *Help*        | open this file in split view |
| *Lint*        | run `Flake8` PEP8 checks       |


## 4. Revision history

| Date      | Ver.  | Author         | Updates               |
| ----      | ----- | ------         | --------              |
| 21 Apr 23 | v1.0  | Phil Grunewald | Plugin version        |
| 20 Feb 21 | v0.1  | Phil Grunewald | Initial version with  |

