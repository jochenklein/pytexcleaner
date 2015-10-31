import os
import glob
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--root',
    help='Root directory of your LaTeX project',
    type=str)
args = parser.parse_args()

if args.root and not os.path.isdir(args.root):
    sys.exit("Error: directory '{0}' not found".format(args.root))

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
    '*.synctex.gz']  # file patterns to remove

counter = 0  # counts removed files


def remove(filepath):
    global counter
    try:
        os.remove(filepath)
        counter += 1
    except OSError:
        print "Failed to remove file '{0}'".format(filepath)

if not args.root:
    for pattern in file_patterns:
        for filepath in glob.glob(pattern):
            remove(filepath)
else:
    for dirpath, dirnames, filenames in os.walk(args.root):
        for pattern in file_patterns:
            for filepath in glob.glob(os.path.join(dirpath, pattern)):
                remove(filepath)

print u'\U0001F37B' + " Cheers! {0} file(s) removed.".format(counter)
