import matplotlib as mpl
import matplotlib.font_manager as fm
#print(mpl.matplotlib_fname())

print(mpl.get_cachedir())
print(mpl.get_cachedir())

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
print(font_list)
