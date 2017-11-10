#!/usr/bin/env python

from tools import fstools
import os, sys
import textwrap
import argparse
import re

parser = argparse.ArgumentParser(description="""
Transform csv file into tab
""", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--csv', metavar = '<clarity_metadata.csv>',
required=True,
help="""CSV file to transform\n\n""")

parser.add_argument('--columns', type=int,
required=True, nargs='+',
help="""List of columns to parse, ex. 1 30 41\n\n""")

parser.add_argument('--out_prefix', metavar = '<STRING>',
default='metadata',
help="""output file prefix.  Default=metadata\n\n""")

parser._optionals.title = "Program Options"

args = parser.parse_args()


if __name__ == '__main__':
    csv = args.csv
    if not fstools.check_file(csv):
        print 'could not find {}'.format(csv)
        sys.exit(1)
    print 'parsing {}...'.format(csv)
    check = re.compile('^Project ID|^#', re.IGNORECASE)
    tab_out = open('{}.tab'.format(args.out_prefix), 'w')
    with open(csv) as fopen:
        for line in fopen:
            new_line = []
            line = line.rstrip()
	    fields = line.split(',')
            if check.match(line):
                header = []
                for c in args.columns:
                    try:
                        int(c)
                    except ValueError:
                        print 'columns must be integer not {}'.format(c)
                    name = fields[int(c)-1]
                    header.append(name)
                tab_out.write('#' + '\t'.join(header) + '\n')
                continue
            for c in args.columns:
                try:
                    int(c)
                except ValueError:
                    print 'columns must be integer not {}'.format(c)
                data = fields[int(c)-1]
                if not data:
                    data = 'unknown'
                new_line.append(data)
            tab_out.write('\t'.join(new_line) + '\n')
    tab_out.close()

