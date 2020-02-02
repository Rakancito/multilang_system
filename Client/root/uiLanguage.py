#_author_	: 'Valiant'
#_date_		: '2019.12.17'
#_version_	: '0.1'

import ui,app,uiCommon,net,uiScriptLocale,localeInfo,mouseModule,item,wndMgr,uiToolTip,dbg

GetLanguageList = ['en','es','hu','ro', 'tr', 'de'] ## Add new type, and add uiScript button
class LanguageLogin(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.languageButtonList = []
		self.wndQuestionDialog = None
		self.LoadingLanguage()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.languageButtonList = []
		self.wndQuestionDialog = None

	def LoadingLanguage(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/LanguageLogin.py")
		except:
			import exception
			exception.Abort("LanguageLogin.Initialize.LoadObject")
		try:
			GetObject = self.GetChild
			self.languageBoard = self.GetChild("LanguageBoard")
			for languageName in GetLanguageList:
				self.languageButtonList.append(GetObject('btnLanguage_{:s}'.format(languageName)))
			for i in xrange(len(self.languageButtonList)):
				self.languageButtonList[i].SetEvent(ui.__mem_func__(self.AskQuestion), i)
		except:
			import exception
			exception.Abort("LanguageLogin.Initialize.BindObject")

	def AnswerOnQuestion(self, answer):
		if not self.wndQuestionDialog:
			return

		self.wndQuestionDialog.Close()
		self.wndQuestionDialog = None

		if answer:
			dbg.LogBox("You selected the language.")
		else:
			dbg.LogBox("Could not select language.")
			# self.SendLanguageLoginPacket() or change packet!

	def AskQuestion(self, arg):
		self.wndQuestionDialog = uiCommon.QuestionDialog()
		self.wndQuestionDialog.SetText("Would you like to choose this language? [arg=%s]" % arg)
		self.wndQuestionDialog.SetAcceptEvent(lambda arg = TRUE: self.AnswerOnQuestion(arg))
		self.wndQuestionDialog.SetCancelEvent(lambda arg = FALSE: self.AnswerOnQuestion(arg))
		self.wndQuestionDialog.Open()
	
	def IsLogin(self):
		self.Show()

	def Close(self):
		self.Destroy()


#End line..
