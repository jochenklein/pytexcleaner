import os
import glob
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root', help='Root directory of your LaTeX files/documentation', type=str)
args = parser.parse_args()

if args.root and not os.path.isdir(args.root):
    sys.exit("Error: directory not found")

file_patterns = [
    '*.aux',
    '*.bbl',
    '*.blg',
    '*.lof',
    '*.log',
    '*.lol',
    '*.lot',
    '*.out',
    '*.toc',
    '*.glo',
    '*.idx',
    '*.ist',
    '*.acn',
    '*.acr',
    '*.alg',
    '*.dvi',
    '*.glg',
    '*.gls',
    '*.ilg',
    '*.ind',
    '*.maf',
    '*.mtc',
    '*.mtc1',
    '*.synctex.gz']  # files to remove

counter = 0  # counts removed files


def remove(filepath):
    global counter
    try:
        os.remove(filepath)
        counter += 1
    except OSError:
        print "Failed to remove %s" % filepath

if not args.root:
    for pattern in file_patterns:
        for filepath in glob.glob(pattern):
            remove(filepath)
else:
    for dirpath, dirnames, filenames in os.walk(args.root):
        for pattern in file_patterns:
            for filepath in glob.glob(os.path.join(dirpath, pattern)):
                remove(filepath)

print u'\U0001F37B' + " Cheers! %d file(s) removed." % counter
