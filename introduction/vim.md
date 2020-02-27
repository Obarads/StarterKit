# VIM
## About
慣れたら強いと思うエディッター。

## Problems
### ファイルをまたぐと50行までしかコピーが保存されない
対応策: https://teratail.com/questions/2053  
情報は~/.viminfoファイルに保存される、保存行数は指定することができる。
.vimrcファイルにset viminfo='20,\"1000とか書く。

## 参考になるもの
- https://qiita.com/lranran/items/3658fb8e8261bdb9adba
- https://qiita.com/ahiruman5/items/4f3c845500c172a02935
- https://qiita.com/colorrabbit/items/755cfbb0e97d48280775
- https://qiita.com/Fendo181/items/8a5545cd7550bd9a3c91


## .vimrc
### .vimrcの注意点
本資料ではVim-Plugを使用しているため、先に~/.vim/plugged/を作成しなくてはいけない。  
また、nerdtreeも使用しているため、nerdtreeのgithubからインストールすること。

### .vimrcの中身
```bash
set viminfo='20,\"1000 " コピー内容の増加

set encoding=utf-8
scriptencoding utf-8

set fileencoding=utf-8 " 保存時の文字コード
set fileencodings=ucs-boms,utf-8,euc-jp,cp932 " 読み込み時の文字コードの自動判別. 左側が優先される
set fileformats=unix,dos,mac " 改行コードの自動判別. 左側が優先される
set ambiwidth=double " □や○文字が崩れる問題を解決

set expandtab " タブ入力を複数の空白入力に置き換える
set tabstop=4 " 画面上でタブ文字が占める幅
set softtabstop=4 " 連続した空白に対してタブキーやバックスペースキーでカーソルが動く幅
set autoindent " 改行時に前の行のインデントを継続する
set smartindent " 改行時に前の行の構文をチェックし次の行のインデントを増減する
set shiftwidth=4 " smartindentで増減する幅

set incsearch " インクリメンタルサーチ. １文字入力毎に検索を行う
set ignorecase " 検索パターンに大文字小文字を区別しない
set smartcase " 検索パターンに大文字を含んでいたら大文字小文字を区別する
set hlsearch " 検索結果をハイライト

nnoremap <silent><Esc><Esc> :<C-u>set nohlsearch!<CR>

set whichwrap=b,s,h,l,<,>,[,],~ " カーソルの左右移動で行末から次の行の行頭への移動が可能になる
set number " 行番号を表示
set cursorline " カーソルラインをハイライト

" 行が折り返し表示されていた場合、行単位ではなく表示行単位でカーソルを移動する
nnoremap j gj
nnoremap k gk
nnoremap <down> gj
nnoremap <up> gk

" バックスペースキーの有効化
set backspace=indent,eol,start

set showmatch " 括弧の対応関係を一瞬表示する
source $VIMRUNTIME/macros/matchit.vim " Vimの「%」を拡張する

set wildmenu " コマンドモードの補完
set history=5000 " 保存するコマンド履歴の数

if has('mouse')
    set mouse=a
    if has('mouse_sgr')
        set ttymouse=sgr
    elseif v:version > 703 || v:version is 703 && has('patch632')
        set ttymouse=sgr
    else
        set ttymouse=xterm2
    endif
endif

if &term =~ "xterm"
    let &t_SI .= "\e[?2004h"
    let &t_EI .= "\e[?2004l"
    let &pastetoggle = "\e[201~"

    function XTermPasteBegin(ret)
        set paste
        return a:ret
    endfunction

    inoremap <special> <expr> <Esc>[200~ XTermPasteBegin("")
endif

if has('vim_starting')
    "set nocompatible
endif

if !filereadable(expand('~/.vim/autoload/plug.vim'))
    if !executable("curl")
        echoerr "You have to install curl or first install vim-plug yourself!"
        execute "q!"
    endif
    echo "Installing Vim-Plug..."
    echo ""
    silent !\curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    let g:not_finish_vimplug = "yes"
    autocmd VimEnter * PlugInstall
endif

" plug用の拡張確認関数
" インストールするVimプラグインを以下に記述
" check the specified plugin is installed
function s:is_plugged(name)
    if exists('g:plugs') && has_key(g:plugs, a:name) && isdirectory(g:plugs[a:name].dir)
        return 1
    else
        return 0
    endif
endfunction

call plug#begin(expand('~/.vim/plugged'))
"----------------------------------------------------------
" ここに追加したいVimプラグインを記述する・・・・・・②
" Note: Plugへの引数は絶対に二重引用符を使うな、単引用符を使え。例: Plug 'XX/YY.vim' <OK Plug "XX/YY.vim" <NG
" カラースキームmolokai
Plug 'tomasr/molokai'
" ステータスラインの表示内容強化
Plug 'itchyny/lightline.vim'
" インデントの可視化
Plug 'Yggdroot/indentLine'
" 末尾の全角と半角の空白文字を赤くハイライト
Plug 'bronson/vim-trailing-whitespace'
if has('lua') " lua機能が有効になっている場合・・・・・・①
    " コードの自動補完
    Plug 'Shougo/neocomplete.vim'
    " スニペットの補完機能
    Plug 'Shougo/neosnippet'
    " スニペット集
    Plug 'Shougo/neosnippet-snippets'
endif

" 多機能セレクタ
Plug 'ctrlpvim/ctrlp.vim'
" CtrlPの拡張プラグイン. 関数検索
Plug 'tacahiroy/ctrlp-funky'
" CtrlPの拡張プラグイン. コマンド履歴検索
Plug 'suy/vim-ctrlp-commandline'
" 構文エラーチェック
Plug 'scrooloose/syntastic'
" フォルダーのツリー構造を表示
Plug 'scrooloose/nerdtree'
" pythonの拡張機能
Plug 'davidhalter/jedi-vim'
"Plug 'raimon49/reuirements.txt.vim',{'for':'requirements'}
"----------------------------------------------------------
call plug#end()

" ファイルタイプ別のVimプラグイン/インデントを有効にする
filetype plugin indent on

"----------------------------------------------------------
" molokaiの設定
"----------------------------------------------------------
if s:is_plugged('molokai') " molokaiがインストールされていれば
    colorscheme molokai " カラースキームにmolokaiを設定する
endif

set t_Co=256 " iTerm2など既に256色環境なら無くても良い
syntax enable " 構文に色を付ける

"----------------------------------------------------------
" ステータスラインの設定
"----------------------------------------------------------
set laststatus=2 " ステータスラインを常に表示
"set noshowmode " 下に-- ModeName --を表示させない 
set showcmd
set ruler
let g:lightline = {
            \ 'colorscheme': 'wombat',
            \ 'active': {
            \ 'left': [ ['mode', 'paste'], ['readonly', 'filepath', 'modified'] ]
            \ },
            \ 'component_function':{
            \ 'filepath': 'FilePath'
            \ }
            \ }

function! FilePath()
    if winwidth(0) > 90
        return expand("%:s")
    else
        return expand("%:t")
    endif
endfunction

"----------------------------------------------------------
" neocomplete・neosnippetの設定
"----------------------------------------------------------
if s:is_plugged('neocomplete.vim')
    " Vim起動時にneocompleteを有効にする
    let g:neocomplete#enable_at_startup = 1
    " smartcase有効化. 大文字が入力されるまで大文字小文字の区別を無視する
    let g:neocomplete#enable_smart_case = 1
    " 3文字以上の単語に対して補完を有効にする
    let g:neocomplete#min_keyword_length = 3
    " 区切り文字まで補完する
    let g:neocomplete#enable_auto_delimiter = 1
    " 1文字目の入力から補完のポップアップを表示
    let g:neocomplete#auto_completion_start_length = 1
    " バックスペースで補完のポップアップを閉じる
    inoremap <expr><BS> neocomplete#smart_close_popup()."<C-h>"

    " エンターキーで補完候補の確定. スニペットの展開もエンターキーで確定・・・・・・②
    imap <expr><CR> neosnippet#expandable() ? "<Plug>(neosnippet_expand_or_jump)" : pumvisible() ? "<C-y>" : "<CR>"
    " タブキーで補完候補の選択. スニペット内のジャンプもタブキーでジャンプ・・・・・・③
    imap <expr><TAB> pumvisible() ? "<C-n>" : neosnippet#jumpable() ? "<Plug>(neosnippet_expand_or_jump)" : "<TAB>"
endif

"----------------------------------------------------------
" CtrlPの設定
"----------------------------------------------------------
let g:ctrlp_match_window = 'order:ttb,min:20,max:20,results:100' " マッチウインドウの設定. 「下部に表示, 大きさ20行で固定, 検索結果100件」
let g:ctrlp_show_hidden = 1 " .(ドット)から始まるファイルも検索対象にする
let g:ctrlp_types = ['fil'] "ファイル検索のみ使用
let g:ctrlp_extensions = ['funky', 'commandline'] " CtrlPの拡張として「funky」と「commandline」を使用

" CtrlPCommandLineの有効化
command! CtrlPCommandLine call ctrlp#init(ctrlp#commandline#id())

" CtrlPFunkyの有効化
let g:ctrlp_funky_matchtype = 'path' 

"----------------------------------------------------------
" Syntasticの設定
"---------------------------------------------------------
" 構文エラー行に「>>」を表示
let g:syntastic_enable_signs = 1
" 他のVimプラグインと競合するのを防ぐ
let g:syntastic_always_populate_loc_list = 1
" 構文エラーリストを非表示
let g:syntastic_auto_loc_list = 0
" ファイルを開いた時に構文エラーチェックを実行する
let g:syntastic_check_on_open = 1
" 「:wq」で終了する時も構文エラーチェックする
let g:syntastic_check_on_wq = 1

" Javascript用. 構文エラーチェックにESLintを使用
let g:syntastic_javascript_checkers=['pylint']
" Javascript以外は構文エラーチェックをしない
let g:syntastic_mode_map = { 'mode': 'passive',
                           \ 'active_filetypes': ['python'],
                           \ 'passive_filetypes': [] }

"----------------------------------------------------------
"NERDTreeの設定
"---------------------------------------------------------
nnoremap <silent><C-e> :NERDTreeToggle<CR>
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
autocmd BufEnter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

"---------------------------------------------------------
" jedi-vim
"--------------------------------------------------------
let g:jedi#popup_on_dot = 0
let g:jedi#goto_assignments_command = "<leader>g"
let g:jedi#goto_definitions_command = "<leader>d"
let g:jedi#documentation_command = "K"
let g:jedi#usages_command = "<leader>n"
let g:jedi#rename_command = "<leader>r"
let g:jedi#show_call_signatures = "0"
let g:jedi#completions_command = "<C-Space>"
let g:jedi#smart_auto_mappings = 0
let g:jedi#force_py_version = 3
autocmd FileType python setlocal completeopt-=preview

```


