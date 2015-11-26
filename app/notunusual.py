from datetime import datetime

class NotUnusual(object):
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
            if kwargs['name'] is not None:
                print "Your name is %s" % kwargs['name']

            for key, value in kwargs.iteritems():
                print key, value
