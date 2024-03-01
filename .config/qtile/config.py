# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULA PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

import os
import subprocess


mod = "mod4"
terminal = guess_terminal()
runlauncher = "rofi -show drun -m \"primary\""
browser = "firefox"
powermenu = "rofi -show p -modi \"p:rofi-power-menu --choices=logout/suspend/reboot/shutdown --no-symbols\""

@hook.subscribe.startup_once
def start_once():
    autostart = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([autostart])

@hook.subscribe.screen_change
def autorandr():
    lazy.spawn("autorandr -c")

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "o", lazy.next_screen(), desc="Switch Screen"),

    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),


    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn(runlauncher), desc="Launch the runlauncher"),

    Key([mod], "m", lazy.spawn("Qminimize -m"), desc="Minimize focused window"),
    Key([mod, "shift"], "m", lazy.spawn("Qminimize -u"), desc="Unminimize window"),


    # Media Keys
    Key([],"XF86AudioRaiseVolume",lazy.spawn("pamixer -i 5"), desc="Increase volume"),
    Key([],"XF86AudioLowerVolume",lazy.spawn("pamixer -d 5"), desc="Decrease volume"),
    Key([],"XF86AudioMute",lazy.spawn("pamixer -t"), desc="Decrease volume"),
    Key([],"XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause"),
    Key([],"XF86AudioNext", lazy.spawn("playerctl next"), desc="Play/Pause"),
    Key([],"XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Play/Pause"),
    Key([],"XF86AudioStop", lazy.spawn("playerctl stop"), desc="Play/Pause"),


    Key([mod], "a", lazy.spawn("pavucontrol"), desc="Open Pavucontrol (audio panel)"),
    Key([mod], "f", lazy.spawn("nautilus"), desc="Open Nautilus (file browser)"),
    Key([mod], "e", lazy.spawn("emacsclient -c -n"), desc="Spawn Emacsclient"),
    Key([mod], "m", lazy.spawn(browser + " outlook.com"), desc="Open Outlook Web"),
    Key([mod], "c", lazy.spawn(browser + " canvas.bham.ac.uk"), desc="Open Canvas"),
    Key([mod], "o", lazy.spawn(browser + " office.com"), desc="Open Microsoft 365"),
    Key([mod], "g", lazy.spawn(browser + " https://www.geogebra.org/calculator"), desc="Open GeoGebra"),
    Key([mod, "shift"], "o", lazy.spawn(browser + " onenote.com"), desc="Open OneNote"),
    Key([mod, "shift"], "w", lazy.spawn(browser + " web.whatsapp.com"), desc="Open Whatsapp Web"),
    Key([mod, "shift"], "r", lazy.spawn(browser + " www.radioplayer.co.uk"), desc="Open Radioplayer"),
    Key([mod], "w", lazy.spawn(browser), desc="Spawn Browser"),
    Key([mod], "s", lazy.spawn("flatpak run com.spotify.Client"), desc="Spawn Spotify"),
    Key([mod], "p", lazy.spawn(powermenu), desc="Open Power Menu"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Move focused window to group {}".format(i.name),
            ),
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(margin=8),
    layout.Max(),
    # layout.Spiral(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def myGroupBox():
    return widget.GroupBox(
        this_current_screen_border='#a67dad',
        this_screen_border='#a67dad',
        highlight_method='line',
        disable_drag=True,
        rounded=False)

screens = [
    Screen(
        bottom=bar.Bar(
            [
                myGroupBox(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Mpd2(
                    status_format="{play_status} {title} ({artist})",
                ),
                widget.Spacer(),

                widget.OpenWeather(
                    location="Selly Oak,GB",
                    format='{icon}: {main_temp}°{units_temperature}',
                ),
                widget.Sep(),

                widget.Battery(
                    format='🔋: {percent:2.0%} {hour:d}:{min:02d}'
                ),
                widget.Sep(),
                widget.Systray(),
                widget.Sep(),
                widget.Clock(format="%Y-%m-%d %H:%M:%S"),
                #widget.QuickExit(),
            ],
            24,
            background='#262625'
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    # On the secondary screen I only want a groupbox
    Screen(bottom=bar.Bar(
            [
                myGroupBox(),
            ],
            24,
            background='#262625'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
