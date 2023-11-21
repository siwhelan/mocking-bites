
class Diary:
    def __init__(self, contents):
        if not isinstance(contents, str):
            raise TypeError("Type is not a string")
        else:
            self.contents = contents
            
            

    def read(self):
        return self.contents