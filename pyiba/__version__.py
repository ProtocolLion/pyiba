#! /usr/bin/env python
# -*- coding: utf-8 -*-

""
# 変更履歴
# [日付] [変更内容]
# 2024-06-14 バージョン管理の開始
# ...（以降、変更があれば追記）...
""

__version_info__ = (1, 0, 0)
__version__ = '.'.join(map(str, __version_info__))

def get_version():
    return __version__

if __name__ == "__main__":
    print("Version:", get_version())
