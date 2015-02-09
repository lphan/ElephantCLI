#!/usr/bin/env python

import argparse
# import sys
import json
# import elephant as el
import interface.elephant_main as ie


__author__ = 'lphan'
# ----------------------------------
#
#       Command Line Interface
#
# ----------------------------------

# def elephant_cli(args):
#     pass
#
#
type_spiketrain = set(['numpy', 'quantities', 'neo'])
data_type_elephant = []


def convert_type_float(t):
    if t is '':
        return None
    else:
        return float(t)


def install_lib(package):
    import pip
    installed_listlib = sorted(["%s" % (i.key) for i in
                                pip.get_installed_distributions()])
    if package in installed_listlib:
        return True
    else:
        return False


def elephant_cli_conversion():
    # Call main interface elephant
    # print "Input Data for value of binarize_function"
    # t_spiketrain = raw_input("choose one of following types for spiketrain\
    #                        [numpy/ quantities/ neo] ")
    t_spiketrain = "numpy"
    if t_spiketrain in type_spiketrain:
        pass
    else:
        raise ValueError

    # value = raw_input("Value for spiketrain, list or list of list: ")
    value = "[1.23, 0.3, 0.87, 0.56]"
    # sampling_rate = convert_type_float(raw_input("Sampling_rate value\
    #                                             (optional) default=None: "))
    sampling_rate = 100
    # t_start = convert_type_float(raw_input("t_start value (optional),\
    #                                       default=None: "))
    t_start = 0
    # t_stop = convert_type_float(raw_input("t_stop value (optional),\
    #                                      default=None: "))
    t_stop = 10.0
    return_times = raw_input("return_times bool-value (optional) True/ False ")

    # TODO: block access to Elephant_sub ie.ElephantConv.conversion_binarize
    result = ie.Elephant_main.start_elephant_conversion(t_spiketrain,
                                                        json.loads(value),
                                                        sampling_rate,
                                                        t_start, t_stop,
                                                        return_times)
    print result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command Line Interface')
    parser.add_argument("-s", "--show", action='store_true', help="List of all\
                        functional interfaces")
    parser.add_argument("-el", "--elephant", action='store_true',
                        help="ElePhAnt Interface")
    # parser.add_argument("-up", "--unifiedportal", action='store_true',
    #                     help="Unified Portal Interface")
    parser.add_argument("-te", "--testing", action='store_true',
                        help="Testing Interface")
    args = parser.parse_args()

    if args.show:
        print "-------------- List of Built-in functions"
        print "Elephant: crosscorrelogram_task"
        print "Elephant: elephant_cv_task"
        print "Elephant: conversion"
    elif args.elephant:
        print "-------------- ElePhAnt Interface"
        # print "First test: automatically calling function conversion ..."
        elephant_func = ['conversion', 'crosscorrelogram_task',
                         'elephant_cv_task']
        subcommand = raw_input('Input callable function: ')
        if subcommand in elephant_func:
            print subcommand
            if subcommand == 'conversion':
                elephant_cli_conversion()
            elif subcommand == 'crosscorrelogram_task':
                # TODO: call crosscorrelogram & elephant_cv in up
                inputdata = raw_input('Input path to Data: ')
                number_of_jobs = raw_input('Input number of jobs [1,200) ')
                job_id = raw_input('Input Job Id: ')
                ie.Elephant_main.start_elephant_up_cc(inputdata,
                                                      int(number_of_jobs),
                                                      int(job_id))
            elif subcommand == 'elephant_cv_task':
                ie.Elephant_main.start_elephant_up_cv()
    # elif args.unifiedportal:
    #     if install_lib('task-sdk'):
    #         print "Unified Portal interface"
    #         tasks = ['get_task', 'get_all_tasks', 'get_job', 'get_all_jobs']
    #         subcommand = raw_input('Input callable function:  ')
    #         if subcommand in tasks:
    #             from up.query_up import parse_args as pa
    #             if subcommand == 'get_task':
    #                 pa(subcommand)
    #             elif subcommand == 'get_all_tasks':
    #                 pa(subcommand)
    #             elif subcommand == 'get_job':
    #                 pa(subcommand)
    #             else:
    #                 print "call get_all_jobs func"
    #                 pa("get_all_jobs")
    #         else:
    #             print"No suitable function found, 'start.py -s' to get help"
    #     else:
    #         print "Need install library task-sdk to use U.P. functions"
    elif args.testing:
        # Run Testing Interface
        print "Running Testing Elephant-Module"
        ie.Elephant_main.testing_module()
    else:
        print "Input subcommand choices ['-s','-el', '-te']"

# Feature: Support analysis data from datapath as input ................
    # if param.function == 'binarize':
    #     elephant_cli_conversion()
    # elif param.function == 'typedata':
    #     # some code to test type of input data path
    #     data_path = raw_input("Input data path to file ")
    #     from neo.io import get_io
    #     try:
    #         x = get_io(data_path)
    #         print "File Format %s is supported by neo", type(x)
    #         print "All functions regarding are available to apply"
    #         # from neo.io import iolist
    #         # y = type(x) in iolist
    #         # if y:
    #         #     print type(x)
    #         # else:
    #         #    print "File-Format is not supported by neo"
    #     except IOError:
    #         print "IOError, File-Format is not supported by neo"

    # else:
    #     print "other functions are still being developed"

    # raw_input (optional) values
    # json.loads(value) has type list
