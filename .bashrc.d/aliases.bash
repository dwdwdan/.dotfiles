alias ls="exa --icons -a"
alias lsa="exa --icons -la --git --time-style iso"

alias fort="fortune hitchhiker | cowsay | lolcat"

alias bashrc="source ~/.bashrc"
alias kc="~/scripts/keyboardConfig/script"

alias v="nvim"
alias e="/usr/local/bin/emacsclient -t"
alias E="emacsclient -c -n"
alias cb="flatpak run app.getclipboard.Clipboard"


alias g="git"
alias gs="git status"
alias ga="git add"
alias gc="git commit"

alias websync="rsync -rLK ~/website/ server:/var/www/personal"

alias q="exit"

alias activate="source env/bin/activate"

# Latex things
alias todos="grep 'TODO Warning' main.log"
alias todocnt="todos | wc -l"
