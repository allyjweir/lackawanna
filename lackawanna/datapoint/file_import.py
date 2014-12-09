__author__ = 'allyjweir'
import os
import errno
import textract


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_file_text(datapoint_file):
    make_sure_path_exists('temp')
    filename = 'temp/' + datapoint_file

    temp_file = open(filename, 'w+')

    return file_text
