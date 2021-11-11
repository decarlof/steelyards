import os
import sys
import path
import json
import pandas as pd
from argparse import ArgumentParser

def import_xlsx(fname, nsheet=0):

    pre, ext = os.path.splitext(fname)
    jfname = pre + '.json'
    xls = pd.ExcelFile(fname)
    df = xls.parse(xls.sheet_names[nsheet])
    dic = df.to_dict()

    try:
        for key in dic['date']:
            dic['date'][key] = str(dic['date'][key])
    except:
    	pass

    with open(jfname, 'w') as fp:
        json.dump(dic, fp, indent=4, sort_keys=True)
    print('Saved data in: %s' % jfname)

def main():

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")

    args = parser.parse_args()

    import_xlsx(args.filename)

if __name__ == "__main__":
     main()