# -*- coding: utf-8 -*-
"""Matplotlib styling example

Python 3.6 or Newer

I used this to make maize and blue graphs for my final defense slides.
This setup works in Google Colab.

"""

import collections
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io

from google.colab import files

# These colors are taken from the UMich VPComm style guide
COLOR_TRANSPARENT = '#ffffff00'
COLOR_BLUE = '#00274c'
COLOR_MAIZE = '#ffcb05'
COLOR_WHITE = '#ffffff'
COLOR_ORANGE = '#cc6600'
COLOR_TEAL = '#83b2a8'
COLOR_BEIGE = '#9b9a6d'
COLOR_OFF_WHITE = '#e4e1df'
COLOR_LIGHT_BLUE = '#587abc'
COLOR_TAN = '#cfc096'
COLOR_DARK_GOLD = '#886b01'
COLOR_VIOLET = '#575294'
COLOR_RED_BROWN = '#7a121c'
COLOR_GOLD = '#7e732f'
COLOR_RED = '#a20f13'
COLOR_YELLOW_GREEN = '#aba70c'

# If you're not in a Colab-esque environment, just install whatever font you
# want to use.
#
# This is bash to add fonts to a non-system directory. Note that this _deletes_
# /var/fonts.
!rm -rf /var/fonts
!wget https://github.com/dadrian/research/raw/master/fonts/roboto-condensed/RobotoCondensed-Bold.ttf -P /var/fonts/roboto-condensed
!wget https://github.com/dadrian/research/raw/master/fonts/roboto-condensed/RobotoCondensed-BoldItalic.ttf -P /var/fonts/roboto-condensed
!wget https://github.com/dadrian/research/raw/master/fonts/roboto-condensed/RobotoCondensed-Italic.ttf -P /var/fonts/roboto-condensed
!wget https://github.com/dadrian/research/raw/master/fonts/roboto-condensed/RobotoCondensed-Light.ttf -P /var/fonts/roboto-condensed
!wget https://github.com/dadrian/research/raw/master/fonts/roboto-condensed/RobotoCondensed-LightItalic.ttf -P /var/fonts/roboto-condensed
!wget https://github.com/dadrian/research/raw/master/fonts/roboto-condensed/RobotoCondensed-Regular.ttf -P /var/fonts/roboto-condensed

# Tell Matplotlib about the fonts. If the fonts are just installed normally,
# you can skip this code.
font_files = mpl.font_manager.findSystemFonts(fontpaths='/var/fonts')
font_list = mpl.font_manager.createFontList(font_files)
known_font_fnames = [font.fname for font in mpl.font_manager.fontManager.ttflist]
to_add = {font for font in font_list if font.fname not in known_font_fnames}
mpl.font_manager.fontManager.ttflist.extend(list(to_add))

# This is equivalent to a Matplotlib RC, but defined in code. Again, this is
# useful if you're in an environment where you don't have a persistent home
# directory.
#
# Customize these to change appearance of the graph.
rc = {
  'axes': {
    'facecolor': COLOR_TRANSPARENT,
    'labelcolor': COLOR_WHITE,
    'edgecolor': COLOR_WHITE,
    'linewidth': 0.8,
    'axisbelow': True,
    'prop_cycle': mpl.cycler('color', [
      COLOR_MAIZE,
      COLOR_ORANGE,
      COLOR_OFF_WHITE,
      COLOR_YELLOW_GREEN,
      COLOR_RED,
      COLOR_TEAL,
      COLOR_LIGHT_BLUE,
      COLOR_BEIGE,
      COLOR_TAN,
    ]),
  },
  'xtick': {
    'labelsize': '12',
    'color': COLOR_WHITE,
  },
  'ytick': {
    'labelsize': 12,
    'color': COLOR_WHITE,
  },
  'grid': {
    'color': COLOR_WHITE,
    'linestyle': '--',
    'linewidth': '0.5'
  },
  'figure': {
    'facecolor': COLOR_BLUE,
    'figsize': '7.5, 4.218',
    'dpi': 192,
  },
  'font': {
    'family': 'Roboto Condensed',
    'size': '18',
    'weight': 'regular',
  },
  'savefig': {
    'facecolor': COLOR_TRANSPARENT,
    'edgecolor': COLOR_WHITE,
  },
  'text': {
     'color': COLOR_WHITE,
  }
}

# This actually sets the settings from the RC
for k, v in rc.items():
  mpl.rc(k, **v)

# Make some plots
x = list()
y = list()
fig = plt.gcf()
ax = plt.axes()
plt.plot(x, y, 'o', color=COLOR_MAIZE)
plt.show()
fig.savefig("graph.png", format='png')  # Save to graph.png
files.download("graph.png")  # Tell Colab to download graph.png
