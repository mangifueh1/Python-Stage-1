class fonts:
    @classmethod
    def regular(cls):
        return ('poppins', 40, 'normal')

    @classmethod
    def result(cls):
        return ('poppins', 15, 'normal')

    @classmethod
    def button(cls):
        return ('poppins', 12, 'bold')

    @classmethod
    def error(cls):
        return ('poppins', 23, 'normal')

    @classmethod
    def custom(cls, size, weight='normal'):
        return ('poppins', size, weight)
