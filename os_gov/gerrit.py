#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>

from gerritlib import gerrit
from os_gov import utils

class Gerrit(gerrit.Gerrit):

    def __init__(self, username=None):
        self.host = "review.openstack.org"
        # TODO mv get_gerrit_usename to shell.py later
        self.user = username or utils.get_gerrit_usename()
        super(Gerrit, self).__init__(hostname=self.host, username=self.user)

    def listMembers(self, group, recursive=False):
        if recursive:
            cmd = "gerrit ls-members --recursive %s" % group
        else:
            cmd = "gerrit ls-members %s" % group
        out, err = self._ssh(cmd)
        if out.strip() == "Group not found or not visible":
            return None
        members = utils.parse_members(out)
        return members
