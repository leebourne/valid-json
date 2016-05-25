#!/usr/bin/python
'''
Created on Nov 10, 2015

@author: Lee Khan-Bourne

Quick script to validate that a JSON file is valid and optionally if it conforms to a schema

Usage:
    python validjson.py <file.json> [schema.json]

Returns:
    'True' if the file is valid
    'False: error message' if the file is not valid
    
'''

import sys
import json
import jsonschema

# Check that there is at least a file parameter specified
if len(sys.argv) < 2:
    print "Syntax: validjson.py <file.json> [schema.json]"
    quit()
try:
    jdata = open(sys.argv[1]).read()
    if len(sys.argv) < 3:                               # Is Schema specified?
        jschema = open(sys.argv[1]).read()              # No? - set it to file
    else:
        jschema = open(sys.argv[2]).read()				# Yes? - set to schema file
    try:
        jsonschema.validate(json.loads(jdata), json.loads(jschema))     # Validate File
        print "True"
    except jsonschema.ValidationError as e:				# Reject if not valid file
        print "False: ", e.message
    except jsonschema.SchemaError as e:					# Reject if not valid against Schema
        print "False: ", e
except Exception as e:						# Unexpected Error
    print "False: ", str(e)