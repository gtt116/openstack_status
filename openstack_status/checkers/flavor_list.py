from openstack_status.checkers import opsclient
from openstack_status.checkers import base


class FlavorList(base.CheckerBase, opsclient.NovaMixin):
    name = 'Flavor List'

    def _prepare(self):
        self.novaclient

    def _run(self):
        self.novaclient.flavors.list()
