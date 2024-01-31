import locale

locale.setlocale(locale.LC_ALL, "")  # for Windows
# locale.setlocale(locale.LC_ALL, "de_DE") # for MacOS

number = 12345.6789
formatted = locale.format_string("%.02f", number)
print(formatted)
print(locale.getlocale())