#!/usr/bin/python3
'''
Module suare
'''


class Square():
    '''
    Class squares
    '''
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        '''Init method'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area square """
        return self.width * self.height

    def permiter_of_my_square(self):
        '''Perimeter'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''string'''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    '''Test Class'''
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
