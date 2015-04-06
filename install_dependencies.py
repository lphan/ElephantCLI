#!/usr/bin/env python
import subprocess
import pip

__author__ = 'lphan'

# ---------------------------------------------------------------------------
# Script to search and install all necessary dependencies (libs) needed
# for JElePhAnt
# 1) Decision: what libraries to install
# 2) Install: all libraries with "Y"
#
# Make sure that the following programs are already installed at your machine
# Prerequisites :
#       python-virtualenv
#       git
#       python-pip
# ---------------------------------------------------------------------------

# Put all packages which will be installed into array. If one package X depends
# package Y, put the package Y in order before package X in list
# New package: sklearn.cluster import dbscan
libs = ['pyinstaller', 'numpy', 'scipy', 'quantities', 'neo', 'pandas', 'nose',
        'sphinx', 'numpydoc', 'cython', 'numexpr', 'tables', 'h5py',
        'matplotlib', 'enum', 'lxml']

# search all installed packaged using pip
install_lib = []
yes = ['Y', 'y', 'YES', 'yes']
no = ['N', 'n', 'NO', 'no']

installed_listlib = sorted(["%s==%s" % (i.key, i.version) for i in
                            pip.get_installed_distributions()])
print "List of already installed packages with their version\n"
print installed_listlib
print "\n"
if raw_input("Choose 'Y' to continue the installation or 'N' to exit ") in yes:
    installed_lib = {}
    for i in range(len(installed_listlib)):
        key, value = installed_listlib[i].split('==')
        # Push lib name and lib version into list of dict
        installed_lib.update({key: value})
        # print "library name     = ", l[0]

    # Check if necessary library already stay in installed_listlib
    for i in range(len(libs)):
        if libs[i] in installed_lib:
            print "lib "+libs[i]+" already installed"
            print "... its version ", installed_lib[libs[i]]
            # TODO: update the current version
            # print "... latest version from Pypi is ..."
            # if version on Pypi is newer, asking for update ..."
            # print "... you want to update new version from pypi ..."
            # if Yes, then append it to install_lib
        else:
            print "lib "+libs[i]+" not installed"
            while True:
                x = raw_input("Choose 'Y' or 'N' to install the package: ")
                if x in yes or x in no:
                    break
            if x in yes:
                # put libs[i] into install_list
                install_lib.append(libs[i])
            else:
                pass
    for lib in install_lib:
        subprocess.call("pip install "+lib, shell=True)
else:
    print "Exit ..."
    pass
