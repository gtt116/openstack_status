import time

from openstack_status.status import models


def update_aggregate(results):
    faileds = [res.failed for res in results]
    if all(faileds):
        status = 'red'
    elif any(faileds):
        status = 'yellow'
    else:
        status = 'green'

    print 'aggregate status: %s' % status
    x = models.CheckAggregation(
        status=status,
    )
    x.save()


class CheckerBase(object):
    name = 'CheckerBase'
    timeout = 2

    def __init__(self):
        self.start = None
        self.end = None
        self.elapse = 0
        self.exception = None
        self.failed = False
        self.status = 'init'
        self.path = ("%s.%s" %
                     (self.__class__.__module__, self.__class__.__name__))

    def _prepare(self):
        pass

    def execute(self):
        self.status = 'init'
        self.save_result()
        self._prepare()

        try:
            self.status = 'running'
            self.save_result()

            self.start = time.time()
            self._run()
        except Exception as ex:
            self.exception = ex
            self.failed = True
        else:
            self.failed = False

        self.end = time.time()
        self.elapse = self.end - self.start
        self.status = 'finished'
        return self.save_result()

    def save_result(self):
        x = models.CheckResult(check_name=self.name,
                               check_path=self.path,
                               elapse=self.elapse,
                               status=self.status,
                               failed=self.failed,
                               exception=self.exception)
        x.save()
        return x

    def _run(self):
        pass
