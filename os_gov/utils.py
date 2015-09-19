#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>
import os


def _get_gerrit_usename():
    global_config = os.path.expanduser("~/.gitconfig")
    if not os.path.exists(global_config):
        return None

    with open(global_config, "r") as f:
        lines = f.readlines()
        finded = False
        username = None
        for l in lines:
            l = l.strip()
            if l.startswith("[gitreview]"):
                finded = True
                continue
            if finded and l.startswith("username"):
                username = l.split()[2]
                break
    return username

def get_gerrit_usename():
    try:
        return _get_gerrit_usename()
    except Exception as e:
        print e
