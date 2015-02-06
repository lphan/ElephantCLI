#!/usr/bin/env python
# import commands
# import apt
# import os
import subprocess
import pip

__author__ = 'lphan'

# TODO:
# 1) Decision: what libaries to install
# 2) Install: all libraries with "Y"
#
# --------------- should be in 1-Script ---------------
# Script to check on the machine and install the software needed and
# all necessary dependencies (libs) needed for ElePhAnt
# Put all packages which will be installed into array
# packages = ['git', 'python-virtualenv', 'python-pip', 'htop']
libs = ['pyinstaller', 'numpy', 'scipy', 'quantities', 'neo', 'pandas', 'nose',
        'h5py', 'sphinx', 'numpydoc', 'task-sdk', 'cython', 'numexpr',
        'tables', 'matplotlib']

# print "------------------------------------------"
# if raw_input("Check whether all packages are installed (Y/N)") is 'Y':
#     for i in range(len(packages)):
#         devnull = open(os.devnull, "w")
#         stat = subprocess.call(["dpkg", "-s", packages[i]], stdout=devnull,
#                                stderr=subprocess.STDOUT)
#         devnull.close()
#         if stat != 0:
#             print "Package "+packages[i]+" not installed."
#             if raw_input("you want to install it (Y/N)") is 'Y':
#                 co = "sudo apt-get install "+packages[i]
#                 print co
#                 subprocess.call(co, shell=True)
#             else:
#                 print "Cancel install", packages[i]
#
#         else:
#             print "Package "+packages[i]+" already installed"
#             output = 'dpkg -s '+packages[i]+' | grep Version'
#             # print output
#             print commands.getoutput(output)

# generate and activate virtualenv
# workspace = raw_input("Input location of workspace to generate virtual env ")
# subprocess.call("cd "+workspace, shell=True)

# ---------------- Do it via commands ------------------

# if raw_input("you want to create new virtual environment (Y/N)") is 'Y':
#     env = raw_input("Input name of virtual environment ")
#     subprocess.call("virtualenv "+env, shell=True)
#     print "virtualenv need to be activated via '. "+env+"/bin/activate'"
#     # path_virlib = env+"/lib/python2.7/site-packages/"
#     # subprocess.call("ls "+path_virlib, shell=True)
# else:
#     pass

# subprocess.check_call(["source ","./virtest/bin/activate"])
# cmd = "source ./virtest/bin/activate"
# p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
#                     stderr=subprocess.PIPE)
# p.wait()
# subprocess.call("cd ..", shell=True)
# subprocess.call("source activate", shell=True)
# venv = ". "+env+"/bin/activate"
# subprocess.call(venv, shell=True)
# ------------------------------------------------------

# ---------------- should be in 2-script ---------------
# Try: setup-tools
# search all installed packaged using pip
install_lib = []
yes = ['Y', 'y', 'YES', 'yes']
no = ['N', 'n', 'NO', 'no']

if raw_input("Check all libraries at current environment (Y/N)") in yes:
    installed_listlib = sorted(["%s==%s" % (i.key, i.version) for i in
                                pip.get_installed_distributions()])
    print installed_listlib
    l = {}
    for i in range(len(installed_listlib)):
        key = installed_listlib[i].split('==')[0]
        value = installed_listlib[i].split('==')[1]
        # Push lib name and lib version into kind of list of dict
        l.update({key: value})
        # print "library name     = ", l[0]

    # Check if necessary library already stay in installed_listlib
    for i in range(len(libs)):
        if libs[i] in l:
            print "lib "+libs[i]+" already installed"
            print "... its version ", l[libs[i]]
        else:
            print "lib "+libs[i]+" not installed"
            if raw_input("you want to install (Y/N)") in yes:
                # put libs[i] into other install_list
                install_lib.append(libs[i])
    for lib in install_lib:
        if lib is 'task-sdk':
            print "Install task-sdk need access to VPN-EPFL"
            subprocess.call("pip install --index-url http://bbpsrv19.epfl.ch:9090/simple/ --pre "+lib, shell=True)
        else:
            subprocess.call("pip install "+lib, shell=True)

else:
    pass

# import PyInstaller as py
#
# if py.is_linux or py.is_unix is True:
#     print "OS Linux"
# elif py.is_win is True:
#     print "OS Win"
# else:
#     print "OS unknown"

# Create binary-executable file at ./bin/

# Save all meta input-infos to config.log or elephant.cfg
