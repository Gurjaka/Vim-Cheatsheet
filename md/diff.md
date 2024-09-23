- zf - manually define a fold up to motion
- zd - delete fold under the cursor
- za - toggle fold under the cursor
- zo - open fold under the cursor
- zc - close fold under the cursor
- zr - reduce (open) all folds by one level
- zm - fold more (close) all folds by one level
- zi - toggle folding functionality
- ]c - jump to start of next change
- [c - jump to start of previous change
- do or :diffg[et] - obtain (get) difference (from other buffer)
- dp or :diffpu[t] - put difference (to other buffer)
- :diffthis - make current window part of diff
- :dif[fupdate] - update differences
- :diffo[ff] - switch off diff mode for current window

**Tip** The commands for folding (e.g. za) operate on one level. To operate on all levels, use uppercase letters (e.g. zA).

**Tip** To view the differences of files, one can directly start Vim in diff mode by running vimdiff in a terminal. One can even set this as git difftool.
