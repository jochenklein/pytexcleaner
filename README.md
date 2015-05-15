# pytexcleaner
Removes unnecessary LaTeX files 

1. Getting started
------------------

There are two options starting `cleanup.py`. Copy the script into your root directory of your LaTeX files/documentation
and run

    $ python cleanup.py

The other option is to use the `--root` parameter to specify the root directory. To do so, run

    $ python cleanup.py --root=<your_root_directory>

The script will remove all unnecessary files (listed in the `file_patterns` list).