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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#Import other Libraries
from qgis.core import *
from shapely.geometry import LineString
from qgis.utils import iface

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from paralleloffsetdialog import ParallelOffsetDialog


class ParallelOffset:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/paralleloffset"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale")[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/paralleloffset_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = ParallelOffsetDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/paralleloffset/icon.png"),
            u"Line Offset", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Line Offset", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Line Offset", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
			layers = iface.legendInterface().layers()
			if len(layers) != 0:
				#Check that there is a selected layer
				layer = iface.mapCanvas().currentLayer()
				if layer.type() == 0:
					#check selected layer is a vector layer
					if layer.geometryType() == 1:
						#check to see if selected layer is a linestring geometry
						if len(layer.selectedFeatures()) != 0:
							#Dir = float(self.dlg.ui.radLeft.isChecked()
							layers = iface.legendInterface().layers()
							Lexists = "false"
							#check to see if the virtual layer already exists
							for layer in layers:
								if layer.name() == "Parallel_Offset":
									Lexists = "true"
									vl = layer
							#if it doesn't exist create it
							if Lexists == "false":
								vl = QgsVectorLayer("Linestring?field=offset:integer&field=direction:string(10)&field=method:string(10)","Parallel_Offset","memory")
								#vl = QgsVectorLayer("Linestring", "Parallel_Offset", "memory")
								pr = vl.dataProvider()
								vl.startEditing()
								#pr.addAttributes( [ QgsField("offset", Double), QgsField("direction",  String), QgsField("method", String) ] )
							else:
								pr = vl.dataProvider()
								vl.startEditing()
						
							#get the direction
							Dir = 'right'
							if self.dlg.ui.radLeft.isChecked():
								Dir = 'left'
							#get the method
							if self.dlg.ui.radRound.isChecked():
								js = 1
							if self.dlg.ui.radMitre.isChecked():
								js = 2
							if self.dlg.ui.radBevel.isChecked():
								js = 3
							#get the offset
							loffset = float(self.dlg.ui.txtDistance.text())
						
							#create the new feature from the selection
					
							for feature in layer.selectedFeatures():
								geom = feature.geometry()
								h = geom.asPolyline()
								line = LineString(h)
								nline = line.parallel_offset(loffset, Dir,resolution=16,join_style=js,mitre_limit=10.0)
								#turn nline back into a polyline and add it to the map as a new layer.
								fet = QgsFeature()
								fet.setGeometry(QgsGeometry.fromWkt(str(nline)))
								fet.setAttributes( [loffset,Dir ,js] )
								pr.addFeatures( [ fet ] )
								vl.commitChanges()
							QgsMapLayerRegistry.instance().addMapLayer(vl)
							mc=self.iface.mapCanvas()
							mc.refresh()
						
				
				# do something useful (delete the line containing pass and
				# substitute with your code)
			#pass
