import neo
import numpy as np
# import pandas as pd
import elephant.conversion as cv
import elephant.pandas_bridge as ep
import elephant.statistics as es
from timeit import Timer

count = 1000
test_array_1d = np.array([1.23, 0.3, 0.87, 0.56])
test_array_2d = np.array([[0.3, 0.56, 0.87, 1.23],
                          [0.02, 0.71, 1.82, 8.46],
                          [0.03, 0.14, 0.15, 0.92]])
test_array_1d = test_array_2d[0, :]


def perf_test_binarize_with_spiketrain():
    st = neo.SpikeTrain(test_array_1d, units='ms', t_stop=10.0,
                        sampling_rate=100)
    cv.binarize(st, return_times=True)


def perf_test_multiindex_from_dict():
    inds = {'test1': 6.5,
            'test2': 5,
            'test3': 'test'}
    # targ = pd.MultiIndex(levels=[[6.5], [5], ['test']],
    #                     labels=[[0], [0], [0]],
    #                     names=['test1', 'test2', 'test3'])
    ep._multiindex_from_dict(inds)


def perf_test_isi_with_spiketrain():
    st = neo.SpikeTrain(test_array_1d, units='ms', t_stop=10.0)
    es.isi(st)

statement1 = "perf_test_binarize_with_spiketrain()"
t1 = Timer(statement1, setup="from __main__ import\
           perf_test_binarize_with_spiketrain")
print "Perf_func binarize_with_spiketrain in 's': ", t1.timeit(number=count)

statement2 = "perf_test_multiindex_from_dict()"
t2 = Timer(statement2, setup="from __main__ import\
           perf_test_multiindex_from_dict")
print "Perf_func multiindex_from_dict in 's': ", t2.timeit(number=count)

statement3 = "perf_test_isi_with_spiketrain()"
t3 = Timer(statement3, setup="from __main__ import\
           perf_test_isi_with_spiketrain")
print "Perf_func isi_with_spiketrain in 's': ", t3.timeit(number=count)
