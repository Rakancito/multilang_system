import uiScriptLocale, app

LANGUAGE_LOGIN_BOARD_WIDTH = 120
LANGUAGE_LOGIN_BOARD_HEIGHT = 40
LANGUAGE_FOLDER_PATH = "d:/ymir work/ui/game/language/flag/"

window = {
	"name" : "LanguageLogin",
	"style" : ("movable", "float",),
	# "x" : (SCREEN_WIDTH - 375) / 2,
	"x" : (SCREEN_WIDTH - 295) / 2,
	"y" : (SCREEN_HEIGHT - 495),
	"width" : LANGUAGE_LOGIN_BOARD_WIDTH,
	"height" : LANGUAGE_LOGIN_BOARD_HEIGHT,
	"children" :
	(
		{
			"name" : "LanguageBoard","type" : "thinboard",
			"x" : 0,"y" : 0,
			"width" : LANGUAGE_LOGIN_BOARD_WIDTH,"height" : LANGUAGE_LOGIN_BOARD_HEIGHT,
		},
		{
			"name" : "btnLanguage_hu","type" : "button",
			"x" : 10*1, "y" : 15,
			"tooltip_text" : "Hu",
			"default_image" : LANGUAGE_FOLDER_PATH+"hu.tga",
			"over_image" : LANGUAGE_FOLDER_PATH+"hu.tga",
			"down_image" : LANGUAGE_FOLDER_PATH+"hu.tga",
		},
		{
			"name" : "btnLanguage_en","type" : "button",
			"x" : 10*3, "y" : 15,
			"tooltip_text" : "En",
			"default_image" : LANGUAGE_FOLDER_PATH+"en.tga",
			"over_image" : LANGUAGE_FOLDER_PATH+"en.tga",
			"down_image" : LANGUAGE_FOLDER_PATH+"en.tga",
		},
		{
			"name" : "btnLanguage_ro","type" : "button",
			"x" : 10*5, "y" : 15,
			"tooltip_text" : "Ro",
			"default_image" : LANGUAGE_FOLDER_PATH+"ro.tga",
			"over_image" : LANGUAGE_FOLDER_PATH+"ro.tga",
			"down_image" : LANGUAGE_FOLDER_PATH+"ro.tga",
		},
		{
			"name" : "btnLanguage_tr","type" : "button",
			"x" : 10*7, "y" : 15,
			"tooltip_text" : "Tr",
			"default_image" : LANGUAGE_FOLDER_PATH+"tr.tga",
			"over_image" : LANGUAGE_FOLDER_PATH+"tr.tga",
			"down_image" : LANGUAGE_FOLDER_PATH+"tr.tga",
		},
		{
			"name" : "btnLanguage_es","type" : "button",
			"x" : 10*9, "y" : 15,
			"tooltip_text" : "Es",
			"default_image" : LANGUAGE_FOLDER_PATH+"es.tga",
			"over_image" : LANGUAGE_FOLDER_PATH+"es.tga",
			"down_image" : LANGUAGE_FOLDER_PATH+"es.tga",
		},
	)
}