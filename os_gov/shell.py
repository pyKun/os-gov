#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>

from utils import get_data

def do_get_cores(hint):
    if not hint:
        return []
    hint = str(hint)
    data = get_data()
    ret = []
    for mem_id in data:
        username = data[mem_id]["username"]
        fullname = data[mem_id]["fullname"]
        target_str = " ".join([username, fullname])
        if hint.lower() in target_str.lower():
            ret.append(data[mem_id])
    return ret
