# **********************************************************************
#
# This is ElePhAnt interface to bind with other ElePhAnt core functions
# (core, analysis, test)
#
# **********************************************************************

import numpy as np
import neo
import quantities as pq
# import elephant as el
from elephant_conversion import Elephant_sub as ElephantConv
# from elephant_neo_tools import Elephant_sub as ElephantNeoTools
# from elephant_pandas_bridge import Elephant_sub as ElephantPandas
# from elephant_statistic import Elephant_sub as ElephantStatistic
from elephant_uptask import Elephant_sub as ElephantUp

yes = set(['Yes', 'Y', 'YES', 'yes'])
no = set(['No', 'N', 'NO', 'no'])


class Elephant_main(object):
    ''' Main Interface to bind all other sub interfaces
    '''

    def __init__(self):
        pass

    @staticmethod
    def _determine_list(l):
        if type(l) is list:
            return True
        else:
            return False

    @staticmethod
    def _check_type_value(value):
        """ Check whether input value is valid
            input valid should be list, or list of list
            [0.2, 0.4, 3] or [[2.4, 5.7],[6, 3, 7.9]]
        """
        if Elephant_main._determine_list(value):
            return value
        else:
            raise ValueError

    @staticmethod
    def _check_type_bool(value):
        """ Check whether input value is type(bool)
        """
        if value == 'True':
            return True
        elif value == 'False':
            return False
        else:
            return None

#     @staticmethod
#     def _check_type_quantities(value):
#         """ Check whether input value is Quantity
#         """
#         if value in yes:
#             # TODO: create Quantity scalar
#             return
#         elif value in no:
#             return value
#         else:
#             raise ValueError

    @staticmethod
    def _build_type(t_spiketrain, value):
        """ build valid type for spiketrain
            determine which type (numpy/ quantities/ neo) is spiketrain
        """
        if t_spiketrain == 'numpy':
            return np.array(value)
        elif t_spiketrain == 'quantities':
            # TODO: Quantity_Array get more parameters
            return pq.Quantity(np.array(value))
        elif t_spiketrain == 'neo':
            # TODO: neo get more parameters
            return neo.SpikeTrain(np.array(value))
        else:
            print "spiketrain", t_spiketrain
            raise ValueError

    @staticmethod
#    def start_elephant_conversion(spiketrain, value, t_sampling_rate=None,
#                                   sampling_rate=None, t_t_start=None,
#                                   t_start=None, t_t_stop=None, t_stop=None,
#                                   return_times=None):
    def start_elephant_conversion(t_spiketrain, value, sampling_rate=None,
                                  t_start=None, t_stop=None,
                                  return_times=None):
        """ get parameter from arguments and assign them to binarize function
        """
        v = Elephant_main._check_type_value(value)
        sp = Elephant_main._build_type(t_spiketrain, v)

        # check type return_times is bool
        b = Elephant_main._check_type_bool(return_times)
        result = ElephantConv.conversion_binarize(sp, sampling_rate, t_start,
                                                  t_stop, return_times=b)
        return result

    def start_elephant_neo_tools(self):
        pass

    def start_elephant_pandas_bridge(self):
        pass

    def start_elephant_statistic(self):
        """ get parameter from arguments and assign them to statistic function
        """
        pass

    @staticmethod
    def start_elephant_up_cc(inputdata, number_of_jobs, job_id):
        # TODO: check all input parameters
        ElephantUp.elephant_up_cc(inputdata, number_of_jobs, job_id)

    @staticmethod
    def start_elephant_up_cv():
        # TODO: check all input parameters
        ElephantUp.elephant_up_cv()
