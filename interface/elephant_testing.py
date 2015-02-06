from elephant.test.test_conversion import binarize_TestCase as bi
from elephant.test.test_statistics import isi_TestCase as isi
from elephant.test.test_statistics import mean_firing_rate_TestCase as mea
from elephant.test.test_neo_tools import GetAllObjsTestCase as gao
# from elephant.test.test_module import module_testsuit as mt
import unittest


__author__ = 'lphan'


class Elephant_sub(object):
    '''Sub Interface to call the testing-functions

    '''
    def __init__(self):
        pass

    @staticmethod
    def test_conversion():
        bi.test_binarize_with_spiketrain_exact()

    @staticmethod
    def test_elephant_module():
        all_suite = unittest.TestSuite()
        all_suite.addTest(bi("test_binarize_with_spiketrain_exact"))
        all_suite.addTest(bi("test_binarize_with_spiketrain_exact_set_ends"))
        all_suite.addTest(bi("test_binarize_with_spiketrain_round"))
        all_suite.addTest(bi("test_binarize_with_quantities_exact"))
        all_suite.addTest(bi("test_binarize_with_quantities_exact_set_ends"))
        all_suite.addTest(bi("test_binarize_with_quantities_round_set_ends"))
        all_suite.addTest(bi("test_binarize_with_plain_array_exact"))
        all_suite.addTest(bi("test_binarize_with_plain_array_exact_set_ends"))
        all_suite.addTest(bi("test_binarize_no_time"))
        all_suite.addTest(bi("test_binariz_rate_with_plain_array_and_units_typeerror"))
        all_suite.addTest(bi("test_binariz_without_sampling_rate_valueerror"))
        all_suite.addTest(isi("test_isi_with_spiketrain"))
        all_suite.addTest(isi("test_isi_with_quantities_1d"))
        all_suite.addTest(isi("test_isi_with_plain_array_1d"))
        all_suite.addTest(isi("test_isi_with_plain_array_2d_default"))
        all_suite.addTest(isi("test_isi_with_plain_array_2d_0"))
        all_suite.addTest(isi("test_isi_with_plain_array_2d_1"))
        all_suite.addTest(mea("test_mean_firing_rate_with_spiketrain"))
        all_suite.addTest(mea("test_mean_firing_rate_with_spiketrain_set_ends"))
        all_suite.addTest(mea("test_mean_firing_rate_with_quantities_1d"))
        all_suite.addTest(mea("test_mean_firing_rate_with_quantities_1d_set_ends"))
        all_suite.addTest(mea("test_mean_firing_rate_with_plain_array_1d"))
        all_suite.addTest(gao("test__get_all_objs__float_valueerror"))
        all_suite.addTest(gao("test__get_all_objs__epoch_for_event_valueerror"))
        all_suite.addTest(gao("test__get_all_objs__empty_list"))
        all_suite.addTest(gao("test__get_all_objs__empty_nested_list"))
        all_suite.addTest(gao("test__get_all_objs__empty_dict"))
        all_suite.addTest(gao("test__get_all_objs__empty_nested_dict"))
        all_suite.addTest(gao("test__get_all_objs__empty_itert"))
        all_suite.addTest(gao("test__get_all_objs__empty_nested_iter"))
        all_suite.addTest(gao("test__get_all_objs__empty_nested_many"))
        all_suite.addTest(gao("test__get_all_objs__spiketrain"))
        all_suite.addTest(gao("test__get_all_objs__list_spiketrain"))
        all_suite.addTest(gao("test__get_all_objs__nested_list_epoch"))
        all_suite.addTest(gao("test__get_all_objs__iter_spiketrain"))
        print "Continue to add more testcases into testsuite ..."
        unittest.TextTestRunner(verbosity=2).run(all_suite)
