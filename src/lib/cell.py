class Cell:
    def __init__(self):
        self.bomb = False
        self.flag = False

    def setBomb(self):
        self.bomb = True

    def isBomb(self):
        return self.bomb

    def setFlag(b):
        assert isinstance(b, bool), "setFlag: Cell: b is not a boolean"
        self.flag = b

    def isFlagged():
        return self.flag
