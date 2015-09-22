#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>


from os_gov import gerrit
from copy import deepcopy
import json

g = gerrit.Gerrit()
all_groups = g.listGroups()
print "all groups: %s" % len(all_groups)
all_members = {}
iter_ = 0
for group in all_groups:
    if " " in group:
        continue
    members = g.listMembers(group)
    print "[%s] count %s in group %s" % (iter_, len(members), group)
    iter_ += 1
    #if iter_ >= 10: break
    for member in members:
        if member in all_members:
            all_members[member]["count"] += 1
            all_members[member]["resp"].append(group)
        else:
            all_members[member] = deepcopy(members[member])
            all_members[member]["count"] = 1
            all_members[member]["resp"] = [group]

json_data = json.dumps(all_members)
with open("./data.json", "w") as f:
    f.write(json_data)
