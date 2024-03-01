#!/bin/sh

feh --bg-scale ~/Pictures/bg.jpg &
picom --experimental-backends &
autorandr -c &
dunst &
numlockx on &

flatpak run com.nextcloud.desktopclient.nextcloud &
blueman-applet &
nm-applet &


emacs --daemon &
