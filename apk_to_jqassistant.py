#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys, os
import subprocess
from optparse import OptionParser

apk_file = ''
project_name = ''
cwd = os.path.dirname(os.path.abspath(__file__))
home = os.path.dirname(os.path.realpath(sys.argv[0]))
out_dir = home + '/out/'
rules_dir = home + '/rules/'


def call(cmd, **kwargs):
    print('Running: {0}'.format(' '.join(cmd)))
    return subprocess.call(cmd, **kwargs)

def print_header(text):
    block = "*********************************************"
    print(block)
    print('**' + text.center(len(block) - 4) + '**')
    print(block)

def dex2jar():
    print_header("Convert 'apk' to 'jar'")
    call([home + '/lib/dex2jar-2.1/d2j-dex2jar.sh', '-f', '-o', out_dir + project_name + '.jar', apk_file])
    print('Done')

def jqassistant_scan():
    print_header("Scan 'jar' with 'jqassistant'")
    call([home + '/lib/jqassistent/bin/jqassistant.sh', 'scan',  '-f', out_dir])
    print('Done')

def jqassistant_analyze():
    print_header("Analyze neo4j databse with 'jqassistant'")
    call([home + '/lib/jqassistent/bin/jqassistant.sh', 'analyze', '-r', rules_dir, '-reportDirectory', out_dir])
    print('Done')

def jqassistant_report():
    print_header("Creates a report useing 'jqassistant'")
    call([home + '/lib/jqassistent/bin/jqassistant.sh', 'report','-reportDirectory', out_dir])
    print('Done')

def jqassistant_server():
    print_header("Start neo4j server with 'jqassistant'")
    call([home + '/lib/jqassistent/bin/jqassistant.sh', 'server'])

def main():
    global apk_file, project_name, home, out_dir
    usage = "usage: %prog action file [options]"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    if len(args) >=1:

        args_action = args[0]
        if args_action == 'test':
            args_apk_file = args[1]

            if os.path.isfile(args_apk_file) and os.path.splitext(args_apk_file)[-1].lower() == '.apk':
                apk_file = args_apk_file
                project_name = os.path.splitext(os.path.basename(args_apk_file))[0].lower()
                dex2jar()
                jqassistant_scan()
                jqassistant_analyze()
                jqassistant_report()
            else:
                print("[ ERROR ] You must select a valid APK file!")
                exit(1)
                
        elif args_action == 'server':
            jqassistant_server()

        elif args_action == 'analyze':
            jqassistant_analyze()
            jqassistant_report()
            
        else:
            print("[ ERROR ] The first argument must be one of the actions: `test`, `server`,`report` or `analyze`")
    else:
        parser.print_help()


# Script start Here
if __name__ == "__main__":
    main()
