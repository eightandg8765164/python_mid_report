#! /usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import random
random.seed()#隨機數生產套件

class RandomImagePlacementWindow(wx.Window):#定義一個類別，需傳入一個wx.window物件(為了將圖片隨機放置於視窗中)
    def __init__(self, parent, image):						#定義此類別建構式方法
        wx.Window.__init__(self, parent)					#副元素建構式	
        self.photo = image.ConvertToBitmap()				#取得點陣圖

        # choose some random positions to draw the image at:
        self.positions = [(100,100)]						#設定初始位置
        for x in range(1000):									#range(x),x代表要產生的img數量
            x = random.randint(0, 1000)						#x , y為0~1000隨機數字
            y = random.randint(0, 1000)
            self.positions.append( (x,y) )					#將初始位置座標加上x,y	
            
        # Bind the Paint event
        self.Bind(wx.EVT_PAINT, self.OnPaint)				#將此類別物件代入OnPaint方法後，以wx.EVT_PAINT之方式執行


    def OnPaint(self, evt):									#定義onPaint函數
        # create dc
        dc = wx.PaintDC(self)	#Using wx.PaintDC within EVT_PAINT / it automatically sets the clipping area to the damaged area of the window. Attempts to draw outside this area do not appear.
        brush = wx.Brush("#2B2B2B") #可以直接使用色碼表
        dc.SetBackground(brush)		#設定背景顏色
        dc.Clear()

        # draw the image in random locations
        for x,y in self.positions:
            dc.DrawBitmap(self.photo, x, y, True) #將self.photo轉成點陣圖畫在x,y座標

        
class TestFrame(wx.Frame):										#視窗類別							
    def __init__(self):											#創立視窗物件
        wx.Frame.__init__(self, None, title="Super style",		#title為視窗名稱
                          size=(1200,700))						#size為視窗大小
        img = wx.Image("spider.png")							#利用wx.Image存取圖片檔案
        win = RandomImagePlacementWindow(self, img)				#將img丟入函數
        

app = wx.PySimpleApp()#建立啟動應用程式
frm = TestFrame()		#產生自訂之視窗
frm.Show()				#顯示視窗
app.MainLoop()			#執行應用程式