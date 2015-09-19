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

def parse_members(output):
    """ Example
id  username    full name   email
8122    cyril.roelandt.enovance Cyril Roelandt  cyril@redhat.com
1297    harlowja    Joshua Harlow   harlowja@yahoo-inc.com
1669    jdanjou Julien Danjou   julien@danjou.info
2813    sileht  Mehdi Abaakouk (sileht) sileht@redhat.com
9107    haypo   Victor Stinner  vstinner@redhat.com
7450    yassine.lamgarchal  Yassine Lamgarchal  yassine.lamgarchal@enovance.com
    """
    members = {}
    for line in output.splitlines():
        id_, username, name_email = line.split(None, 2)
        name, email = name_email.rsplit(None, 1)
        if id_ == "id":
            continue
        members[id_] = {"username": username,
                        "fullname": name,
                        "email": email,}

    return members
