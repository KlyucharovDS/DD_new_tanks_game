# -*- coding: utf-8 -*-
# ----------------------variables----------------------
# colors
# BLACK = (0, 0, 0)
# GRAY = (127, 127, 127)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# CYAN = (0, 255, 255)
# MAGENTA = (255, 0, 255)

class Colors:
    """
    Все оттенки по группам
    """

    def __init__(self):
        self.RED_SHADES = RedShades()
        self.PINC_SHADES = PincShades()
        self.ORANGE_SHADES = OrangeShades()
        self.BLUE_SHADES = BlueShades()
        self.BROWN_SHADES = BrownShedes()
        self.GRAY_SHADES = GrayShades()
        self.GREEN_SHADES = GreenShades()
        self.MAIN_SHADES = MainShades()
        self.PURPLE_SHADES = PurpleShades()
        self.YELLOW_SHADES = YellowShades()


# КРАСНЫЕ ОТТЕНКИ
class RedShades:
    """
    КРАСНЫЕ ОТТЕНКИ
    """

    def __init__(self):
        self.INDIANRED = (205, 92, 92)
        self.LIGHTCORAL = (240, 128, 128)
        self.SALMON = (250, 128, 114)
        self.DARKSALMON = (233, 150, 122)
        self.LIGHTSALMON = (255, 160, 122)
        self.CRIMSON = (220, 20, 60)
        self.RED = (255, 0, 0)
        self.FIREBRICK = (178, 34, 34)
        self.DARKRED = (139, 0, 0)


class PincShades:
    """
    РОЗОВЫЕ ОТТЕНКИ
    """

    def __init__(self):
        self.PINK = (255, 192, 203)
        self.LIGHTPINK = (255, 182, 193)
        self.HOTPINK = (255, 105, 180)
        self.DEEPPINK = (255, 20, 147)
        self.MEDIUMVIOLETRED = (199, 21, 133)
        self.PALEVIOLETRED = (219, 112, 147)


class OrangeShades:
    """
    ОРАНЖЕВЫЕ ОТТЕНКИ
    """

    def __init__(self):
        self.LIGHTSALMON = (255, 160, 122)
        self.CORAL = (255, 127, 80)
        self.TOMATO = (255, 99, 71)
        self.ORANGERED = (255, 69, 0)
        self.DARKORANGE = (255, 140, 0)
        self.ORANGE = (255, 165, 0)


class YellowShades:
    """
    ЖЕЛТЫЕ
    """

    def __init__(self):
        self.GOLD = (255, 215, 0)
        self.YELLOW = (255, 255, 0)
        self.LIGHTYELLOW = (255, 255, 224)
        self.LEMONCHIFFON = (255, 250, 205)
        self.LIGHTGOLDENRODYELLOW = (250, 250, 210)
        self.PAPAYAWHIP = (255, 239, 213)
        self.MOCCASIN = (255, 228, 181)
        self.PEACHPUFF = (255, 218, 185)
        self.PALEGOLDENROD = (238, 232, 170)
        self.KHAKI = (240, 230, 140)
        self.DARKKHAKI = (189, 183, 107)


class PurpleShades:
    """
        ФИОЛЕТОВЫЕ
    """

    def __init__(self):
        self.AVENDER = (230, 230, 250)
        self.THISTLE = (216, 191, 216)
        self.PLUM = (221, 160, 221)
        self.VIOLET = (238, 130, 238)
        self.ORCHID = (218, 112, 214)
        self.FUCHSIA = (255, 0, 255)
        self.MAGENTA = (255, 0, 255)
        self.MEDIUMORCHID = (186, 85, 211)
        self.MEDIUMPURPLE = (147, 112, 219)
        self.BLUEVIOLET = (138, 43, 226)
        self.DARKVIOLET = (148, 0, 211)
        self.DARKORCHID = (153, 50, 204)
        self.DARKMAGENTA = (139, 0, 139)
        self.PURPLE = (128, 0, 128)
        self.INDIGO = (75, 0, 130)
        self.SLATEBLUE = (106, 90, 205)
        self.DARKSLATEBLUE = (72, 61, 139)


class BrownShedes:
    """
    КОРИЧНЕВЫЕ
    """

    def __init__(self):
        self.CORNSILK = (255, 248, 220)
        self.BLANCHEDALMOND = (255, 235, 205)
        self.BISQUE = (255, 228, 196)
        self.NAVAJOWHITE = (255, 222, 173)
        self.WHEAT = (245, 222, 179)
        self.BURLYWOOD = (222, 184, 135)
        self.TAN = (210, 180, 140)
        self.ROSYBROWN = (188, 143, 143)
        self.SANDYBROWN = (244, 164, 96)
        self.GOLDENROD = (218, 165, 32)
        self.DARKGOLDENROD = (184, 134, 11)
        self.PERU = (205, 133, 63)
        self.CHOCOLATE = (210, 105, 30)
        self.SADDLEBROWN = (139, 69, 19)
        self.SIENNA = (160, 82, 45)
        self.BROWN = (165, 42, 42)
        self.MAROON = (128, 0, 0)


