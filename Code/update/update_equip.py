#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python_version : 3.13.0
#discription    : This defines the action that updates push button for bindings.
#author         : stellalalalalalalalalala
#created        : 2025.06.30
#last modified  : 2025.07.03


from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton

import json

def update_equip(self, state, build):

	with open("Text/CharmData.json", "r") as file:
		charmData = json.load(file)

	qss_charm_p1= """
		QPushButton {
			border-image: url("Image/charms/"""

	qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
		QPushButton:hover {
			background-color: #000000; } """

	buildA_1_state = state.get("equip_A")[0]
	buildA_2_state = state.get("equip_A")[1]
	buildA_3_state = state.get("equip_A")[2]
	buildA_4_state = state.get("equip_A")[3]
	buildA_5_state = state.get("equip_A")[4]
	buildA_6_state = state.get("equip_A")[5]
	buildA_7_state = state.get("equip_A")[6]
	buildA_8_state = state.get("equip_A")[7]
	buildA_9_state = state.get("equip_A")[8]
	buildA_10_state = state.get("equip_A")[9]
	buildA_11_state = state.get("equip_A")[10]

	if buildA_1_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_1.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_1_state == 1:
		build_current = build.get("current_A")[0]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_1.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_2_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_2.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_2_state == 1:
		build_current = build.get("current_A")[1]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_2.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_3_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_3.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_3_state == 1:
		build_current = build.get("current_A")[2]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_3.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_4_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_4.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_4_state == 1:
		build_current = build.get("current_A")[3]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_4.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_5_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_5.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_5_state == 1:
		build_current = build.get("current_A")[4]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_5.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_6_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_6.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_6_state == 1:
		build_current = build.get("current_A")[5]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_6.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_7_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_7.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_7_state == 1:
		build_current = build.get("current_A")[6]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_7.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_8_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_8.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_8_state == 1:
		build_current = build.get("current_A")[7]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_8.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_9_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_9.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_9_state == 1:
		build_current = build.get("current_A")[8]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_9.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_10_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_10.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_10_state == 1:
		build_current = build.get("current_A")[9]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_10.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildA_11_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_A_11.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildA_11_state == 1:
		build_current = build.get("current_A")[10]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_A_11.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	buildB_1_state = state.get("equip_B")[0]
	buildB_2_state = state.get("equip_B")[1]
	buildB_3_state = state.get("equip_B")[2]
	buildB_4_state = state.get("equip_B")[3]
	buildB_5_state = state.get("equip_B")[4]
	buildB_6_state = state.get("equip_B")[5]
	buildB_7_state = state.get("equip_B")[6]
	buildB_8_state = state.get("equip_B")[7]
	buildB_9_state = state.get("equip_B")[8]
	buildB_10_state = state.get("equip_B")[9]
	buildB_11_state = state.get("equip_B")[10]

	if buildB_1_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_1.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_1_state == 1:
		build_current = build.get("current_B")[0]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_1.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_2_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_2.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_2_state == 1:
		build_current = build.get("current_B")[1]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_2.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_3_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_3.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_3_state == 1:
		build_current = build.get("current_B")[2]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_3.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_4_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_4.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_4_state == 1:
		build_current = build.get("current_B")[3]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_4.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_5_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_5.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_5_state == 1:
		build_current = build.get("current_B")[4]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_5.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_6_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_6.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_6_state == 1:
		build_current = build.get("current_B")[5]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_6.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_7_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_7.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_7_state == 1:
		build_current = build.get("current_B")[6]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_7.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_8_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_8.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_8_state == 1:
		build_current = build.get("current_B")[7]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_8.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_9_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_9.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_9_state == 1:
		build_current = build.get("current_B")[8]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_9.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_10_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_10.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_10_state == 1:
		build_current = build.get("current_B")[9]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_10.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0

	if buildB_11_state == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.equip_B_11.setStyleSheet(qss_charm)
		qss_charm = ""
	elif buildB_11_state == 1:
		build_current = build.get("current_B")[10]
		charm_name = charmData["charm_" + str(build_current)]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.equip_B_11.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		return 0