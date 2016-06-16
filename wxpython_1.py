#! /usr/bin/env python
# -*- coding: utf-8 -*-


import wx
import time

class ClockWindow(wx.Window): 									#定義類別，傳入wx.window(為了顯示時間)
    def __init__(self, parent):									#此類別建構式
        wx.Window.__init__(self, parent)						#副元素建構式	
        self.Bind(wx.EVT_PAINT, self.OnPaint)					#將此類別物件代入OnPaint方法後，以wx.EVT_PAINT之方式執行
        self.timer = wx.Timer(self)								#創立self.timer物件
        self.Bind(wx.EVT_TIMER, self.OnTimer)					#將此類別物件代入OnTimer方法後，以wx.EVT_TIMER之方式執行
        self.timer.Start(1000)									#計時器開始(1000毫秒動一次)

    def Draw(self, dc):											#定義Draw函數
        t = time.localtime(time.time())							#宣告t=現在時間
        st = time.strftime("%H:%M:%S", t)						#以time.strftime方法,將t轉換為小時:分鐘:秒
        w, h = self.GetClientSize()								#創建緩存設備文字
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))	#設定背景為空
        dc.Clear()
        dc.SetFont(wx.Font(60, wx.DECORATIVE, wx.NORMAL, wx.BOLD))	#設定字體格式(大小,字體風格(wx.DECORATIVE, wx.DEFAULT,wx.MODERN, wx.ROMAN, wx.SCRIPT or wx.SWISS.)字體斜度(wx.NORMAL, wx.SLANT or wx.ITALIC.),字體粗細(wx.NORMAL, wx.LIGHT, or wx.BOLD))
        tw, th = dc.GetTextExtent(st)							#取得字串高度和寬度
        dc.DrawText(st, (w-tw)/2, (h)/2 - th/2)					#在規定矩陣裡寫入文字(文字,左右位置,高度位置)
        
    def OnTimer(self, evt):										#定義OnTimer函數
        dc = wx.BufferedDC(wx.ClientDC(self))					#建立dc變數
        self.Draw(dc)											#將dc代入Draw方法

    def OnPaint(self, evt):										#定義OnPaint函數
        dc = wx.BufferedPaintDC(self)							#建立dc變數
        self.Draw(dc)											#將dc代入Draw方法

class MyFrame(wx.Frame):														#建立視窗類別
    def __init__(self):															#建構式
        wx.Frame.__init__(self, None, title="wxpython小時鐘" ,size=(900,900))	#title為視窗名稱,size為視窗大小
        ClockWindow(self)														#建立ClockWindow物件，並將此視窗代入
        

app = wx.PySimpleApp()	#建立啟動應用程式
frm = MyFrame()			#產生自訂之視窗
frm.Show()				#顯示視窗
app.MainLoop()			#執行應用程式