class MainShades:
    """
    MAIN COLORS
    """

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.GRAY = (128, 128, 128)
        self.SILVER = (192, 192, 192)
        self.WHITE = (255, 255, 255)
        self.FUCHSIA = (255, 0, 255)
        self.PURPLE = (128, 0, 128)
        self.RED = (255, 0, 0)
        self.MAROON = (128, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.OLIVE = (128, 128, 0)
        self.LIME = (0, 255, 0)
        self.GREEN = (0, 128, 0)
        self.AQUA = (0, 255, 255)
        self.TEAL = (0, 128, 128)
        self.BLUE = (0, 0, 255)
        self.NAVY = (0, 0, 128)


class GreenShades:
    """
    ЗЕЛЕНЫЕ
    """

    def __init__(self):
        self.GREENYELLOW = (173, 255, 47)
        self.CHARTREUSE = (127, 255, 0)
        self.LAWNGREEN = (124, 252, 0)
        self.LIME = (0, 255, 0)
        self.LIMEGREEN = (50, 205, 50)
        self.PALEGREEN = (152, 251, 152)
        self.LIGHTGREEN = (144, 238, 144)
        self.MEDIUMSPRINGGREEN = (0, 250, 154)
        self.SPRINGGREEN = (0, 255, 127)
        self.MEDIUMSEAGREEN = (60, 179, 113)
        self.SEAGREEN = (46, 139, 87)
        self.FORESTGREEN = (34, 139, 34)
        self.GREEN = (0, 128, 0)
        self.DARKGREEN = (0, 100, 0)
        self.YELLOWGREEN = (154, 205, 50)
        self.OLIVEDRAB = (107, 142, 35)
        self.OLIVE = (128, 128, 0)
        self.DARKOLIVEGREEN = (85, 107, 47)
        self.MEDIUMAQUAMARINE = (102, 205, 170)
        self.DARKSEAGREEN = (143, 188, 143)
        self.LIGHTSEAGREEN = (32, 178, 170)
        self.DARKCYAN = (0, 139, 139)
        self.TEAL = (0, 128, 128)


class BlueShades:
    """
    СИНИЕ ТОНА
    """

    def __init__(self):
        self.AQUA = (0, 255, 255)
        self.CYAN = (0, 255, 255)
        self.LIGHTCYAN = (224, 255, 255)
        self.PALETURQUOISE = (175, 238, 238)
        self.AQUAMARINE = (127, 255, 212)
        self.TURQUOISE = (64, 224, 208)
        self.MEDIUMTURQUOISE = (72, 209, 204)
        self.DARKTURQUOISE = (0, 206, 209)
        self.CADETBLUE = (95, 158, 160)
        self.STEELBLUE = (70, 130, 180)
        self.LIGHTSTEELBLUE = (176, 196, 222)
        self.POWDERBLUE = (176, 224, 230)
        self.LIGHTBLUE = (173, 216, 230)
        self.SKYBLUE = (135, 206, 235)
        self.LIGHTSKYBLUE = (135, 206, 250)
        self.DEEPSKYBLUE = (0, 191, 255)
        self.DODGERBLUE = (30, 144, 255)
        self.CORNFLOWERBLUE = (100, 149, 237)
        self.MEDIUMSLATEBLUE = (123, 104, 238)
        self.ROYALBLUE = (65, 105, 225)
        self.BLUE = (0, 0, 255)
        self.MEDIUMBLUE = (0, 0, 205)
        self.DARKBLUE = (0, 0, 139)
        self.NAVY = (0, 0, 128)
        self.MIDNIGHTBLUE = (25, 25, 112)


class WhiteShades:
    """
    БЕЛЫЕ
    """

    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.SNOW = (255, 250, 250)
        self.HONEYDEW = (240, 255, 240)
        self.MINTCREAM = (245, 255, 250)
        self.AZURE = (240, 255, 255)
        self.ALICEBLUE = (240, 248, 255)
        self.GHOSTWHITE = (248, 248, 255)
        self.WHITESMOKE = (245, 245, 245)
        self.SEASHELL = (255, 245, 238)
        self.BEIGE = (245, 245, 220)
        self.OLDLACE = (253, 245, 230)
        self.FLORALWHITE = (255, 250, 240)
        self.IVORY = (255, 255, 240)
        self.ANTIQUEWHITE = (250, 235, 215)
        self.LINEN = (250, 240, 230)
        self.LAVENDERBLUSH = (255, 240, 245)
        self.MISTYROSE = (255, 228, 225)


class GrayShades:
    """
    СЕРЫЕ
    """

    def __init__(self):
        self.GAINSBORO = (220, 220, 220)
        self.LIGHTGREY = (211, 211, 211)
        self.LIGHTGRAY = (211, 211, 211)
        self.SILVER = (192, 192, 192)
        self.DARKGRAY = (169, 169, 169)
        self.DARKGREY = (169, 169, 169)
        self.GRAY = (128, 128, 128)
        self.GREY = (128, 128, 128)
        self.DIMGRAY = (105, 105, 105)
        self.DIMGREY = (105, 105, 105)
        self.LIGHTSLATEGRAY = (119, 136, 153)
        self.LIGHTSLATEGREY = (119, 136, 153)
        self.SLATEGRAY = (112, 128, 144)
        self.SLATEGREY = (112, 128, 144)
        self.DARKSLATEGRAY = (47, 79, 79)
        self.DARKSLATEGREY = (47, 79, 79)
        self.BLACK = (0, 0, 0)


# init coordinates & sizes
HEIGTH = 1024
WIDTH = 768
FPS = 60
COLORS = Colors()

# -----------------------------------------------------
