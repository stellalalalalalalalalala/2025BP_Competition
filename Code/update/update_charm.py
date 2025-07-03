#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python_version : 3.13.0
#discription    : This defines the action that updates push button for bindings.
#author         : stellalalalalalalalalala
#created        : 2025.06.30
#last modified  : 2025.07.02


from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton

import json

def update_charm(self, state, build):


	if (state["step"] == 3) or (state["step"] == 6) or (state["step"] == 8)  or (state["step"] == 10)  or (state["step"] == 11)  or (state["step"] == 13)  or (state["step"] == 16):
		step_A = True
		step_B = False
	elif (state["step"] == 4) or (state["step"] == 5) or (state["step"] == 7)  or (state["step"] == 9)  or (state["step"] == 12)  or (state["step"] == 14)  or (state["step"] == 15):
		step_A = False
		step_B = True
	elif (state["step"] == 1) or (state["step"] == 2):
		step_A = False
		step_B = False
	else:
		step_A = True
		step_B = True

	with open("Text/CharmData.json", "r") as file:
		charmData = json.load(file)

	qss_charm_p1= """
		QPushButton {
			border-image: url("Image/charms/"""

	if state["Fury"] == False:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = "inactive_Fury"
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3

		self.charm_A_20.setStyleSheet(qss_charm)
		self.charm_B_20.setStyleSheet(qss_charm)

		self.charm_A_20.setEnabled(state["Fury"])
		self.charm_B_20.setEnabled(state["Fury"])

		qss_charm = ""

	charmA_1_state = state.get("charm_A")[0]
	charmA_2_state = state.get("charm_A")[1]
	charmA_3_state = state.get("charm_A")[2]
	charmA_4_state = state.get("charm_A")[3]
	charmA_5_state = state.get("charm_A")[4]
	charmA_6_state = state.get("charm_A")[5]
	charmA_7_state = state.get("charm_A")[6]
	charmA_8_state = state.get("charm_A")[7]
	charmA_9_state = state.get("charm_A")[8]
	charmA_10_state = state.get("charm_A")[9]
	charmA_11_state = state.get("charm_A")[10]
	charmA_12_state = state.get("charm_A")[11]
	charmA_13_state = state.get("charm_A")[12]
	charmA_14_state = state.get("charm_A")[13]
	charmA_15_state = state.get("charm_A")[14]
	charmA_16_state = state.get("charm_A")[15]
	charmA_17_state = state.get("charm_A")[16]
	charmA_18_state = state.get("charm_A")[17]
	charmA_19_state = state.get("charm_A")[18]
	charmA_20_state = state.get("charm_A")[19]
	charmA_21_state = state.get("charm_A")[20]
	charmA_22_state = state.get("charm_A")[21]
	charmA_23_state = state.get("charm_A")[22]
	charmA_24_state = state.get("charm_A")[23]
	charmA_25_state = state.get("charm_A")[24]
	charmA_26_state = state.get("charm_A")[25]
	charmA_27_state = state.get("charm_A")[26]
	charmA_28_state = state.get("charm_A")[27]
	charmA_29_state = state.get("charm_A")[28]
	charmA_30_state = state.get("charm_A")[29]
	charmA_31_state = state.get("charm_A")[30]
	charmA_32_state = state.get("charm_A")[31]
	charmA_33_state = state.get("charm_A")[32]
	charmA_34_state = state.get("charm_A")[33]
	charmA_35_state = state.get("charm_A")[34]
	charmA_36_state = state.get("charm_A")[35]
	charmA_37_state = state.get("charm_A")[36]
	charmA_38_state = state.get("charm_A")[37]
	charmA_39_state = state.get("charm_A")[38]

	if charmA_1_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_1"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_1.setEnabled(True & step_A)
		self.charm_A_1.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_1_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_1"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_1.setEnabled(True & step_A)
		self.charm_A_1.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_1_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_1.setStyleSheet(qss_charm)
		qss_charm = ""
		self.charm_A_1.setEnabled(False)

	if charmA_2_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_2"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_2.setEnabled(True & step_A)
		self.charm_A_2.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_2_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_2"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_2.setEnabled(True & step_A)
		self.charm_A_2.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_2_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_2.setEnabled(False)
		self.charm_A_2.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_3_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_3"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_3.setEnabled(True & step_A)
		self.charm_A_3.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_3_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_3"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_3.setEnabled(True & step_A)
		self.charm_A_3.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_3_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_13.setEnabled(False)
		self.charm_A_3.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_4_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_4"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_4.setEnabled(True & step_A)
		self.charm_A_4.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_4_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_4"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_4.setEnabled(True & step_A)
		self.charm_A_4.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_4_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_4.setEnabled(False)
		self.charm_A_4.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_5_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_5"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_5.setEnabled(True & step_A)
		self.charm_A_5.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_5_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_5"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_5.setEnabled(True & step_A)
		self.charm_A_5.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_5_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_5.setEnabled(False)
		self.charm_A_5.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_6_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_6"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_6.setEnabled(True & step_A)
		self.charm_A_6.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_6_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_6"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_6.setEnabled(True & step_A)
		self.charm_A_6.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_6_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_6.setEnabled(False)
		self.charm_A_6.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_7_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_7"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_7.setEnabled(True & step_A)
		self.charm_A_7.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_7_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_7"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_7.setEnabled(True & step_A)
		self.charm_A_7.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_7_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_7.setEnabled(False)
		self.charm_A_7.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_8_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_8"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_8.setEnabled(True & step_A)
		self.charm_A_8.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_8_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_8"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_8.setEnabled(True & step_A)
		self.charm_A_8.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_8_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_8.setEnabled(False)
		self.charm_A_8.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_9_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_9"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_9.setEnabled(True & step_A)
		self.charm_A_9.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_9_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_9"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_9.setEnabled(True & step_A)
		self.charm_A_9.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_9_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_9.setEnabled(False)
		self.charm_A_9.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_10_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_10"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_10.setEnabled(True & step_A)
		self.charm_A_10.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_10_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_10"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_10.setEnabled(True & step_A)
		self.charm_A_10.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_10_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_10.setEnabled(False)
		self.charm_A_10.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_11_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_11"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_11.setEnabled(True & step_A)
		self.charm_A_11.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_11_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_11"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_11.setEnabled(True & step_A)
		self.charm_A_11.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_11_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_11.setEnabled(False)
		self.charm_A_11.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_12_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_12"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_12.setEnabled(True & step_A)
		self.charm_A_12.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_12_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_12"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_12.setEnabled(True & step_A)
		self.charm_A_12.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_12_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_12.setEnabled(False)
		self.charm_A_12.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_13_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_13"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_13.setEnabled(True & step_A)
		self.charm_A_13.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_13_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_13"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_13.setEnabled(True & step_A)
		self.charm_A_13.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_13_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_13.setEnabled(False)
		self.charm_A_13.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_14_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_14"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_14.setEnabled(True & step_A)
		self.charm_A_14.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_14_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_14"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_14.setEnabled(True & step_A)
		self.charm_A_14.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_14_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_14.setEnabled(False)
		self.charm_A_14.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_15_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_15"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_15.setEnabled(True & step_A)
		self.charm_A_15.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_15_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_15"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_15.setEnabled(True & step_A)
		self.charm_A_15.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_15_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_15.setEnabled(False)
		self.charm_A_15.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_16_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_16"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_16.setEnabled(True & step_A)
		self.charm_A_16.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_16_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_16"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_16.setEnabled(True & step_A)
		self.charm_A_16.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_16_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_16.setEnabled(False)
		self.charm_A_16.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_17_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_17"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_17.setEnabled(True & step_A)
		self.charm_A_17.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_17_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_17"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_17.setEnabled(True & step_A)
		self.charm_A_17.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_17_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_17.setEnabled(False)
		self.charm_A_17.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_18_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_18"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_18.setEnabled(True & step_A)
		self.charm_A_18.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_18_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_18"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_18.setEnabled(True & step_A)
		self.charm_A_18.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_18_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_18.setEnabled(False)
		self.charm_A_18.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_19_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_19"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_19.setEnabled(True & step_A)
		self.charm_A_19.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_19_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_19"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_19.setEnabled(True & step_A)
		self.charm_A_19.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_19_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_19.setEnabled(False)
		self.charm_A_19.setStyleSheet(qss_charm)
		qss_charm = ""

	if (charmA_20_state == 0) & state["Fury"]:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_20"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_20.setEnabled(True & step_A)
		self.charm_A_20.setStyleSheet(qss_charm)
		qss_charm = ""

	elif (charmA_20_state == 1) & state["Fury"]:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_20"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_20.setEnabled(True & step_A)
		self.charm_A_20.setStyleSheet(qss_charm)
		qss_charm = ""

	elif (charmA_20_state == 2) & state["Fury"]:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_20.setEnabled(False)
		self.charm_A_20.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_21_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_21"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_21.setEnabled(True & step_A)
		self.charm_A_21.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_21_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_21"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_21.setEnabled(True & step_A)
		self.charm_A_21.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_21_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_21.setEnabled(False)
		self.charm_A_21.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_22_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_22"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_22.setEnabled(True & step_A)
		self.charm_A_22.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_22_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_22"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_22.setEnabled(True & step_A)
		self.charm_A_22.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_22_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_22.setEnabled(False)
		self.charm_A_22.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_23_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_23"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_23.setEnabled(True & step_A)
		self.charm_A_23.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_23_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_23"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_23.setEnabled(True & step_A)
		self.charm_A_23.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_23_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_23.setEnabled(False)
		self.charm_A_23.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_24_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_24"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_24.setEnabled(True & step_A)
		self.charm_A_24.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_24_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_24"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_24.setEnabled(True & step_A)
		self.charm_A_24.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_24_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_24.setEnabled(False)
		self.charm_A_24.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_25_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_25"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_25.setEnabled(True & step_A)
		self.charm_A_25.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_25_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_25"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_25.setEnabled(True & step_A)
		self.charm_A_25.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_25_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_25.setEnabled(False)
		self.charm_A_25.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_26_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_26"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_26.setEnabled(True & step_A)
		self.charm_A_26.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_26_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_26"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_26.setEnabled(True & step_A)
		self.charm_A_26.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_26_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_26.setEnabled(False)
		self.charm_A_26.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_27_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_27"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_27.setEnabled(True & step_A)
		self.charm_A_27.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_27_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_27"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_27.setEnabled(True & step_A)
		self.charm_A_27.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_27_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_27.setEnabled(False)
		self.charm_A_27.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_28_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_28"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_28.setEnabled(True & step_A)
		self.charm_A_28.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_28_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_28"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_28.setEnabled(True & step_A)
		self.charm_A_28.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_28_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_28.setEnabled(False)
		self.charm_A_28.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_29_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_29"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_29.setEnabled(True & step_A)
		self.charm_A_29.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_29_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_29"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_29.setEnabled(True & step_A)
		self.charm_A_29.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_29_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_29.setEnabled(False)
		self.charm_A_29.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_30_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_30"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_30.setEnabled(True & step_A)
		self.charm_A_30.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_30_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_30"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_30.setEnabled(True & step_A)
		self.charm_A_30.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_30_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_31.setEnabled(False)
		self.charm_A_30.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_31_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_31"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_31.setEnabled(True & step_A)
		self.charm_A_31.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_31_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_31"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_31.setEnabled(True & step_A)
		self.charm_A_31.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_31_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_31.setEnabled(False)
		self.charm_A_31.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_32_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_32"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_32.setEnabled(True & step_A)
		self.charm_A_32.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_32_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_32"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_32.setEnabled(True & step_A)
		self.charm_A_32.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_32_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_32.setEnabled(False)
		self.charm_A_32.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_33_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_33"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_33.setEnabled(True & step_A)
		self.charm_A_33.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_33_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_33"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_33.setEnabled(True & step_A)
		self.charm_A_33.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_33_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_33.setEnabled(False)
		self.charm_A_33.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_34_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_34"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_34.setEnabled(True & step_A)
		self.charm_A_34.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_34_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_34"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_34.setEnabled(True & step_A)
		self.charm_A_34.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_34_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_34.setEnabled(False)
		self.charm_A_34.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_35_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_35"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_35.setEnabled(True & step_A)
		self.charm_A_35.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_35_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_35"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_35.setEnabled(True & step_A)
		self.charm_A_35.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_35_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_35.setEnabled(False)
		self.charm_A_35.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_36_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_36"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_36.setEnabled(True & step_A)
		self.charm_A_36.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_36_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_36"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_36.setEnabled(True & step_A)
		self.charm_A_36.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_36_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_36.setEnabled(False)
		self.charm_A_36.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_37_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_37"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_37.setEnabled(True & step_A)
		self.charm_A_37.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_37_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_37"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_37.setEnabled(True & step_A)
		self.charm_A_37.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_37_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_37.setEnabled(False)
		self.charm_A_37.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_38_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_38"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_38.setEnabled(True & step_A)
		self.charm_A_38.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_38_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_38"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_38.setEnabled(True & step_A)
		self.charm_A_38.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_38_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_38.setEnabled(False)
		self.charm_A_38.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmA_39_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_39"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_39.setEnabled(True & step_A)
		self.charm_A_39.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_39_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_39"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_A_39.setEnabled(True & step_A)
		self.charm_A_39.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmA_39_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_A_39.setEnabled(False)
		self.charm_A_39.setStyleSheet(qss_charm)
		qss_charm = ""

	charmB_1_state = state.get("charm_B")[0]
	charmB_2_state = state.get("charm_B")[1]
	charmB_3_state = state.get("charm_B")[2]
	charmB_4_state = state.get("charm_B")[3]
	charmB_5_state = state.get("charm_B")[4]
	charmB_6_state = state.get("charm_B")[5]
	charmB_7_state = state.get("charm_B")[6]
	charmB_8_state = state.get("charm_B")[7]
	charmB_9_state = state.get("charm_B")[8]
	charmB_10_state = state.get("charm_B")[9]
	charmB_11_state = state.get("charm_B")[10]
	charmB_12_state = state.get("charm_B")[11]
	charmB_13_state = state.get("charm_B")[12]
	charmB_14_state = state.get("charm_B")[13]
	charmB_15_state = state.get("charm_B")[14]
	charmB_16_state = state.get("charm_B")[15]
	charmB_17_state = state.get("charm_B")[16]
	charmB_18_state = state.get("charm_B")[17]
	charmB_19_state = state.get("charm_B")[18]
	charmB_20_state = state.get("charm_B")[19]
	charmB_21_state = state.get("charm_B")[20]
	charmB_22_state = state.get("charm_B")[21]
	charmB_23_state = state.get("charm_B")[22]
	charmB_24_state = state.get("charm_B")[23]
	charmB_25_state = state.get("charm_B")[24]
	charmB_26_state = state.get("charm_B")[25]
	charmB_27_state = state.get("charm_B")[26]
	charmB_28_state = state.get("charm_B")[27]
	charmB_29_state = state.get("charm_B")[28]
	charmB_30_state = state.get("charm_B")[29]
	charmB_31_state = state.get("charm_B")[30]
	charmB_32_state = state.get("charm_B")[31]
	charmB_33_state = state.get("charm_B")[32]
	charmB_34_state = state.get("charm_B")[33]
	charmB_35_state = state.get("charm_B")[34]
	charmB_36_state = state.get("charm_B")[35]
	charmB_37_state = state.get("charm_B")[36]
	charmB_38_state = state.get("charm_B")[37]
	charmB_39_state = state.get("charm_B")[38]

	if charmB_1_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_1"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_1.setEnabled(True & step_B)
		self.charm_B_1.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_1_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_1"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_1.setEnabled(True & step_B)
		self.charm_B_1.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_1_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_1.setStyleSheet(qss_charm)
		qss_charm = ""
		self.charm_B_1.setEnabled(False)

	if charmB_2_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_2"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_2.setEnabled(True & step_B)
		self.charm_B_2.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_2_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_2"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_2.setEnabled(True & step_B)
		self.charm_B_2.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_2_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_2.setEnabled(False)
		self.charm_B_2.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_3_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_3"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_3.setEnabled(True & step_B)
		self.charm_B_3.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_3_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_3"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_3.setEnabled(True & step_B)
		self.charm_B_3.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_3_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_3.setEnabled(False)
		self.charm_B_3.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_4_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_4"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_4.setEnabled(True & step_B)
		self.charm_B_4.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_4_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_4"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_4.setEnabled(True & step_B)
		self.charm_B_4.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_4_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_4.setEnabled(False)
		self.charm_B_4.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_5_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_5"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_5.setEnabled(True & step_B)
		self.charm_B_5.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_5_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_5"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_5.setEnabled(True & step_B)
		self.charm_B_5.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_5_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_5.setEnabled(False)
		self.charm_B_5.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_6_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_6"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_6.setEnabled(True & step_B)
		self.charm_B_6.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_6_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_6"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_6.setEnabled(True & step_B)
		self.charm_B_6.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_6_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_6.setEnabled(False)
		self.charm_B_6.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_7_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_7"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_7.setEnabled(True & step_B)
		self.charm_B_7.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_7_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_7"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_7.setEnabled(True & step_B)
		self.charm_B_7.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_7_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_7.setEnabled(False)
		self.charm_B_7.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_8_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_8"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_8.setEnabled(True & step_B)
		self.charm_B_8.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_8_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_8"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_8.setEnabled(True & step_B)
		self.charm_B_8.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_8_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_8.setEnabled(False)
		self.charm_B_8.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_9_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_9"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_9.setEnabled(True & step_B)
		self.charm_B_9.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_9_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_9"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_9.setEnabled(True & step_B)
		self.charm_B_9.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_9_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_9.setEnabled(False)
		self.charm_B_9.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_10_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_10"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_10.setEnabled(True & step_B)
		self.charm_B_10.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_10_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_10"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_10.setEnabled(True & step_B)
		self.charm_B_10.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_10_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_10.setEnabled(False)
		self.charm_B_10.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_11_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_11"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_11.setEnabled(True & step_B)
		self.charm_B_11.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_11_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_11"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_11.setEnabled(True & step_B)
		self.charm_B_11.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_11_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_11.setEnabled(False)
		self.charm_B_11.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_12_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_12"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_12.setEnabled(True & step_B)
		self.charm_B_12.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_12_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_12"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_12.setEnabled(True & step_B)
		self.charm_B_12.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_12_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_12.setEnabled(False)
		self.charm_B_12.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_13_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_13"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_13.setEnabled(True & step_B)
		self.charm_B_13.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_13_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_13"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_13.setEnabled(True & step_B)
		self.charm_B_13.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_13_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_13.setEnabled(False)
		self.charm_B_13.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_14_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_14"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_14.setEnabled(True & step_B)
		self.charm_B_14.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_14_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_14"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_14.setEnabled(True & step_B)
		self.charm_B_14.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_14_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_14.setEnabled(False)
		self.charm_B_14.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_15_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_15"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_15.setEnabled(True & step_B)
		self.charm_B_15.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_15_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_15"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_15.setEnabled(True & step_B)
		self.charm_B_15.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_15_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_15.setEnabled(False)
		self.charm_B_15.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_16_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_16"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_16.setEnabled(True & step_B)
		self.charm_B_16.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_16_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_16"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_16.setEnabled(True & step_B)
		self.charm_B_16.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_16_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_16.setEnabled(False)
		self.charm_B_16.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_17_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_17"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_17.setEnabled(True & step_B)
		self.charm_B_17.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_17_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_17"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_17.setEnabled(True & step_B)
		self.charm_B_17.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_17_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_17.setEnabled(False)
		self.charm_B_17.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_18_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_18"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_18.setEnabled(True & step_B)
		self.charm_B_18.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_18_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_18"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_18.setEnabled(True & step_B)
		self.charm_B_18.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_18_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_18.setEnabled(False)
		self.charm_B_18.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_19_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_19"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_19.setEnabled(True & step_B)
		self.charm_B_19.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_19_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_19"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_19.setEnabled(True & step_B)
		self.charm_B_19.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_19_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_19.setEnabled(False)
		self.charm_B_19.setStyleSheet(qss_charm)
		qss_charm = ""

	if (charmB_20_state == 0)  & state["Fury"]:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_20"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_20.setEnabled(True & step_B)
		self.charm_B_20.setStyleSheet(qss_charm)
		qss_charm = ""

	elif (charmB_20_state == 1) & state["Fury"]:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_20"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_20.setEnabled(True & step_B)
		self.charm_B_20.setStyleSheet(qss_charm)
		qss_charm = ""

	elif (charmB_20_state == 2) & state["Fury"]:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_20.setEnabled(False)
		self.charm_B_20.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_21_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_21"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_21.setEnabled(True & step_B)
		self.charm_B_21.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_21_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_21"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_21.setEnabled(True & step_B)
		self.charm_B_21.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_21_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_21.setEnabled(False)
		self.charm_B_21.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_22_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_22"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_22.setEnabled(True & step_B)
		self.charm_B_22.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_22_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_22"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_22.setEnabled(True & step_B)
		self.charm_B_22.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_22_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_22.setEnabled(False)
		self.charm_B_22.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_23_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_23"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_23.setEnabled(True & step_B)
		self.charm_B_23.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_23_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_23"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_23.setEnabled(True & step_B)
		self.charm_B_23.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_23_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_23.setEnabled(False)
		self.charm_B_23.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_24_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_24"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_24.setEnabled(True & step_B)
		self.charm_B_24.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_24_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_24"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_24.setEnabled(True & step_B)
		self.charm_B_24.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_24_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_24.setEnabled(False)
		self.charm_B_24.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_25_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_25"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_25.setEnabled(True & step_B)
		self.charm_B_25.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_25_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_25"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_25.setEnabled(True & step_B)
		self.charm_B_25.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_25_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_25.setEnabled(False)
		self.charm_B_25.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_26_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_26"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_26.setEnabled(True & step_B)
		self.charm_B_26.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_26_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_26"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_26.setEnabled(True & step_B)
		self.charm_B_26.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_26_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_26.setEnabled(False)
		self.charm_B_26.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_27_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_27"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_27.setEnabled(True & step_B)
		self.charm_B_27.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_27_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_27"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_27.setEnabled(True & step_B)
		self.charm_B_27.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_27_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_27.setEnabled(False)
		self.charm_B_27.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_28_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_28"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_28.setEnabled(True & step_B)
		self.charm_B_28.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_28_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_28"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_28.setEnabled(True & step_B)
		self.charm_B_28.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_28_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_28.setEnabled(False)
		self.charm_B_28.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_29_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_29"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_29.setEnabled(True & step_B)
		self.charm_B_29.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_29_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_29"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_29.setEnabled(True & step_B)
		self.charm_B_29.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_29_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_29.setEnabled(False)
		self.charm_B_29.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_30_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_30"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_30.setEnabled(True & step_B)
		self.charm_B_30.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_30_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_30"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_30.setEnabled(True & step_B)
		self.charm_B_30.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_30_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_31.setEnabled(False)
		self.charm_B_30.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_31_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_31"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_31.setEnabled(True & step_B)
		self.charm_B_31.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_31_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_31"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_31.setEnabled(True & step_B)
		self.charm_B_31.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_31_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_31.setEnabled(False)
		self.charm_B_31.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_32_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_32"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_32.setEnabled(True & step_B)
		self.charm_B_32.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_32_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_32"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_32.setEnabled(True & step_B)
		self.charm_B_32.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_32_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_32.setEnabled(False)
		self.charm_B_32.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_33_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_33"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_33.setEnabled(True & step_B)
		self.charm_B_33.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_33_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_33"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_33.setEnabled(True & step_B)
		self.charm_B_33.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_33_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_33.setEnabled(False)
		self.charm_B_33.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_34_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_34"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_34.setEnabled(True & step_B)
		self.charm_B_34.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_34_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_34"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_34.setEnabled(True & step_B)
		self.charm_B_34.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_34_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_34.setEnabled(False)
		self.charm_B_34.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_35_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_35"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_35.setEnabled(True & step_B)
		self.charm_B_35.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_35_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_35"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_35.setEnabled(True & step_B)
		self.charm_B_35.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_35_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_35.setEnabled(False)
		self.charm_B_35.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_36_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_36"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_36.setEnabled(True & step_B)
		self.charm_B_36.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_36_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_36"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_36.setEnabled(True & step_B)
		self.charm_B_36.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_36_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_36.setEnabled(False)
		self.charm_B_36.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_37_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_37"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_37.setEnabled(True & step_B)
		self.charm_B_37.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_37_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_37"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_37.setEnabled(True & step_B)
		self.charm_B_37.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_37_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_37.setEnabled(False)
		self.charm_B_37.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_38_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_38"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_38.setEnabled(True & step_B)
		self.charm_B_38.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_38_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_38"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_38.setEnabled(True & step_B)
		self.charm_B_38.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_38_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_38.setEnabled(False)
		self.charm_B_38.setStyleSheet(qss_charm)
		qss_charm = ""

	if charmB_39_state == 0:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; }
			QPushButton:hover {
				background-color: none;
				background-image: url("Image/charms/hoven.png"); 
				background-repeat: no-repeat;
				background-position: center; }
			QPushButton:pressed {
				background-color: none;
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_39"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_39.setEnabled(True & step_B)
		self.charm_B_39.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_39_state == 1:

		qss_charm_p3 = """.png") 0 0 0 0 strech strech; 
				background-image: url("Image/charms/frame.png"); 
				background-repeat: no-repeat;
				background-position: center; } """
		charm_name = charmData["charm_39"]
		qss_charm = qss_charm_p1 + charm_name + qss_charm_p3
		self.charm_B_39.setEnabled(True & step_B)
		self.charm_B_39.setStyleSheet(qss_charm)
		qss_charm = ""

	elif charmB_39_state == 2:

		qss_charm = 	"""
			QPushButton {
				border-image: url("Image/charms/empty.png") 0 0 0 0 stretch stretch; } """	
		self.charm_B_39.setEnabled(False)
		self.charm_B_39.setStyleSheet(qss_charm)
		qss_charm = ""