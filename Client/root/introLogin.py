## 1.) Find this:
from _weakref import proxy


## 2.) Add after this:
ENABLE_LANGUAGE = True
if ENABLE_LANGUAGE:
	import uiLanguage

## 1.) Find this:
class LoginWindow(ui.ScriptWindow):
	def __init__(self, stream):

## 2.) Add after this:
		if ENABLE_LANGUAGE:
			self.wndLanguage = uiLanguage.LanguageLogin()

## 1.) Find this:
			exception.Abort("LoginWindow.__LoadScript.BindObject")

## 2.) Add after this:
		if ENABLE_LANGUAGE:
			self.wndLanguage.IsLogin()