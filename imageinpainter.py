import wx

class frameClass(wx.Frame):

    def __init__(self,parent,title):
        #create frame
        super(frameClass,self).__init__(parent,title=title)
        self.Centre()
        #display frame
        self.Show()

app=wx.App()
frameClass(None,"Image Inpainter")
app.MainLoop()
