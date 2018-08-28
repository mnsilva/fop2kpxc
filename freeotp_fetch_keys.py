#!/usr/bin/env python3

import base64
import json
import os, sys

print(sys.argv[1])
json_fd = open(sys.argv[1], 'r')
js = json.load(json_fd)
for obj in js['tokens']:
    token = obj['secret']
    secret = bytes((x + 256) & 255 for x in token)
    code = base64.b32encode(secret)

    label = '<unknown>'
    for l in [ 'labelAlt', 'issuerAlt' ]:
        if (l in obj):
            label = obj[l]
            break
    print( label + ': ' + code.decode() )
json_fd.close()
