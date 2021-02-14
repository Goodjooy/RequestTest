from src.frames.main_frame import AppMainFrame
import wx
if __name__=="__main__":
    app=wx.App()

    frame=AppMainFrame(None)
    frame.Show()

    app.MainLoop()