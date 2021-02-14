
from wx.core import TreeCtrl


class Body(object):
    def __init__(self) -> None:
        super().__init__()

    def send_data(self) -> dict:
        raise NotImplementedError()

    def append_to_tree(root, tree: TreeCtrl):
        raise NotImplementedError()
