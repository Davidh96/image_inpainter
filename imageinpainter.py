import wx

class frameClass(wx.Frame):

    def __init__(self,parent,title):
        #create frame
        super(frameClass,self).__init__(parent,title=title)
        self.parentGUI()
        self.Centre()
        #display frame
        self.Show()



    def parentGUI(self):
        menuBar=wx.MenuBar()
        fileButton=wx.Menu()

        openItem=fileButton.Append(wx.ID_OPEN,'Open')
        exitItem=fileButton.Append(wx.ID_EXIT,'Exit')

        menuBar.Append(fileButton,'File')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU,self.Quit,exitItem)
        self.Bind(wx.EVT_MENU,self.Open,openItem)


    def Quit(self,e):
        self.Close()

    def Open(self,e):
        openFileDialog = wx.FileDialog(self, "Open", "", "",
                                       "Image files (*.png)|*.png",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        openFileDialog.GetPath()
        openFileDialog.Destroy()



app=wx.App()
frameClass(None,"Image Inpainter")
app.MainLoop()
