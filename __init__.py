# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ParallelOffset
                                 A QGIS plugin
 Creates a parallell line at a given distance
                             -------------------
        begin                : 2013-07-23
        copyright            : (C) 2013 by City and County of Swansea
        email                : steven.gardiner@swansea.gov.uk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Line Offset"


def description():
    return "Creates a parallell line at a given distance"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "City and County of Swansea"

def email():
    return "steven.gardiner@swansea.gov.uk"

def classFactory(iface):
    # load ParallelOffset class from file ParallelOffset
    from paralleloffset import ParallelOffset
    return ParallelOffset(iface)
