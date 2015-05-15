import os
import glob

project_directory = '/Users/jochen/tmp/'  # root directory of your LaTeX files/documentation.
file_patterns = ['*.aux', '*.bbl', '*.log']  # files to remove
counter = 0  # counts removed files


def remove(filepath):
    global counter
    try:
        os.remove(filepath)
        counter += 1
    except OSError:
        print "Failed to remove %s" % filepath


for dirpath, dirnames, filenames in os.walk(project_directory):
    for pattern in file_patterns:
        for filepath in glob.glob(os.path.join(dirpath, pattern)):
            print filepath

print u'\U0001F37B' + " Cheers! %d file(s) removed." % counter