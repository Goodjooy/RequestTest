# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"请求测试", pos = wx.DefaultPosition, size = wx.Size( 1024,576 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 512,288 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer_root = wx.BoxSizer( wx.VERTICAL )

		bSizer_work_group = wx.BoxSizer( wx.HORIZONTAL )

		bSizer_workshop = wx.BoxSizer( wx.VERTICAL )

		bSizer_workshop.SetMinSize( wx.Size( 300,-1 ) )
		self.m_panel_workshop = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_panel_workshop, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl_request_struct = wx.TreeCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT|wx.TR_SINGLE|wx.TR_TWIST_BUTTONS )
		bSizer6.Add( self.m_treeCtrl_request_struct, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer6 )
		self.m_scrolledWindow1.Layout()
		bSizer6.Fit( self.m_scrolledWindow1 )
		bSizer4.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button1 = wx.Button( self.m_panel_workshop, wx.ID_ANY, u"新建请求", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel_workshop, wx.ID_ANY, u"发送请求", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self.m_panel_workshop, wx.ID_ANY, u"设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )


		self.m_panel_workshop.SetSizer( bSizer4 )
		self.m_panel_workshop.Layout()
		bSizer4.Fit( self.m_panel_workshop )
		bSizer_workshop.Add( self.m_panel_workshop, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline_1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_workshop.Add( self.m_staticline_1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_gauge_state = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_state.SetValue( 0 )
		bSizer_workshop.Add( self.m_gauge_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer_work_group.Add( bSizer_workshop, 0, wx.EXPAND, 5 )

		self.m_staticline_2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer_work_group.Add( self.m_staticline_2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_info_veiw_port = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self.m_panel_info_veiw_port, wx.ID_ANY, u"请求头与响应头", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer8.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_staticline5 = wx.StaticLine( self.m_panel_info_veiw_port, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer8.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeListCtrl_request_info = wx.dataview.TreeListCtrl( self.m_panel_info_veiw_port, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_treeListCtrl_request_info.AppendColumn( u"Column1", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.m_treeListCtrl_request_info.AppendColumn( u"Column2", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

		bSizer12.Add( self.m_treeListCtrl_request_info, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer8.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_panel_info_veiw_port, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer7.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self.m_panel_info_veiw_port, wx.ID_ANY, u"响应主体", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer9.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_staticline6 = wx.StaticLine( self.m_panel_info_veiw_port, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_simplebook_respond_body = wx.Simplebook( self.m_panel_info_veiw_port, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_html = wx.Panel( self.m_simplebook_respond_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel_html, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer14.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_html.SetSizer( bSizer14 )
		self.m_panel_html.Layout()
		bSizer14.Fit( self.m_panel_html )
		self.m_simplebook_respond_body.AddPage( self.m_panel_html, u"a page", False )
		self.m_panel_json = wx.Panel( self.m_simplebook_respond_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl_respond_json = wx.TreeCtrl( self.m_panel_json, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_NO_LINES|wx.TR_TWIST_BUTTONS )
		bSizer15.Add( self.m_treeCtrl_respond_json, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_json.SetSizer( bSizer15 )
		self.m_panel_json.Layout()
		bSizer15.Fit( self.m_panel_json )
		self.m_simplebook_respond_body.AddPage( self.m_panel_json, u"a page", False )
		self.m_panel_else = wx.Panel( self.m_simplebook_respond_body, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self.m_panel_else, wx.ID_ANY, u"不可接受的响应", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer16.Add( self.m_staticText4, 0, wx.ALL, 5 )


		self.m_panel_else.SetSizer( bSizer16 )
		self.m_panel_else.Layout()
		bSizer16.Fit( self.m_panel_else )
		self.m_simplebook_respond_body.AddPage( self.m_panel_else, u"a page", False )

		bSizer9.Add( self.m_simplebook_respond_body, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.m_panel_info_veiw_port.SetSizer( bSizer7 )
		self.m_panel_info_veiw_port.Layout()
		bSizer7.Fit( self.m_panel_info_veiw_port )
		bSizer_work_group.Add( self.m_panel_info_veiw_port, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer_root.Add( bSizer_work_group, 1, wx.EXPAND, 5 )

		self.m_staticline_3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_root.Add( self.m_staticline_3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_infomation = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_infomation.Wrap( -1 )

		bSizer_root.Add( self.m_staticText_infomation, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer_root )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.exit )
		self.Bind( wx.EVT_MOVE_END, self.resize )
		self.m_treeCtrl_request_struct.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.edit_data )
		self.m_treeCtrl_request_struct.Bind( wx.EVT_TREE_SEL_CHANGED, self.select_data )
		self.m_button1.Bind( wx.EVT_BUTTON, self.new_reuqest )
		self.m_button2.Bind( wx.EVT_BUTTON, self.send_request )
		self.m_button3.Bind( wx.EVT_BUTTON, self.setting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exit( self, event ):
		event.Skip()

	def resize( self, event ):
		event.Skip()

	def edit_data( self, event ):
		event.Skip()

	def select_data( self, event ):
		event.Skip()

	def new_reuqest( self, event ):
		event.Skip()

	def send_request( self, event ):
		event.Skip()

	def setting( self, event ):
		event.Skip()


###########################################################################
## Class MyDialogNewRequest
###########################################################################

class MyDialogNewRequest ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"新建请求", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"请求方法", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_ELLIPSIZE_MIDDLE )
		self.m_staticText11.Wrap( -1 )

		bSizer17.Add( self.m_staticText11, 0, wx.ALL|wx.EXPAND, 5 )

		m_comboBox_reuqest_methodChoices = [ u"GET", u"POST", u"PUT", u"DELETE" ]
		self.m_comboBox_reuqest_method = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox_reuqest_methodChoices, 0 )
		self.m_comboBox_reuqest_method.SetSelection( 0 )
		bSizer17.Add( self.m_comboBox_reuqest_method, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"请求URL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer17.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer17.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()
		bSizer17.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


