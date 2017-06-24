import wx
import numpy as np
import cv2
from matplotlib import pyplot as plt
import imgProc


class frameClass(wx.Frame):

    def __init__(self,parent,title):

        #create frame
        super(frameClass,self).__init__(parent,title=title)
        self.parentGUI()
        self.Centre()
        wx.Size(1920,1080)

        self.SetBackgroundColour('white')

        #display frame
        self.Show()

    def parentGUI(self):
        menuBar=wx.MenuBar()
        fileButton=wx.Menu()

        #menu items
        openItem=fileButton.Append(wx.ID_OPEN,'Open Image\tCtrl+O')
        exitItem=fileButton.Append(wx.ID_EXIT,'Exit')

        menuBar.Append(fileButton,'File')

        self.SetMenuBar(menuBar)

        #bind functions to menu buttons
        self.Bind(wx.EVT_MENU,self.Quit,exitItem)
        self.Bind(wx.EVT_MENU,self.Open,openItem)

    def Quit(self,e):
        self.Close()

    #function to open up the image that is to be inpainted
    def Open(self,e):
        openFileDialog = wx.FileDialog(self, "Open", "", "",
                                       "Image files (*.jpg)|*.jpg",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        path = openFileDialog.GetPath()
        print (path)

        if path == path:
            self.SetBackgroundColour('white')

        image_file = path
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # image's upper left corner anchors at panel coordinates (0, 0)
        if bmp1.GetWidth() >1920 and bmp1.GetHeight() > 1080:
            InfoBox = wx.MessageDialog(None,
                                       'Sorry, your image is too Big',
                                       'Warning',
                                       wx.ICON_INFORMATION)
            InfoBox.ShowModal()
            InfoBox.Destroy()

        else:
            print ('success')
            self.bmp1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))

            OpenBitBox = wx.MessageDialog(None, 'Open Mask?','Question',wx.YES_NO)
            OpenBitBoxAnswer = OpenBitBox.ShowModal()
            OpenBitBox.Destroy()

            if OpenBitBoxAnswer == wx.ID_YES:
                self.Open_Mask(e)
                print ('Bitmap Saved')
                BitUploadText = wx.StaticText(self, -1, "Mask Uploaded", style=wx.ALIGN_LEFT)
                BitUploadText.SetForegroundColour('#ffcc33')
                font = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
                BitUploadText.SetFont(font)



    def Open_Mask(self,e):
        openFileDialog_bit = wx.FileDialog(self, "Open", "", "",
                                       "Image files (*.jpg)|*.jpg",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog_bit.ShowModal()
        path_bit = openFileDialog_bit.GetPath()
        print (path_bit)

        image_file_bit = path_bit
        bmp_bit = wx.Image(image_file_bit, wx.BITMAP_TYPE_ANY).ConvertToBitmap()





app=wx.App()
frameClass(None,"Image Inpainter")
processor=imgProc.imageProcessor()

img1=processor.structureImage()
img2=processor.textureImage()

completed = cv2.addWeighted(img1,0.95,img2,0.05,0)
cv2.imshow('completed',completed)

app.MainLoop()
