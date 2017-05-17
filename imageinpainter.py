import wx
import os

class frameClass(wx.Frame):

    __imagePath=""

    def __init__(self,parent,title):
        #create frame
        super(frameClass,self).__init__(parent,title=title)
        self.parentGUI()
        self.panelGUI()
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

    def panelGUI(self):
        panel = wx.Panel(self)
        img = wx.EmptyImage(240,240)
        wx.imageCtrl = wx.StaticBitmap(panel, wx.ID_ANY,
                                         wx.BitmapFromImage(img))


    def Quit(self,e):
        self.Close()

    def Open(self,e):
        openFileDialog = wx.FileDialog(self, "Open", "", "",
                                       "Image files (*.png)|*.png",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if openFileDialog.ShowModal() == wx.ID_OK:
            self.__imagePath=openFileDialog.GetPath()


        openFileDialog.Destroy()
        self.displayImg()

    def displayImg(self):
        filepath = self.__imagePath
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)

        wx.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        # panel.Refresh()


app=wx.App()
frameClass(None,"Image Inpainter")
app.MainLoop()
