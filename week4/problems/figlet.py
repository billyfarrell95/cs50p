from pyfiglet import Figlet
import sys, random

figlet = Figlet()
figlet_fonts = figlet.getFonts()

def main():
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
        if font in figlet_fonts:
             message = input("Message: ")
             print_figlet(message, font)
        else:
             print("Invalid usage")
             sys.exit(1)
    elif len(sys.argv) == 1:
        font = random.choice(figlet_fonts)
        if font in figlet_fonts:
             message = input("Message: ")
             print_figlet(message, font)
        else:
             print("Invalid usage")
    else:
        print("Invalid usage")
        sys.exit(1)

def print_figlet(s, f):
        figlet.getFonts()
        figlet.setFont(font=f)
        print(figlet.renderText(s))

if __name__ == "__main__":
    main()