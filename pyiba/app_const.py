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
APP_NAME_FULL    = "python image binary analyzer"
APP_NAME_SHORT   = "pyiba"
APP_NAME         = APP_NAME_SHORT
APP_VERSION      = '.'.join(map(str, __version_info__))
APP_VERSION_DATE = datetime.date.today().strftime("%Y-%m-%d")
APP_DESCRIPTION  = "python image binary analyzer"
