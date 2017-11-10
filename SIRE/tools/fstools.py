#!/usr/bin/env python

import time
import sys, os
import subprocess
import errno

USAGE='''
fstools.py
usage: {}
'''.format(sys.argv[0])

def check_file(file):
    b = False
    if not isinstance(file, basestring):
        raise ValueError('file must be a string')
    try:
        b = os.path.isfile(file) #get bool
    except OSError:
        raise
    if b:
        return True
    else:
        return False


def remove_file(file):
    try:
        os.remove(file)
    except OSError:
        raise


def load_text_file(file, return_list=False):
    lines = []
    with open(file) as stream:
        lines = stream.read()
    if return_list:
        return ''''''.join(lines).split('\n')
    text_obj = ''''''.join(lines).replace('\n', '<br/>')
    return text_obj


def check_directory(directory):
    b = False
    if not isinstance(directory, basestring):
        raise ValueError('directory must be a string')
    try:
        b = os.path.isdir(directory) #get bool
    except OSError:
        raise
    if b:
        return True
    else:
        return False


def create_directory(directory):
    if not isinstance(directory, basestring):
        raise ValueError('directory must be a string')
    try:
        os.mkdir(directory, 0755)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

 
def change_directory(directory):
    try:
        os.chdir(directory)
    except OSError:
        raise


def absolute_path(file):
    abs_path = ''
    try:
        abs_path = os.path.abspath(file)
    except OSError:
        raise
    if abs_path:
        return abs_path
    return False


def file_size(file):
    size = 0
    if absolute_path(file):
        try:
            size = os.path.getsize(absolute_path(file))
        except OSError:
            raise
        return size
    return False
    
