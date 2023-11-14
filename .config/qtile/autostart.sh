#!/bin/sh

feh --bg-scale ~/Pictures/bg.jpg &
picom --experimental-backends &
autorandr -c &
flatpak run com.nextcloud.desktopclient.nextcloud &
dunst &
numlockx on &


emacs --daemon &
