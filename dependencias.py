import os
import time
dependencias = [
                "base-devel", "rustup", "pacman-contrib", "bspwm", "polybar", "sxhkd",
			    "alacritty", "brightnessctl", "dunst", "rofi", "lsd",
			    "jq", "polkit-gnome", "git", "playerctl", "mpd",
			    "ncmpcpp", "geany", "ranger", "mpc", "picom",
			    "feh", "ueberzug", "maim", "pamixer", "libwebp", "xdg-user-dirs",
			    "webp-pixbuf-loader", "xorg-xprop", "xorg-xkill", "physlock", "papirus-icon-theme",
			    "ttf-jetbrains-mono", "ttf-jetbrains-mono-nerd", "ttf-terminus-nerd", "ttf-inconsolata", "ttf-joypixels",
			    "zsh", "zsh-autosuggestions", "zsh-history-substring-search", "zsh-syntax-highlighting"
                ]

def esta_instalada(paquete):
    exit_code = os.system(f"pacman -Qi {paquete} &> /dev/null")
    return exit_code == 0

print("Revisando dependencias")
for paquete in dependencias:
    if not esta_instalada(paquete):
        os.system(f"sudo pacman -S {paquete}")
        print("")
    else:
        print(f"{paquete} ya existe en el sistema")
        time.sleep(1)
time.sleep(3)