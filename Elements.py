class Section:
    
    def __init__(self, name, number, path) -> None:
        self.name = name
        self.number = int(number)
        self.elements = []
        self.path = path

class Elements:

    def __init__(self) -> None:
        self.type = None
        self.pictures = []
        self.length = 0
        self.number = 0

    def addPicture(self, pathToPicture, number, title, caption=None):
        self.number = int(number)
        self.title = title
        self.type = "Pictures"
        self.pictures.append(
            Picture(pathToPicture, caption)
        )
        self.length += 1
    
    def addTeX(self, path, number, title):
        self.number = int(number)
        self.path = path
        self.title = title
        self.type = 'TeX'
        self.length = 1

class Picture():

    def __init__(self, path, caption) -> None:
        self.path = path
        if caption:
            self.caption = caption
        else:
            self.caption = None