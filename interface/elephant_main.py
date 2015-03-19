# **********************************************************************
#
# This is ElePhAnt interface to bind with other ElePhAnt core functions
# (core, analysis, test)
#
# **********************************************************************

import numpy as np
import neo
import quantities as pq
import json
import fnmatch
import sys
# import pprint
# import elephant as el
from elephant_conversion import Elephant_sub as ElephantConv
# from elephant_neo_tools import Elephant_sub as ElephantNeoTools
# from elephant_pandas_bridge import Elephant_sub as ElephantPandas
# from elephant_statistic import Elephant_sub as ElephantStatistic
from elephant_uptask import Elephant_sub as ElephantUp
from elephant_testing import Elephant_sub as ElephantTest
# from elephant_testing import Elephant_sub as ElephantTest


__author__ = 'lphan'
yes = ['Yes', 'Y', 'YES', 'yes', 'y']
no = ['No', 'N', 'NO', 'no', 'n']


# Reference: http://en.wikibooks.org/wiki/Python_Programming/Decorators
class Trace(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        funcname = self.f.__name__
        cache_file_name = 'logging/'+'cache_'+funcname+'.json'

        try:
            filename = open(cache_file_name)
            d = json.load(filename)
            # print d
            print "File exists, reading Info from file ... "
            # compare function_parameters
            # print len(args)
            res = Trace._check_content(d, *args)
            print "Result check = ", res
            if res:
                print "Same function with same parameters"
                # Show result of last time & ask whether to run again
                print d
                run = raw_input('Run function again (Y/N): ')
                if run in no:
                    # quit
                    print "Exiting program ..."
                    sys.exit(0)
                else:
                    print "Continue ..."
            else:
                run = raw_input("Different Parameters, overwrite log (Y/N): ")
                if run in no:
                    pass
                else:
                    print "Overwriting log-file ..."
                    count = d['Number_of_running'] + 1
                    data = {"funcname": "crosscorrelogram_task",
                            "Inputdata": args[0],
                            "Number_of_jobs": args[1],
                            "Job_id": args[2],
                            "Number_of_running": count}

                    # Write new json-file to save new function_parameters
                    with open(cache_file_name, 'w') as outfile:
                        json.dump(data, outfile)

            filename.close()
        except IOError:
            print 'File does not exist, creating new log file'
            if funcname is 'start_elephant_up_cc':
                count = 1
                data = {"funcname": "crosscorrelogram_task",
                        "Inputdata": args[0],
                        "Number_of_jobs": args[1],
                        "Job_id": args[2],
                        "Number_of_running": count}

                # Write new json-file to save new function_parameters
                with open(cache_file_name, 'w') as outfile:
                    json.dump(data, outfile)
            # TODO: add path of output_file after running function

        # After running function, count_var, path_of_output_file, time_date
        # will be added subsequently into cache.json
        return self.f(*args, **kwargs)

    @staticmethod
    def _check_content(data, *args):
        # print (data.items()[0], args[0])
        # print (data.items()[1], args[1])
        # print (data.items()[2], args[2])
        for k, v in data.items():
            if k == 'Inputdata':
                # print args[0]
                res1 = fnmatch.fnmatch(v, args[0])
                # print "Res1 = ", res1
            elif k == 'Number_of_jobs':
                # print "v & args[1] = ", v, args[1]
                # res2 = fnmatch.fnmatch(v, args[1])
                if v == args[1]:
                    res2 = True
                else:
                    res2 = False
                # print "type of args[1] = ", type(args[1])
                # print "type of k,v = ", type(v)
                # print "Res2 = ", type(res2)
            elif k == 'Job_id':
                # print "v & args[2] = ", v, args[2]
                # res3 = fnmatch.fnmatch(v, args[2])
                if v == args[2]:
                    res3 = True
                else:
                    res3 = False
                # print res3
            else:
                pass

        if res1 and res2 and res3:
            return True
        else:
            print res1, res2, res3
            return False


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

    # decorator for cache-info
    @staticmethod
    @Trace
    def start_elephant_up_cc(inputdata, number_of_jobs, job_id):
        # TODO: check all input parameters
        ElephantUp.elephant_up_cc(inputdata, number_of_jobs, job_id)

    @staticmethod
    def start_elephant_up_cv():
        # TODO: check all input parameters
        ElephantUp.elephant_up_cv()

    @staticmethod
    def testing_module():
        # ElephantTest.test_elephant_module()
        # ElephantTest.suite()
        ElephantTest.test_elephant_module()
