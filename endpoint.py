#!/usr/bin/env python
import json
import sys

def cnt(s):
    return len(s)

#string, list of string
def set_address(params):
    address = params["address"]
    dest = params["dest"]

#
def get_businesses(params):
    pass

#dict[str,int]
def get_scores(params):
    d = params["dict"]

#print "sup"

while True:
    try:
        r = raw_input()

        query = json.loads(r)
        qid = query["id"]
        name = query["name"]
        params = query["params"]

        response = {}
        response["id"] = qid
        if name == "cnt":
            response["result"] = cnt(params["str"])
        elif name == "set_address":
            response["result"] = set_address(params)
        elif name == "get_businesses":
            response["result"] = get_businesses(params)
        elif name == "get_scores":
            response["result"] = get_scores(params)

        print json.dumps(response)
        sys.stdout.flush()

    except EOFError:
        pass

