# -*- coding: utf-8 -*-
#
# Tool Library
# Author: xiaoyue
# Email: xiaoyue2019@outlook.com
# Created Time: 2021-12-14


def parse_readme(filename: str = 'readme.md'):
    """Interpreting readme files
    :param filename str: md file name
    :return title str: title
    :return text  str: document content
    """
    with open(filename, encoding='utf8') as r:
        text = r.readlines()
    title = text[0].strip('# \n').strip()
    text = ''.join(text[1:]).strip()
    return title, text
