# What is this
This is a vim colorscheme checker.  
↓Please watch the DEMO gif↓  

# Demo
![Demo](https://raw.githubusercontent.com/ts-26a/colors_check.vim/master/gif/ex.gif)

# Installing
With Vim-Plug:  
```
Plug 'ts-26a/colorscheck.vim', {'do': ':UpdateRemotePlugins'}
```
then `:PlugInstall`

With dein.vim:  
```
call dein#add('ts-26a/colorscheck.vim')
```
then `:call dein#install()` and `:UpdateRemotePlugins`  

# Requires
- `pip3 install pynvim neovim requests`
- `:echo has('python3')` is 1

# Commands

`:ColorsCheck <repository or file url> [coloes-name] [rtp]`  
Please see `:help ColorsCheck`  

`:ColorsCacheClean`  
Clean the caches.  
