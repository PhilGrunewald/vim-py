" Filetype plugin for executing python in block and other conveniences
" vim-py-kid plugin
" Author: Phil Grunewald
" Version: 1.0

let s:sfile = expand("<sfile>:p:h")

" ==============
"  Incrementing
" ==============

nnoremap ++ <C-a>
nnoremap -- <C-x>
nnoremap <C-a> :call Toggle('+')<CR>
nnoremap <C-x> :call Toggle('-')<CR>

function! Toggle(change)
    if (expand("<cword>") == "True")
        normal ciwFalse
    elseif (expand("<cword>") == "False")
        normal ciwTrue
    elseif (a:change == '+')
        normal ++
    elseif (a:change == '-')
        normal --
    endif
endfunction

" ==============
"  Commenting
" ==============

if exists("g:comment_char")
  let g:comment_char = "#"
  execute commentOn
endif

" ==============
" appearance
" ==============

" for quickfix on the right
set splitright

" ==============
"  Linting
" ==============

" PEP 8 the file
command! Lint :call Flake8()

" Help
command! Help :h vim-py

" ==============
"  Folding
" ==============

fu! PyFold()
    let foldSize = 1 + v:foldend - v:foldstart
    let padding     = repeat("▆", foldSize/4)
    let line = "   " . foldSize . " lines " . padding
    return line
endf

set foldtext=PyFold()
set foldmethod=indent
set foldcolumn=3
set foldlevel=5
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set foldignore-=#
set autoindent

" ==============
" Execute python
" ==============

compiler pyunit
set makeprg=python\ %
if has('nvim')
    command! Python     :call Process()
else
    command! Python		:make | vert copen | redraw!
endif

nnoremap <buffer><leader>p		:Python<CR>
nnoremap <buffer><S-ENTER>		:Python<CR>
nnoremap <buffer><leader>k		:call HelpMe("<cword>")<CR>
vmap <buffer><leader>k "*y:call HelpMe(@*)<CR>

function! Process()
    " run vim.py to create dot-file.py
    " copy vimpy.py for import
    " python execute dot-file
    " hide vimpy.py
    PWD
    silent! %s/^\(\s*\)>\(.*\)/\1print(\2)/
    silent! %s/^?\(.*\)/print(help(\1))/
    " silent! %s/^#>$/#>                                            <#/
    write
    let cmd = 'terminal python3 '.s:sfile.'/../python3/vim.py '.expand('%').' '.line('.').' && cp '.s:sfile.'/../python3/vimpy.py ./ && python3 .% && mv vimpy.py .vimpy.py'
    silent! bd! term*python " kill previous python terminals "
    vertical split
    execute cmd
    wincmd h
endfunction

function! HelpMe(helpStr)
    let cmd = 'terminal python3 '.s:sfile.'/../python3/vim.py '.expand('%').' '.a:helpStr.' && python3 .%'
    silent! bd! term*python " kill previous python terminals "
    vertical split
    execute cmd
    wincmd h
endfunction

command! XX echo s:sfile

