import os, argparse

class Main:

    def __init__(self):
        pass

    def compileLua(self):
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a LaTeX Beamer Presentation from the folder structure located in TopFolder.")
    parser.add_argument('--compileLuaLaTeX', dest="lualatex", action="store_true", help="Set this to compile the generated TeX File with LuaLaTeX")
    args = parser.parse_args()

    main = Main()

    if args.lualatex:
        main.compileLua()