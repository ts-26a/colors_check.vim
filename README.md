# What is this
This is a vim colorscheme checker.  
↓Please watch the DEMO gif↓  

# Demo
![Demo](https://raw.githubusercontent.com/ts-26a/colors_check.vim/master/gif/ex.gif)

# Installing
```vim
set runtimepath+=~/.cache/colors_check
```
And

if you're using [Vim-Plug](https://github.com/junegunn/vim-plug):
```
Plug 'ts-26a/colorscheck.vim', {'do': ':UpdateRemotePlugins'}
```
then `:PlugInstall`

or if [dein.vim](https://github.com/Shougo/dein.vim):
```
call dein#add('ts-26a/colorscheck.vim')
```
then `:call dein#install()` and `:UpdateRemotePlugins`  

# Requires
- `pip3 install pynvim neovim requests`
- `:echo has('python3')` is 1

# Usage

`:ColorsCheck <repository or file url> [colors-name] [rtp]`  
Please see `:help ColorsCheck`  

`:ColorsCacheClean`  
Clean the caches.  
