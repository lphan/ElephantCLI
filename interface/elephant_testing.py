__author__ = 'lphan'


class Elephant_sub(object):
    '''Sub Interface to call the testing-functions

    '''
    def __init__(self):
        pass

    @staticmethod
    def test_suite_elephant():
        import elephant
        elephant.test()
