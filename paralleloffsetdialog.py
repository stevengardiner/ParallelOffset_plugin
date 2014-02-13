# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ParallelOffsetDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_paralleloffset import Ui_ParallelOffset
# create the dialog for zoom to point


class ParallelOffsetDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_ParallelOffset()
        self.ui.setupUi(self)
