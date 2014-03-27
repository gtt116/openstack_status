from openstack_status.checkers import opsclient
from openstack_status.checkers import base


class InstanceList(base.CheckerBase, opsclient.NovaMixin):
    name = 'Instance List'

    def _prepare(self):
        self.novaclient

    def _run(self):
        self.novaclient.servers.list()
