from elephant.statistics import (isi, mean_firing_rate, fanofactor)

__author__ = 'lphan'


class Elephant_sub(object):
    ''' Sub Interface to bind all function in statistic
    '''

    def __init__(self):
        pass

    def statistic_fanofactor(self, spiketrains):
        """
            get parameter and call function in statistic
        """
        fanofactor(spiketrains)

    def statistic_isi(self, spiketrain, axis=-1):

        isi(spiketrain, axis)

    def statistic_mean_firing_rates(self, spiketrain, t_start=None,
                                    t_stop=None, axis=None):
        mean_firing_rate(spiketrain, t_start, t_stop, axis)
