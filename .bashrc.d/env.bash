export EDITOR="nvim"
export PAGER="less"

# Start Bold
export LESS_TERMCAP_md=$(tput bold; tput setaf 2) # green
# Start Standout
export LESS_TERMCAP_so=$(tput bold; tput setaf 4) # blue
# End standout
export LESS_TERMCAP_se=$(tput rmso; tput sgr0)
# Start underline
export LESS_TERMCAP_us=$(tput smul; tput bold; tput setaf 1) # red
# end bold, standout, underline
export LESS_TERMCAP_me=$(tput sgr0)


export GROFF_NO_SGR=yes
