#-------------------------------------------------------------------------------
# Name:        Computational APP
# Purpose:
#
# Author:      Preetam,Jeevan
#
# Created:     16-03-2014
# Copyright:   (c) preetam 2014
# Licence:     <your licence>

# ODE = string equations and runge kutta
# definite integral - romberg method, euler maclauren
# STrings- mass variation, free end, pulse
#-------------------------------------------------------------------------------
import wx
import final_string_ as stri
import variable_mass as mass
import final_string_free_end as free
import final_maclauren as maclauren
import runge_kutta_coupled_oscillator_plt as runge
import romberg

class WX_DOP(wx.Frame):

    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, 'Solver',#style=wx.NO_BORDER,
            size=(400,300))
        global panel
        '''
        image_file ='apple-equation2.jpg'
        bmp = wx.Image(image_file,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap=wx.StaticBitmap(self,-1,bmp,(0,0))
        str1 = "%s  %dx%d" % (image_file, bmp.GetWidth(), bmp.GetHeight())
        #parent.SetTitle(str1)
'''
        panel = wx.Panel(self,-1)
        #panel.SetBackgroundColour("wx.BLUE")
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        status= self.CreateStatusBar()
        extp = wx.Button(panel, -1, "Extapolation", pos= (75,50),size=(90,70))
        self.Bind(wx.EVT_BUTTON,self.Onextp, extp)

        intg = wx.Button(panel, -1, "Integration", pos= (75,150),size=(90,70))
        self.Bind(wx.EVT_BUTTON,self.Onintg, intg)

        diff = wx.Button(panel, -1, "Differentiation", pos= (225,50),size=(90,70))
        self.Bind(wx.EVT_BUTTON,self.Ondiff, diff)

        self.root = wx.Button(panel, -1,  "ODE's", pos= (225,150),size=(90,70))
        self.Bind(wx.EVT_BUTTON,self.Onroot, self.root)

    def Onextp(self, event):
        pass
        self.DestroyChildren()
        print "hello dis is extp"
        panel_extp=wx.Panel(self,-1)
        back_extp=wx.Button(panel_extp,wx.NewId(),"Back",pos=(90,150))
        #self.Bind(wx.EVT_BUTTON, self.__init__(frame,-1), romberg)


    def Onintg(self, event):
        self.DestroyChildren()
        panel_root=wx.Panel(self,-1)
        self.SetSize((400,301))
        vbox1=wx.BoxSizer(wx.VERTICAL)
        vbox2=wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel_vbox = wx.Panel(panel_root, -1, style = wx.DOUBLE_BORDER, size=(200,200))
        #text=wx.StaticText(panel_vbox,label='this is right vbox')
        vbox2.Add(panel_vbox, flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=10)
        #text=wx.StaticText(panel_vbox,label='this is right vbox')
        #vbox2.Add(text, flag=wx.RIGHT|wx.TOP|wx.BOTTOM)
        romberg=wx.Button(panel_root,label="Romberg", size=(100,30))
        self.Bind(wx.EVT_BUTTON, self.onromberg, romberg)
        euler=wx.Button(panel_root, -1, "Euler maclauren", size=(100,30))
        self.Bind(wx.EVT_BUTTON,self.Oneuler, euler)
        vbox1.Add(euler, flag=wx.LEFT|wx.TOP, border=10)
        vbox1.Add((-1, 50)) #gap b/w two buttons
        vbox1.Add(romberg, flag=wx.LEFT|wx.TOP, border=10)
        hbox.Add(vbox1, flag=wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        hbox.Add((50, -1))
        hbox.Add(vbox2, flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=10)
        panel_root.SetSizer(hbox)

    def Ondiff(self, event):
        self.DestroyChildren()
        panel_root=wx.Panel(self,-1)
        self.SetSize((400,301))
        vbox1=wx.BoxSizer(wx.VERTICAL)
        vbox2=wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel_vbox = wx.Panel(panel_root, -1, style = wx.DOUBLE_BORDER, size=(200,200))
        #text=wx.StaticText(panel_vbox,label='this is right vbox')
        vbox2.Add(panel_vbox, flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=10)
        #text=wx.StaticText(panel_vbox,label='this is right vbox')
        #vbox2.Add(text, flag=wx.RIGHT|wx.TOP|wx.BOTTOM)
        quad=wx.Button(panel_root,label="quadratic", size=(70,30))
        self.Bind(wx.EVT_ENTER_WINDOW, self.onquad, quad)
        string=wx.Button(panel_root, -1, "String", size=(70,30))
        vbox1.Add(string, flag=wx.LEFT|wx.TOP, border=10)
        vbox1.Add((-1, 50)) #gap b/w two buttons
        vbox1.Add(quad, flag=wx.LEFT|wx.TOP, border=10)
        hbox.Add(vbox1, flag=wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        hbox.Add((50, -1))
        hbox.Add(vbox2, flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=10)
        panel_root.SetSizer(hbox)

    def Onroot(self, event):
        self.DestroyChildren()
        panel_root=wx.Panel(self,-1,size=(400,350))
        vbox1=wx.BoxSizer(wx.VERTICAL)
        vbox2=wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel_vbox = wx.Panel(panel_root, -1, style = wx.DOUBLE_BORDER, size=(200, 200))#, pos=(40,300))
        #panel_vbox.SetDimensions(self,40,300,250,300)
        vbox2.Add(panel_vbox, flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=10)
        #text=wx.StaticText(panel_vbox,label='this is right vbox')
        #vbox2.Add(text, flag=wx.RIGHT|wx.TOP|wx.BOTTOM)
        mass=wx.Button(panel_root,label="mass variation", size=(100,30))
        self.Bind(wx.EVT_BUTTON,self.Onmass, mass)
        free=wx.Button(panel_root, -1, "free end", size=(100,30))
        self.Bind(wx.EVT_BUTTON,self.Onfree, free)
        string=wx.Button(panel_root, -1, "initial conditions", size=(100,30))
        self.Bind(wx.EVT_BUTTON,self.Onstring, string)
        kutta=wx.Button(panel_root, -1, "coupled oscillator", size=(100,30))
        self.Bind(wx.EVT_BUTTON,self.onkutta, kutta)
        vbox1.Add(string, flag=wx.LEFT|wx.TOP, border=10)
        vbox1.Add((-1, 25)) #gap b/w two buttons
        vbox1.Add(mass, flag=wx.LEFT|wx.TOP, border=10)
        vbox1.Add((-1,25))
        vbox1.Add(free, flag=wx.LEFT|wx.TOP, border=10)
        vbox1.Add((-1,25))
        vbox1.Add(kutta,flag=wx.LEFT|wx.TOP,border=10)
        hbox.Add(vbox1, flag=wx.LEFT|wx.TOP|wx.BOTTOM, border=10)
        hbox.Add((50, -1))
        hbox.Add(vbox2, flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=10)
        panel_root.SetSizer(hbox)
    #def onkutta(self,event):
        #pass


    def onquad(self, event):
        self.DestroyChildren()
    def OnCloseWindow(self, event):
        self.Destroy()
    def Oneuler(self, event):
        self.DestroyChildren()
        global panel_euler,text_euler,text2_euler,text3_euler,text4_euler
        panel_euler=wx.Panel(self,-1)
        self.SetSize((400,301))
        submit_euler = wx.Button(panel_euler, -1, "submit", pos=(90, 190))
        self.Bind(wx.EVT_BUTTON, self.onsubmit_euler, submit_euler)
        static = wx.StaticText(panel_euler, wx.NewId(), "integral of", pos=(10, 50))
        text_euler = wx.TextCtrl(panel_euler, wx.NewId(), "1/x", size=(175, -1), pos=(150, 50))
        static2 = wx.StaticText(panel_euler, wx.NewId(), "lower limit", pos=(10, 80))
        text2_euler = wx.TextCtrl(panel_euler, wx.NewId(), "1", size=(175, -1), pos=(150, 80))
        static3 = wx.StaticText(panel_euler, wx.NewId(), "upper limit", pos=(10, 110))
        text3_euler = wx.TextCtrl(panel_euler, wx.NewId(), "2", size=(175, -1), pos=(150, 110))
        static4 = wx.StaticText(panel_euler, wx.NewId(), "Result", pos=(10, 150))
        self.text4_euler = wx.TextCtrl(panel_euler, wx.NewId(), "1", size=(175, -1), pos=(150, 150))
        back_euler=wx.Button(panel_euler,wx.NewId(),"Back",pos=(90,220))
        self.Bind(wx.EVT_BUTTON,self.Onintg,back_euler)

    def onsubmit_euler(self, event):
        global t1_euler,t2_euler, t3_euler,text4_euler
        t1_euler= text_euler.GetValue()
        t2_euler=text2_euler.GetValue()
        t3_euler=text3_euler.GetValue()
        a=(t1_euler)
        b=float(t2_euler)
        c=float(t3_euler)
        d=(maclauren.maclauren__(a,b,c))
        e=str(d)
        #print e
        self.text4_euler.SetValue(e)

    def onromberg(self, event):
        self.DestroyChildren()
        global panel_romberg,text_romberg,text2_romberg,text3_romberg,text4_romberg,text5_romberg,text6_romberg
        panel_romberg=wx.Panel(self,-1)
        self.SetSize((400,301))
        submit_romberg = wx.Button(panel_romberg, -1, "submit", pos=(90, 230))
        self.Bind(wx.EVT_BUTTON, self.onsubmit_romberg, submit_romberg)
        static = wx.StaticText(panel_romberg, wx.NewId(), "integral of", pos=(10, 50))
        text_romberg = wx.TextCtrl(panel_romberg, wx.NewId(), "1.0/x", size=(175, -1), pos=(200, 50))
        static2 = wx.StaticText(panel_romberg, wx.NewId(), "enter k, for degree of accuracy h^2k:",size=(190, -1), pos=(10, 80))
        text2_romberg = wx.TextCtrl(panel_romberg, wx.NewId(), "5", size=(175, -1), pos=(200, 80))
        static3 = wx.StaticText(panel_romberg, wx.NewId(), "enter initial m, for 2^m starting points:",size=(190, -1), pos=(10, 110))
        text3_romberg = wx.TextCtrl(panel_romberg, wx.NewId(), "3", size=(175, -1), pos=(200, 110))
        static4 = wx.StaticText(panel_romberg, wx.NewId(), "enter upper bound:", size=(190, -1),pos=(10, 140))
        text4_romberg = wx.TextCtrl(panel_romberg, wx.NewId(), "2", size=(175, -1), pos=(200, 140))
        static5 = wx.StaticText(panel_romberg, wx.NewId(), "enter lower bound", size=(190, -1),pos=(10, 170))
        text5_romberg = wx.TextCtrl(panel_romberg, wx.NewId(), "1", size=(175, -1), pos=(200, 170))
        static6 = wx.StaticText(panel_romberg, wx.NewId(), "Result", pos=(10, 200))
        self.text6_romberg = wx.TextCtrl(panel_romberg, wx.NewId(), "1", size=(175, -1), pos=(200, 200))

        back_intg=wx.Button(panel_romberg,wx.NewId(),"Back",pos=(90,260))
        self.Bind(wx.EVT_BUTTON,self.Onintg,back_intg)

    def onsubmit_romberg(self, event):
        #self.DestroyChildren()
        global t1_romberg,t2_romberg, t3_romberg,t4_romberg,t5_romberg
        t1_romberg= text_romberg.GetValue()
        t2_romberg=text2_romberg.GetValue()
        t3_romberg=text3_romberg.GetValue()
        t4_romberg=text4_romberg.GetValue()
        t5_romberg=text5_romberg.GetValue()

        #main(fun,_k,_m,ub,lb)
        a=(t1_romberg)
        b=int(t2_romberg)
        c=int(t3_romberg)
        w=int(t4_romberg)
        x=int(t5_romberg)
        ans=str(romberg.main(a,b,c,w,x))
        #print ans
        self.text6_romberg.SetValue(ans)

    def Onfree(self, event):
        self.DestroyChildren()
        global panel_free,text_free,text2_free
        panel_free=wx.Panel(self,-1)
        self.SetSize((400,301))
        submit_free = wx.Button(panel_free, -1, "submit", pos=(90, 120))
        self.Bind(wx.EVT_BUTTON, self.onsubmit_free, submit_free)
        static = wx.StaticText(panel_free, wx.NewId(), "no. of nodes", pos=(10, 50))
        text_free = wx.TextCtrl(panel_free, wx.NewId(), "100", size=(175, -1), pos=(150, 50))
        static2 = wx.StaticText(panel_free, wx.NewId(), "equation of initial string", pos=(10, 80))
        text2_free = wx.TextCtrl(panel_free, wx.NewId(), "sin(x*2.5*pi)", size=(175, -1), pos=(150, 80))
        back_free=wx.Button(panel_free,wx.NewId(),"Back",pos=(90,150))
        self.Bind(wx.EVT_BUTTON,self.Onroot,back_free)

    def onsubmit_free(self,event):
        global t1_free,t2_free
        t1_free= text_free.GetValue()
        t2_free=text2_free.GetValue()
        a=int(t1_free)
        b=(t2_free)
        free.string__(a,b)

    def Onmass(self, event):
        self.DestroyChildren()
        global panel_mass,text,text2
        panel_mass=wx.Panel(self,-1)
        self.SetSize((400,301))
        submit_mass = wx.Button(panel_mass, -1, "submit", pos=(90, 120))
        self.Bind(wx.EVT_BUTTON, self.onsubmit_mass, submit_mass)
        static = wx.StaticText(panel_mass, wx.NewId(), "equation of initial string", pos=(10, 50))
        text = wx.TextCtrl(panel_mass, wx.NewId(), "2.71**(-1*100*(x-0.2)**2)", size=(175, -1), pos=(150, 50))
        static2 = wx.StaticText(panel_mass, wx.NewId(), "ratio of two mass densities", pos=(10, 80))
        text2 = wx.TextCtrl(panel_mass, wx.NewId(), "8", size=(100, -1), pos=(150, 80))
        back_mass=wx.Button(panel_mass,wx.NewId(),"Back",pos=(90,150))
        self.Bind(wx.EVT_BUTTON,self.Onroot,back_mass)
    def onsubmit_mass(self,event):
        global t1,t2
        t1= text.GetValue()
        t2=text2.GetValue()
        a=(t1)
        b=int(t2)
        mass.string__(a,b)
    def Onstring(self,event):
        self.DestroyChildren()
        global panel_str,text_str,text2_str
        panel_str=wx.Panel(self,-1)
        self.SetSize((400,301))
        submit_str = wx.Button(panel_str, -1, "submit", pos=(90, 120))
        self.Bind(wx.EVT_BUTTON, self.onsubmit_str, submit_str)
        static = wx.StaticText(panel_str, wx.NewId(), "no. of nodes", pos=(10, 50))
        text_str = wx.TextCtrl(panel_str, wx.NewId(), "", size=(100, -1), pos=(150, 50))
        static2 = wx.StaticText(panel_str, wx.NewId(), "equation of initial string", pos=(10, 80))
        text2_str = wx.TextCtrl(panel_str, wx.NewId(), "2.71**(-1*100*(x-0.5)**2)", size=(175, -1), pos=(150, 80))
        back_str=wx.Button(panel_str,wx.NewId(),"Back",pos=(90,150))
        self.Bind(wx.EVT_BUTTON,self.Onroot,back_str)

    def onsubmit_str(self,event):
        global t1_str,t2_str
        t1_str= text_str.GetValue()
        t2_str=text2_str.GetValue()
        a=int(t1_str)
        b=(t2_str)
        stri.string__(a,b)

    def onkutta(self, event):
        self.DestroyChildren()
        global panel_kutta,text_kutta,text2_kutta,text3_kutta,text4_kutta,text5_kutta,text6_kutta,text7_kutta,text8_kutta,text9_kutta
        panel_kutta=wx.Panel(self,-1)
        self.SetSize((400,401))
        submit_kutta = wx.Button(panel_kutta, -1, "submit", pos=(90, 290))
        self.Bind(wx.EVT_BUTTON, self.onsubmit_kutta, submit_kutta)
        static = wx.StaticText(panel_kutta, wx.NewId(), "enter a first function:", pos=(10, 50))
        text_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "x2-2*x1", size=(175, -1), pos=(200, 50))
        static2 = wx.StaticText(panel_kutta, wx.NewId(), "enter a second function:",size=(190, -1), pos=(10, 80))
        text2_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "x1-2*x2", size=(175, -1), pos=(200, 80))
        static3 = wx.StaticText(panel_kutta, wx.NewId(), "enter the x10(first_variable): ",size=(190, -1), pos=(10, 110))
        text3_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "0.1", size=(175, -1), pos=(200, 110))
        static4 = wx.StaticText(panel_kutta, wx.NewId(), "enter the x20(second_variable):", size=(190, -1),pos=(10, 140))
        text4_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "0.1", size=(175, -1), pos=(200, 140))
        static5 = wx.StaticText(panel_kutta, wx.NewId(), "enter the v1(initial velocity):", size=(190, -1),pos=(10, 170))
        text5_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "0", size=(175, -1), pos=(200, 170))
        static6 = wx.StaticText(panel_kutta, wx.NewId(), "enter the v2(initial velocity):", pos=(10, 200))
        text6_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "0", size=(175, -1), pos=(200, 200))
        static7 = wx.StaticText(panel_kutta, wx.NewId(), "enter the h value:", pos=(10, 230))
        text7_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "0.05", size=(175, -1), pos=(200, 230))
        static8 = wx.StaticText(panel_kutta, wx.NewId(), "enter the final time:", pos=(10, 260))
        text8_kutta = wx.TextCtrl(panel_kutta, wx.NewId(), "12.56637", size=(175, -1), pos=(200, 260))
        back_intg=wx.Button(panel_kutta,wx.NewId(),"Back",pos=(90,320))
        self.Bind(wx.EVT_BUTTON,self.Onroot,back_intg)
        #oscillator(x2-2*x1,x1-2*x2,0.1,0.1,0.05,0,0,6.283185*2)

    def onsubmit_kutta(self,event):
        global t1_kutta,t2_kutta, t3_kutta,t4_kutta,t5_kutta
        t1_kutta= text_kutta.GetValue()
        t2_kutta=text2_kutta.GetValue()
        t3_kutta=text3_kutta.GetValue()
        t4_kutta=text4_kutta.GetValue()
        t5_kutta=text5_kutta.GetValue()
        t6_kutta=text6_kutta.GetValue()
        t7_kutta=text7_kutta.GetValue()
        t8_kutta=text8_kutta.GetValue()

        fun1=(t1_kutta)
        fun2=(t2_kutta)
        x10=float(t3_kutta)
        x20=float(t4_kutta)
        v10=float(t5_kutta)
        v20=float(t6_kutta)
        h=float(t7_kutta)
        time=float(t8_kutta)
        print fun1,fun2,v10,v20,time
        (runge.oscillator(fun1,fun2,x10,x20,h,v10,v20,time))
        #runge.oscillator("x2-2*x1","x1-2*x2",0.1,0.1,0.05,0,0,6.283185*2)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = WX_DOP(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
