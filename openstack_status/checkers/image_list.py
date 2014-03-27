from openstack_status.checkers import opsclient
from openstack_status.checkers import base


class ImageList(base.CheckerBase, opsclient.NovaMixin):
    name = 'Image List'

    def _prepare(self):
        self.novaclient

    def _run(self):
        self.novaclient.images.list()
