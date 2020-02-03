# Multi Lang System
Multi Language System


- Instructions:

# Installation:

Just Search in all Archives the DEFINES and place things as I have arranged.

DEFINES: 

- ENABLE_MULTILANGUAGE

# Modifications for add or remove countrys:

- For change DEFAULT LANGUAGE you need change in length.h DEFAULT_LANGUAGE = 1 for your number language or other.

If you want add or remove a country you need:

Search in Client PythonApplicationModule.cpp and InstanceBaseEffect.cpp :

// FOR CHANGE COUNTRY

and replace the switch case for your switch case, but remember you need to couple the cases, to the order of the DB "common.lang".

Search in Server length.h:

enum ELanguages

and replace:

	MAX_LANGUAGES = 6,
	TRANSLATE_LANGUAGE = 7,
	
For a number greater than the number of languages you have, just remember, TRANSLATE_LANGUAGE must be greater than MAX_LANGUAGES

In your DB common.lang 

Just remove or add the language, but remember, the order that you have in the database must match that of PythonApplicationModule and InstanceBaseEffect of the Client.

# Note

You just need to accommodate the translations of your server and client, in addition to adding a button to change language, I was already lazy to do so.

The system works fine, I have already tried it.

For references I took the free system of Languages in a Turkish forum and fixed it.
