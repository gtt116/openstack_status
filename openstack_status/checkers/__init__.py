import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'openstack_status.settings'
import time
from multiprocessing import pool as multiprocess_pool

from openstack_status.openstack.common import importutils
from openstack_status.checkers import base


def all_checkers():
    hehe = [
        'openstack_status.checkers.flavor_list.FlavorList',
        'openstack_status.checkers.instance_list.InstanceList',
        'openstack_status.checkers.instance_boot.InstanceBoot',
        'openstack_status.checkers.image_list.ImageList',
    ]
    return  hehe


def all_checker_names():
    names = []
    for c in all_checkers():
        names.append(importutils.import_class(c).name)
    return names


def main():
    timeout = 20
    sleep = 10

    while True:
        print "Start checker"

        async_results = []
        cocurrent = len(all_checkers())
        pool = multiprocess_pool.ThreadPool(cocurrent)
        for check in all_checkers():
            c = importutils.import_class(check)()
            print "Execute checker: %s" % c
            res = pool.apply_async(c.execute)
            async_results.append(res)

        results = []
        for res in async_results:
            ret = res.get(timeout)
            results.append(ret)

        base.update_aggregate(results)
        print "Sleep %s" % sleep
        time.sleep(sleep)


if __name__ == '__main__':
    main()
