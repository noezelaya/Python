# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar  5 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import math

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ingeniería Economica", pos = wx.DefaultPosition, size = wx.Size( 400,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gSizer2 = wx.GridSizer( 4, 5, 0, 0 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Seleccione lo que desea conocer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		gSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnSimple = wx.Button( self, wx.ID_ANY, u"I. Simple", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnSimple.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.btnSimple.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		gSizer2.Add( self.btnSimple, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btn = wx.Button( self, wx.ID_ANY, u"I. Compuesto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.btn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		gSizer2.Add( self.btn, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnCerrar = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCerrar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.btnCerrar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		gSizer2.Add( self.btnCerrar, 0, wx.ALL, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSimple.Bind( wx.EVT_BUTTON, self.irSimple )
		self.btn.Bind( wx.EVT_BUTTON, self.irCompuesto )
		self.btnCerrar.Bind( wx.EVT_BUTTON, self.Cerrar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def irSimple( self, event ):
		form_hijo=simpleFrame(self)
		form_hijo.Show()
		form_hijo.Mostrar("VER")
	
	def irCompuesto( self, event ):
		form_hijo=compuestoFrame(self)
		form_hijo.Show()
		form_hijo.Mostrar("VER")
	
	def Cerrar( self, event ):
		self.Close(self.Close(True))    

##########Simple##########

###########################################################################
## Class simpleFrame
###########################################################################

class simpleFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Interes Simple", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		#Clase Padre formulario superior
		self.frm_padre=parent
		
		sizer0 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer3 = wx.GridSizer( 9, 5, 0, 0 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Ingrese los valores", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Interés", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		self.m_staticText71.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText71.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText71.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.interesLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.interesLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText711 = wx.StaticText( self, wx.ID_ANY, u"Capital", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText711.Wrap( -1 )
		self.m_staticText711.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText711.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText711.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText711, 0, wx.ALL, 5 )
		
		self.capitalLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.capitalLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7112 = wx.StaticText( self, wx.ID_ANY, u"Tasa de interés", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7112.Wrap( -1 )
		self.m_staticText7112.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText7112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText7112, 0, wx.ALL, 5 )
		
		self.tasaLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.tasaLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7111 = wx.StaticText( self, wx.ID_ANY, u"Tiempo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7111.Wrap( -1 )
		self.m_staticText7111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText7111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText7111, 0, wx.ALL, 5 )
		
		self.tiempoLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.tiempoLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Seleccione lo que desee conocer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer3.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnInteres = wx.Button( self, wx.ID_ANY, u"Interes", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btnInteres, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Capital", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Tasa de I.", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button15, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Tiempo", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button16, 0, wx.ALL, 5 )
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		#self.m_button12 = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		#gSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		#self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.m_staticText22.Wrap( -1 )
		#gSizer3.Add( self.m_staticText22, 0, wx.ALL, 5 )
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		gSizer3.Add( self.lbl3, 0, wx.ALL, 5 )
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnInteres.Bind( wx.EVT_BUTTON, self.Interes )
		self.m_button14.Bind( wx.EVT_BUTTON, self.Capital )
		self.m_button15.Bind( wx.EVT_BUTTON, self.Tasa )
		self.m_button16.Bind( wx.EVT_BUTTON, self.Tiempo )
		#self.m_button12.Bind( wx.EVT_BUTTON, self.Close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Interes( self, event ):
		try:
			interes=self.interesLabel.GetValue()
			interes=float(interes)
			capital=self.capitalLabel.GetValue()
			capital=float(capital)
			tasa=self.tasaLabel.GetValue()
			tasa=float(tasa)
			tiempo=self.tiempoLabel.GetValue()
			tiempo=float(tiempo)
			if (capital<1 or tasa<0 or tiempo<0):
				self.lbl3.SetLabel("Ingrese cantidades positivas")
			else:
				resultado=(float(capital)*float(tasa)*float(tiempo))
				self.lbl3.SetLabel("El interés es: "+str(resultado))
		except:
			self.lbl3.SetLabel("Ingrese cantidades validas")
	
	def Capital( self, event ):
		try:
			interes=self.interesLabel.GetValue()
			interes=float(interes)
			capital=self.capitalLabel.GetValue()
			capital=float(capital)
			tasa=self.tasaLabel.GetValue()
			tasa=float(tasa)
			tiempo=self.tiempoLabel.GetValue()
			tiempo=float(tiempo)
			if (interes<0 or capital<1 or tasa<0 or tiempo<0):
				self.lbl3.SetLabel("Ingrese cantidades positivas")
			else:
				resultado=(float(interes)/(float(tasa)*float(tiempo)))
				self.lbl3.SetLabel("El capital es: "+str(resultado))
		except:
			self.lbl3.SetLabel("Ingrese cantidades validas")
		
	
	def Tasa( self, event ):
		try:
			interes=self.interesLabel.GetValue()
			interes=float(interes)
			capital=self.capitalLabel.GetValue()
			capital=float(capital)
			tasa=self.tasaLabel.GetValue()
			tasa=float(tasa)
			tiempo=self.tiempoLabel.GetValue()
			tiempo=float(tiempo)
			if (interes<0 or capital<1 or tasa<0 or tiempo<0):
				self.lbl3.SetLabel("Ingrese cantidades positivas")
			else:
				resultado=(float(interes)/(float(capital)*float(tiempo)))
				self.lbl3.SetLabel("La tasa de interés es: "+str(resultado))
		except:
			self.lbl3.SetLabel("Ingrese cantidades validas")
		
		
	
	def Tiempo( self, event ):
		try:
			interes=self.interesLabel.GetValue()
			interes=float(interes)
			capital=self.capitalLabel.GetValue()
			capital=float(capital)
			tasa=self.tasaLabel.GetValue()
			tasa=float(tasa)
			tiempo=self.tiempoLabel.GetValue()
			tiempo=float(tiempo)
			if (interes<0 or capital<1 or tasa<0 or tiempo<0):
				self.lbl3.SetLabel("Ingrese cantidades positivas")
			else:
				resultado=(float(interes)/(float(capital)*float(tasa)))
				self.lbl3.SetLabel("El tiempo es: "+str(resultado))
		except:
			self.lbl3.SetLabel("Ingrese cantidades validas")
		
		
	
	#def Close( self, event ):
		#self.Close()
	

#########################################
class compuestoFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Interes Compuesto", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		#Clase Padre formulario superior
		self.frm_padre=parent
		
		sizer0 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer3 = wx.GridSizer( 9, 5, 0, 0 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Ingrese los valores", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Monto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		self.m_staticText71.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText71.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText71.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.interesLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.interesLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText711 = wx.StaticText( self, wx.ID_ANY, u"Capital", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText711.Wrap( -1 )
		self.m_staticText711.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText711.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText711.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText711, 0, wx.ALL, 5 )
		
		self.capitalLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.capitalLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7112 = wx.StaticText( self, wx.ID_ANY, u"Tasa de interés", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7112.Wrap( -1 )
		self.m_staticText7112.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText7112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText7112, 0, wx.ALL, 5 )
		
		self.tasaLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.tasaLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7111 = wx.StaticText( self, wx.ID_ANY, u"Tiempo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7111.Wrap( -1 )
		self.m_staticText7111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText7111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_staticText7111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		gSizer3.Add( self.m_staticText7111, 0, wx.ALL, 5 )
		
		self.tiempoLabel = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.tiempoLabel, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Seleccione lo que desee conocer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer3.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnInteres = wx.Button( self, wx.ID_ANY, u"Monto", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btnInteres, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self, wx.ID_ANY, u"Capital", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Tasa de I.", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button15, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Tiempo", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button16, 0, wx.ALL, 5 )
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		#self.m_button12 = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		#gSizer3.Add( self.m_button12, 0, wx.ALL, 5 )
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		#self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.m_staticText22.Wrap( -1 )
		#gSizer3.Add( self.m_staticText22, 0, wx.ALL, 5 )
		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )
		gSizer3.Add( self.lbl3, 0, wx.ALL, 5 )
		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnInteres.Bind( wx.EVT_BUTTON, self.Interes )
		self.m_button14.Bind( wx.EVT_BUTTON, self.Capital )
		self.m_button15.Bind( wx.EVT_BUTTON, self.Tasa )
		self.m_button16.Bind( wx.EVT_BUTTON, self.Tiempo )
		#self.m_button12.Bind( wx.EVT_BUTTON, self.Close )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Interes( self, event ):
		interes=self.interesLabel.GetValue()
		capital=self.capitalLabel.GetValue()
		tasa=self.tasaLabel.GetValue()
		tiempo=self.tiempoLabel.GetValue()
		resultado=(float(capital)*((1+float(tasa))**float(tiempo)))
		self.lbl3.SetLabel("El Monto es: "+str(resultado))
	
	def Capital( self, event ):
		monto=self.interesLabel.GetValue()
		capital=self.capitalLabel.GetValue()
		tasa=self.tasaLabel.GetValue()
		tiempo=self.tiempoLabel.GetValue()
		resultado=(float(monto)/((1+float(tasa))**float(tiempo)))
		self.lbl3.SetLabel("El capital es: "+str(resultado))
	
	def Tasa( self, event ):
		monto=self.interesLabel.GetValue()
		capital=self.capitalLabel.GetValue()
		tasa=self.tasaLabel.GetValue()
		tiempo=self.tiempoLabel.GetValue()
		resultado=((float(monto)/(float(capital)**(1/float(tiempo)))-1))
		self.lbl3.SetLabel("La tasa de interés es: "+str(resultado))
	
	def Tiempo( self, event ):
		monto=self.interesLabel.GetValue()
		capital=self.capitalLabel.GetValue()
		tasa=self.tasaLabel.GetValue()
		tiempo=self.tiempoLabel.GetValue()
		resultado=(math.log10(float(monto)/float(capital))/math.log10(1+float(tasa)))
		self.lbl3.SetLabel("El tiempo es: "+str(resultado))
	
	#def Close( self, event ):
		#self.Close()
	




	
if __name__ == '__main__': 
  
	app = wx.App() # Se instancia una aplicación wxPython.
	frame=mainFrame(None) # Se instancia el contenedor principal.
	frame.Show() # Mostramos la ventana.
	app.MainLoop() # Esperamos a los eventos.
