#! /usr/bin/env python
# -*- coding: utf-8 -*-


import wx
import time

class ClockWindow(wx.Window): 									#�w�q���O�A�ǤJwx.window(���F��ܮɶ�)
    def __init__(self, parent):									#�����O�غc��
        wx.Window.__init__(self, parent)						#�Ƥ����غc��	
        self.Bind(wx.EVT_PAINT, self.OnPaint)					#�N�����O����N�JOnPaint��k��A�Hwx.EVT_PAINT���覡����
        self.timer = wx.Timer(self)								#�Х�self.timer����
        self.Bind(wx.EVT_TIMER, self.OnTimer)					#�N�����O����N�JOnTimer��k��A�Hwx.EVT_TIMER���覡����
        self.timer.Start(1000)									#�p�ɾ��}�l(1000�@��ʤ@��)

    def Draw(self, dc):											#�w�qDraw���
        t = time.localtime(time.time())							#�ŧit=�{�b�ɶ�
        st = time.strftime("%H:%M:%S", t)						#�Htime.strftime��k,�Nt�ഫ���p��:����:��
        w, h = self.GetClientSize()								#�Ыؽw�s�]�Ƥ�r
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))	#�]�w�I������
        dc.Clear()
        dc.SetFont(wx.Font(60, wx.DECORATIVE, wx.NORMAL, wx.BOLD))	#�]�w�r��榡(�j�p,�r�魷��(wx.DECORATIVE, wx.DEFAULT,wx.MODERN, wx.ROMAN, wx.SCRIPT or wx.SWISS.)�r��׫�(wx.NORMAL, wx.SLANT or wx.ITALIC.),�r��ʲ�(wx.NORMAL, wx.LIGHT, or wx.BOLD))
        tw, th = dc.GetTextExtent(st)							#���o�r�갪�שM�e��
        dc.DrawText(st, (w-tw)/2, (h)/2 - th/2)					#�b�W�w�x�}�̼g�J��r(��r,���k��m,���צ�m)
        
    def OnTimer(self, evt):										#�w�qOnTimer���
        dc = wx.BufferedDC(wx.ClientDC(self))					#�إ�dc�ܼ�
        self.Draw(dc)											#�Ndc�N�JDraw��k

    def OnPaint(self, evt):										#�w�qOnPaint���
        dc = wx.BufferedPaintDC(self)							#�إ�dc�ܼ�
        self.Draw(dc)											#�Ndc�N�JDraw��k

class MyFrame(wx.Frame):														#�إߵ������O
    def __init__(self):															#�غc��
        wx.Frame.__init__(self, None, title="wxpython�p����" ,size=(900,900))	#title�������W��,size�������j�p
        ClockWindow(self)														#�إ�ClockWindow����A�ñN�������N�J
        

app = wx.PySimpleApp()	#�إ߱Ұ����ε{��
frm = MyFrame()			#���ۭͦq������
frm.Show()				#��ܵ���
app.MainLoop()			#�������ε{��