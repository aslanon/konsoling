#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014, Onur ASLAN <slnnronur@gmail.com>#
#

from distutils.core import setup
datas = [('/bin', ['data/konsoling.desktop']), ("/usr/share/pixmaps", ["icons/konsoling.png"])]

setup(name = "konsoling",
    version = "1.0",
    description = "Konsoling masaüstü yazılımı",
    author = "Onur ASLAN",
    author_email = "slnnronur@gmail.com",
    url = "http://www.konsoling.com",
    packages = ["konsoling"],
    data_files = datas,
    scripts = ["data/konsoling"])

