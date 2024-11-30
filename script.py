import gettext
lang = gettext. translation( 'base', localedir='locales', languages=['fr'])
lang. install()
_ = lang.gettext
print(_("Hello, world!"))