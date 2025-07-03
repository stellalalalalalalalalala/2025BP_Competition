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
from PyQt6.QtWidgets import QLabel

import json

def update_round2(self, state, build):

	with open("Text/CharmData.json", "r") as file:
		charmData = json.load(file)

	qss_charm_p1= """
		QLabel {
			border-image: url("Image/charms/"""

	qss_charm_p3 = """.png") 0 0 0 0 strech strech; }"""

	buildA_1_num = build.get("round_2_A")[0]
	buildA_2_num = build.get("round_2_A")[1]
	buildA_3_num = build.get("round_2_A")[2]
	buildA_4_num = build.get("round_2_A")[3]
	buildA_5_num = build.get("round_2_A")[4]
	buildA_6_num = build.get("round_2_A")[5]
	buildA_7_num = build.get("round_2_A")[6]
	buildA_8_num = build.get("round_2_A")[7]
	buildA_9_num = build.get("round_2_A")[8]
	buildA_10_num = build.get("round_2_A")[9]
	buildA_11_num = build.get("round_2_A")[10]

	if buildA_1_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_1.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[0]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_1.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_2_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_2.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[1]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_2.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_3_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_3.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[2]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_3.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_4_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_4.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[3]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_4.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_5_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_5.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[4]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_5.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_6_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_6.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[5]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_6.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_7_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_7.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[6]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_7.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_8_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_8.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[7]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_8.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_9_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_9.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_A")[8]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_9.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildA_10_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_10.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_1_A")[9]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_10.setStyleSheet(qss_charm)
		qss_charm = ""
		
	if buildA_11_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_A_11.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_1_A")[10]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_A_11.setStyleSheet(qss_charm)
		qss_charm = ""


	buildB_1_num = build.get("round_2_B")[0]
	buildB_2_num = build.get("round_2_B")[1]
	buildB_3_num = build.get("round_2_B")[2]
	buildB_4_num = build.get("round_2_B")[3]
	buildB_5_num = build.get("round_2_B")[4]
	buildB_6_num = build.get("round_2_B")[5]
	buildB_7_num = build.get("round_2_B")[6]
	buildB_8_num = build.get("round_2_B")[7]
	buildB_9_num = build.get("round_2_B")[8]
	buildB_10_num = build.get("round_2_B")[9]
	buildB_11_num = build.get("round_2_B")[10]

	if buildB_1_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_1.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[0]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_1.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_2_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_2.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[1]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_2.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_3_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_3.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[2]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_3.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_4_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_4.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[3]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_4.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_5_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_5.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[4]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_5.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_6_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_6.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[5]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_6.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_7_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_7.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[6]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_7.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_8_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_8.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[7]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_8.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_9_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_9.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_2_B")[8]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_9.setStyleSheet(qss_charm)
		qss_charm = ""

	if buildB_10_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_10.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_1_B")[9]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_10.setStyleSheet(qss_charm)
		qss_charm = ""
		
	if buildB_11_num == 0:
		qss_charm = qss_charm_p1 + "0" + qss_charm_p3
		self.r2_charm_B_11.setStyleSheet(qss_charm)
		qss_charm = ""
	else:
		build_current = build.get("round_1_B")[10]
		charm_name = charmData.get("charm_" + str(build_current))
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.r2_charm_B_11.setStyleSheet(qss_charm)
		qss_charm = ""