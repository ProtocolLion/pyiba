#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""pyibaのconstモジュール

このモジュールは、pyibaプロジェクトの定数を定義します。
"""

#---------------------------------
# インポート
#---------------------------------
# standard library
import datetime

# third party library

# local library
# from ..std.stdutils import *
from __version__ import __version_info__

#---------------------------------
# 定数
#---------------------------------
NAME_FULL    = "python image binary analyzer"
NAME_SHORT   = "pyiba"
NAME         = NAME_SHORT
VERSION      = '.'.join(map(str, __version_info__))
VERSION_DATE = datetime.date.today().strftime("%Y-%m-%d")
DESCRIPTION  = "python image binary analyzer"
