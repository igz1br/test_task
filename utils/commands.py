from utils.lantern import Lantern

commands = {
    "ON": lambda x: Lantern.on(),
    "OFF": lambda x: Lantern.off(),
    "COLOR": lambda x: Lantern.change_color(x)
}


