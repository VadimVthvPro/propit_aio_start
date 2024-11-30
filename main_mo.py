import gettext
import sqlite3




def printer(user_id, com):
    conn = sqlite3.connect('pro3.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT lang FROM user_lang WHERE user_id = ?", (str(user_id), )
    )
    leng= cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    lenguag = gettext.translation('messages', localedir='locales', languages=[leng], fallback=False)
    lenguag.install()
    _ = lenguag.gettext  # Greek
    ngettext = lenguag.ngettext
    return _(com)


def printer_with_given(leng, com):
 #   lengu = gettext.translation('messages', localedir='locales', languages=[leng], fallback=False)
 #   lengu.install()
    _ = leng.gettext  # Greek
    ngettext = leng.ngettext
    return _(com)
