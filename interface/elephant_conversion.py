try:
    from elephant.conversion import binarize
    # from elephant.conversion import binarize
    # import elephant.conversion as ec
except ImportError:
    print "Error"


__author__ = 'lphan'


class Elephant_sub(object):
    '''Sub Interface to call the main functions conversion in layer core

    '''
    def __init__(self):
        pass

    @staticmethod
    def conversion_binarize(spiketrain, sampling_rate=None, t_start=None,
                            t_stop=None, return_times=None):
        result = binarize(spiketrain, sampling_rate, t_start, t_stop,
                          return_times)
        # print result
        return result
