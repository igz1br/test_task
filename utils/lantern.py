from enum import Enum

class Color(Enum):
    white = 0
    red = 1
    green = 2
    blue = 3

class Lantern():
    status: bool = False
    color: Color = Color.white


    @staticmethod
    def on():
        Lantern.status = True

    @staticmethod
    def off():
        Lantern.status = False
    
    @staticmethod
    def change_color(new_color: float):
        new_color: int = int(new_color)
        Lantern.color = Color(new_color % 4)
        

    
            