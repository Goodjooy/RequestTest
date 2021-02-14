from .design_frame import MainFrame

class AppMainFrame(MainFrame):
    """
    主入口
    """
    def __init__(self, parent):
        super().__init__(parent)
    


    def new_reuqest(self, event):
        pass

    def send_request(self, event):
        return super().send_request(event)

    def setting(self, event):
        return super().setting(event)

    