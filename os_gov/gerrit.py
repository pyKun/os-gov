#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>

from gerritlib import gerrit

class Gerrit(gerrit.Gerrit):
    def __init__(self, username):
        self.host = "review.openstack.org"
        self.user = username
        super(Gerrit, self).__init__(hostname=self.host, username=self.user)
