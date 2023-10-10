# Generate-Beamer-Presentation

Generate a LaTeX Beamer Presentation from a hierarchic folder structure.

All elements must be placed in the folder **TopFolder**. You will find more information about the available elements in the **TopFolder**

## Requirements
[Python]() and [Poetry]() needs to be installed on the system.

## Usage
1. Download or clone the repo
2. run `poetry install` inside the repository folder
3. run `poetry run python Main.py` to generate a `.tex` file for the structure inside the TopFolder Folder
4. run `poetry run python Main.py --compileLuaLaTeX` to generate the `.pdf` after generating the `.tex`<br>
    **!! NOTE: this requires an installation of LuaLaTeX !!**
