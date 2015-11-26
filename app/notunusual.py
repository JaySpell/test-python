from datetime import datetime

class NotUnusual(object):
    username = "Wrong"
    password = "dontdoit"
    def __init__(self, a_str):
        self.name = a_str

    @property
    def decorate_it(self):
        my_date = datetime()
        return my_date

    def see_me_cry(self, *args, **kwargs):
        for arg in args:
            print arg

        if kwargs is not None:
            for key, value in kwargs.iteritems():
                print key, value
