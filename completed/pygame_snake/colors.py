class Colors:
    green = (98, 191, 110)
    red = (214, 90, 90)
    yellow = (218, 223, 74)
    white = (255, 255, 255)

    @classmethod
    def get_all_colors(cls):
        return [cls.green, cls.red, cls.yellow, cls.white]
