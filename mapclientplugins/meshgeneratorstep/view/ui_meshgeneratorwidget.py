# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapclientplugins\meshgeneratorstep\qt\meshgeneratorwidget.ui'
#
# Created: Fri Sep 29 10:44:37 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MeshGeneratorWidget(object):
    def setupUi(self, MeshGeneratorWidget):
        MeshGeneratorWidget.setObjectName("MeshGeneratorWidget")
        MeshGeneratorWidget.resize(580, 616)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MeshGeneratorWidget.sizePolicy().hasHeightForWidth())
        MeshGeneratorWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(MeshGeneratorWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtGui.QDockWidget(MeshGeneratorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(353, 197))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 364, 531))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.identifier_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.identifier_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.identifier_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.identifier_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.identifier_frame.setObjectName("identifier_frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.identifier_frame)
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.identifier_label = QtGui.QLabel(self.identifier_frame)
        self.identifier_label.setObjectName("identifier_label")
        self.verticalLayout_4.addWidget(self.identifier_label)
        self.line = QtGui.QFrame(self.identifier_frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_3.addWidget(self.identifier_frame)
        self.meshType_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.meshType_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meshType_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.meshType_frame.setObjectName("meshType_frame")
        self.formLayout_3 = QtGui.QFormLayout(self.meshType_frame)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.meshType_label = QtGui.QLabel(self.meshType_frame)
        self.meshType_label.setObjectName("meshType_label")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.meshType_label)
        self.meshType_comboBox = QtGui.QComboBox(self.meshType_frame)
        self.meshType_comboBox.setObjectName("meshType_comboBox")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.meshType_comboBox)
        self.verticalLayout_3.addWidget(self.meshType_frame)
        self.meshTypeOptions_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.meshTypeOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meshTypeOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.meshTypeOptions_frame.setObjectName("meshTypeOptions_frame")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.meshTypeOptions_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3.addWidget(self.meshTypeOptions_frame)
        self.modifyOptions_frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.modifyOptions_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.modifyOptions_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.modifyOptions_frame.setObjectName("modifyOptions_frame")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.modifyOptions_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.deleteElementRanges_label = QtGui.QLabel(self.modifyOptions_frame)
        self.deleteElementRanges_label.setObjectName("deleteElementRanges_label")
        self.verticalLayout_6.addWidget(self.deleteElementRanges_label)
        self.deleteElementsRanges_lineEdit = QtGui.QLineEdit(self.modifyOptions_frame)
        self.deleteElementsRanges_lineEdit.setObjectName("deleteElementsRanges_lineEdit")
        self.verticalLayout_6.addWidget(self.deleteElementsRanges_lineEdit)
        self.scale_label = QtGui.QLabel(self.modifyOptions_frame)
        self.scale_label.setObjectName("scale_label")
        self.verticalLayout_6.addWidget(self.scale_label)
        self.scale_lineEdit = QtGui.QLineEdit(self.modifyOptions_frame)
        self.scale_lineEdit.setObjectName("scale_lineEdit")
        self.verticalLayout_6.addWidget(self.scale_lineEdit)
        self.verticalLayout_3.addWidget(self.modifyOptions_frame)
        self.displayOptions_groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayOptions_groupBox.sizePolicy().hasHeightForWidth())
        self.displayOptions_groupBox.setSizePolicy(sizePolicy)
        self.displayOptions_groupBox.setObjectName("displayOptions_groupBox")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.displayOptions_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.displayAxes_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayAxes_checkBox.setObjectName("displayAxes_checkBox")
        self.verticalLayout_7.addWidget(self.displayAxes_checkBox)
        self.displayLines_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayLines_checkBox.setObjectName("displayLines_checkBox")
        self.verticalLayout_7.addWidget(self.displayLines_checkBox)
        self.displaySurfaces_frame = QtGui.QFrame(self.displayOptions_groupBox)
        self.displaySurfaces_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.displaySurfaces_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.displaySurfaces_frame.setObjectName("displaySurfaces_frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.displaySurfaces_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.displaySurfaces_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfaces_checkBox.setObjectName("displaySurfaces_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfaces_checkBox)
        self.displaySurfacesExterior_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesExterior_checkBox.setObjectName("displaySurfacesExterior_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfacesExterior_checkBox)
        self.displaySurfacesTranslucent_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesTranslucent_checkBox.setObjectName("displaySurfacesTranslucent_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfacesTranslucent_checkBox)
        self.displaySurfacesWireframe_checkBox = QtGui.QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesWireframe_checkBox.setObjectName("displaySurfacesWireframe_checkBox")
        self.horizontalLayout_3.addWidget(self.displaySurfacesWireframe_checkBox)
        self.verticalLayout_7.addWidget(self.displaySurfaces_frame)
        self.displayElementNumbers_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayElementNumbers_checkBox.setObjectName("displayElementNumbers_checkBox")
        self.verticalLayout_7.addWidget(self.displayElementNumbers_checkBox)
        self.displayNodeNumbers_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayNodeNumbers_checkBox.setObjectName("displayNodeNumbers_checkBox")
        self.verticalLayout_7.addWidget(self.displayNodeNumbers_checkBox)
        self.displayNodeDerivatives_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayNodeDerivatives_checkBox.setObjectName("displayNodeDerivatives_checkBox")
        self.verticalLayout_7.addWidget(self.displayNodeDerivatives_checkBox)
        self.displayXiAxes_checkBox = QtGui.QCheckBox(self.displayOptions_groupBox)
        self.displayXiAxes_checkBox.setObjectName("displayXiAxes_checkBox")
        self.verticalLayout_7.addWidget(self.displayXiAxes_checkBox)
        self.verticalLayout_3.addWidget(self.displayOptions_groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.viewAll_button = QtGui.QPushButton(self.frame)
        self.viewAll_button.setObjectName("viewAll_button")
        self.horizontalLayout_2.addWidget(self.viewAll_button)
        self.done_button = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done_button.sizePolicy().hasHeightForWidth())
        self.done_button.setSizePolicy(sizePolicy)
        self.done_button.setObjectName("done_button")
        self.horizontalLayout_2.addWidget(self.done_button)
        self.verticalLayout.addWidget(self.frame)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.sceneviewer_widget = SceneviewerWidget(MeshGeneratorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewer_widget.sizePolicy().hasHeightForWidth())
        self.sceneviewer_widget.setSizePolicy(sizePolicy)
        self.sceneviewer_widget.setObjectName("sceneviewer_widget")
        self.horizontalLayout.addWidget(self.sceneviewer_widget)

        self.retranslateUi(MeshGeneratorWidget)
        QtCore.QMetaObject.connectSlotsByName(MeshGeneratorWidget)

    def retranslateUi(self, MeshGeneratorWidget):
        MeshGeneratorWidget.setWindowTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Mesh Generator Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.identifier_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Identifier", None, QtGui.QApplication.UnicodeUTF8))
        self.meshType_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Mesh type:", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteElementRanges_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Delete element ID ranges (e.g. 1,2-5,13):", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_label.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Scale x*y*z:", None, QtGui.QApplication.UnicodeUTF8))
        self.displayOptions_groupBox.setTitle(QtGui.QApplication.translate("MeshGeneratorWidget", "Display options:", None, QtGui.QApplication.UnicodeUTF8))
        self.displayAxes_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Axes", None, QtGui.QApplication.UnicodeUTF8))
        self.displayLines_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Lines", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfaces_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Surfaces", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfacesExterior_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Exterior", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfacesTranslucent_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Transluc.", None, QtGui.QApplication.UnicodeUTF8))
        self.displaySurfacesWireframe_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Wireframe", None, QtGui.QApplication.UnicodeUTF8))
        self.displayElementNumbers_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Element numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.displayNodeNumbers_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Node numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.displayNodeDerivatives_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Node derivatives", None, QtGui.QApplication.UnicodeUTF8))
        self.displayXiAxes_checkBox.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Xi axes", None, QtGui.QApplication.UnicodeUTF8))
        self.viewAll_button.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "View All", None, QtGui.QApplication.UnicodeUTF8))
        self.done_button.setText(QtGui.QApplication.translate("MeshGeneratorWidget", "Done", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget
