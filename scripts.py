import gettext
el = gettext.translation('base', localedir='locales', languages=['fr'])
el.install()
_ = el.gettext