#! /usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import random
random.seed()#�H���ƥͲ��M��

class RandomImagePlacementWindow(wx.Window):#�w�q�@�����O�A�ݶǤJ�@��wx.window����(���F�N�Ϥ��H����m�������)
    def __init__(self, parent, image):						#�w�q�����O�غc����k
        wx.Window.__init__(self, parent)					#�Ƥ����غc��	
        self.photo = image.ConvertToBitmap()				#���o�I�}��

        # choose some random positions to draw the image at:
        self.positions = [(100,100)]						#�]�w��l��m
        for x in range(1000):									#range(x),x�N��n���ͪ�img�ƶq
            x = random.randint(0, 1000)						#x , y��0~1000�H���Ʀr
            y = random.randint(0, 1000)
            self.positions.append( (x,y) )					#�N��l��m�y�Х[�Wx,y	
            
        # Bind the Paint event
        self.Bind(wx.EVT_PAINT, self.OnPaint)				#�N�����O����N�JOnPaint��k��A�Hwx.EVT_PAINT���覡����


    def OnPaint(self, evt):									#�w�qonPaint���
        # create dc
        dc = wx.PaintDC(self)	#Using wx.PaintDC within EVT_PAINT / it automatically sets the clipping area to the damaged area of the window. Attempts to draw outside this area do not appear.
        brush = wx.Brush("#2B2B2B") #�i�H�����ϥΦ�X��
        dc.SetBackground(brush)		#�]�w�I���C��
        dc.Clear()

        # draw the image in random locations
        for x,y in self.positions:
            dc.DrawBitmap(self.photo, x, y, True) #�Nself.photo�ন�I�}�ϵe�bx,y�y��

        
class TestFrame(wx.Frame):										#�������O							
    def __init__(self):											#�Хߵ�������
        wx.Frame.__init__(self, None, title="Super style",		#title�������W��
                          size=(1200,700))						#size�������j�p
        img = wx.Image("spider.png")							#�Q��wx.Image�s���Ϥ��ɮ�
        win = RandomImagePlacementWindow(self, img)				#�Nimg��J���
        

app = wx.PySimpleApp()#�إ߱Ұ����ε{��
frm = TestFrame()		#���ۭͦq������
frm.Show()				#��ܵ���
app.MainLoop()			#�������ε{��