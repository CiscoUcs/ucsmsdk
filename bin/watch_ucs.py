#!/usr/bin/env python

import argparse
import time

from ucsmsdk.utils.ucsguilaunch import ucs_gui_launch
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils.converttopython import convert_to_ucs_python

parser = argparse.ArgumentParser(
    description='Convert to Ucs Python.',
    prog="convert-to-python")
parser.add_argument(
    '--hostname',
    help="hostname/ip of the server",
    required=True)
parser.add_argument('--username', help="username", required=True)
parser.add_argument('--password', help="password", required=True)
args = parser.parse_args()
host, user, password = args.hostname, args.username, args.password


try:
    input = raw_input
except NameError:
    pass

try:
    handle = UcsHandle(host, user, password)
    handle.login()

    ucs_gui_launch(handle)

    time.sleep(5)
    print("================================================")
    print("Hit an Enter here AFTER the Java UI is up and running...")
    print("================================================")
    wait = input()
    convert_to_ucs_python()

except:
    handle.logout()
    raise

finally:
    handle.logout()
