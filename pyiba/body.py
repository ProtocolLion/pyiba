#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""pyibaのmainモジュール

このモジュールは、pyibaプロジェクトのメインエントリポイントを提供します。
"""

#---------------------------------
# インポート
#---------------------------------
# standard library

# third party library

# local library
# from ..std.stdutils import *
from __version__ import __version_info__
import app_const
import app_argparser
from .main_gui import show_window

#---------------------------------
# 定数
#---------------------------------


#---------------------------------
# main
#---------------------------------
def main():
    """Main function for the pyiba body module."""

    ############################################################
    # constants
    ############################################################
    print("This is the main function of the pyiba body module.")

    ############################################################
    # argparser
    ############################################################
    print("This is the main function of the pyiba body module.")

    ############################################################
    # logger
    ############################################################
    print("This is the main function of the pyiba body module.")

    ############################################################
    # common process
    ############################################################
    print("This is the main function of the pyiba body module.")

    ############################################################
    # main process
    ############################################################
    print("This is the main function of the pyiba body module.")
    # tkinterウィンドウを表示
    show_window()
