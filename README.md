# os-gov
This is a python library to get and cache information from openstack governance

## Document

Quick-start::

    >>> from os_gov import shell
    >>> shell.do_get_cores("kong")
    >>> [{u'count': 3,
    >>> u'email': u'anlin.kong@gmail.com',
    >>> u'fullname': u'Lingxian Kong',
    >>> u'resp': [u'mistral-core', u'terracotta-core', u'terracotta-release'],
    >>> u'username': u'kong'}]
    
    >>> shell.do_get_companies("united")
    >>> [{u'count': 1,
    >>> u'email': u'xingchao@unitedstack.com',
    >>> u'fullname': u'Xingchao Yu',
    >>> u'resp': [u'puppet-manager-core'],
    >>> u'username': u'yuxcer'}]
