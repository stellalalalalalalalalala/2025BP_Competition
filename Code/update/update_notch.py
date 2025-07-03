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

def update_notch(self, state):

	qss_notch_uncharmed = """
		QLabel {
			border-image: url("Image/notches/uncharmed.png") 0 0 0 0 strech strech; } """

	qss_notch_charmed = """
		QLabel {
			border-image: url("Image/notches/charmed.png") 0 0 0 0 strech strech; } """

	notch1_A_state = state.get("notch_A")[0]
	notch2_A_state = state.get("notch_A")[1]
	notch3_A_state = state.get("notch_A")[2]
	notch4_A_state = state.get("notch_A")[3]
	notch5_A_state = state.get("notch_A")[4]
	notch6_A_state = state.get("notch_A")[5]
	notch7_A_state = state.get("notch_A")[6]
	notch8_A_state = state.get("notch_A")[7]
	notch9_A_state = state.get("notch_A")[8]
	notch10_A_state = state.get("notch_A")[9]
	notch11_A_state = state.get("notch_A")[10]

	if notch1_A_state == 0:
		self.notch_A_1.setStyleSheet(qss_notch_uncharmed)
	elif notch1_A_state == 1:
		self.notch_A_1.setStyleSheet(qss_notch_charmed)
	else:
		return 0
        
	if notch2_A_state == 0:
		self.notch_A_2.setStyleSheet(qss_notch_uncharmed)
	elif notch2_A_state == 1:
		self.notch_A_2.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch3_A_state == 0:
		self.notch_A_3.setStyleSheet(qss_notch_uncharmed)
	elif notch3_A_state == 1:
		self.notch_A_3.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch4_A_state == 0:
		self.notch_A_4.setStyleSheet(qss_notch_uncharmed)
	elif notch4_A_state == 1:
		self.notch_A_4.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch5_A_state == 0:
		self.notch_A_5.setStyleSheet(qss_notch_uncharmed)
	elif notch5_A_state == 1:
		self.notch_A_5.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch6_A_state == 0:
		self.notch_A_6.setStyleSheet(qss_notch_uncharmed)
	elif notch6_A_state == 1:
		self.notch_A_6.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch7_A_state == 0:
		self.notch_A_7.setStyleSheet(qss_notch_uncharmed)
	elif notch7_A_state == 1:
		self.notch_A_7.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch8_A_state == 0:
		self.notch_A_8.setStyleSheet(qss_notch_uncharmed)
	elif notch8_A_state == 1:
		self.notch_A_8.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch9_A_state == 0:
		self.notch_A_9.setStyleSheet(qss_notch_uncharmed)
	elif notch9_A_state == 1:
		self.notch_A_9.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch10_A_state == 0:
		self.notch_A_10.setStyleSheet(qss_notch_uncharmed)
	elif notch10_A_state == 1:
		self.notch_A_10.setStyleSheet(qss_notch_charmed)
	else:
		return 0
        
	if notch11_A_state == 0:
		self.notch_A_11.setStyleSheet(qss_notch_uncharmed)
	elif notch11_A_state == 1:
		self.notch_A_11.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	notch1_B_state = state.get("notch_B")[0]
	notch2_B_state = state.get("notch_B")[1]
	notch3_B_state = state.get("notch_B")[2]
	notch4_B_state = state.get("notch_B")[3]
	notch5_B_state = state.get("notch_B")[4]
	notch6_B_state = state.get("notch_B")[5]
	notch7_B_state = state.get("notch_B")[6]
	notch8_B_state = state.get("notch_B")[7]
	notch9_B_state = state.get("notch_B")[8]
	notch10_B_state = state.get("notch_B")[9]
	notch11_B_state = state.get("notch_B")[10]

	if notch1_B_state == 0:
		self.notch_B_1.setStyleSheet(qss_notch_uncharmed)
	elif notch1_B_state == 1:
		self.notch_B_1.setStyleSheet(qss_notch_charmed)
	else:
		return 0
        
	if notch2_B_state == 0:
		self.notch_B_2.setStyleSheet(qss_notch_uncharmed)
	elif notch2_B_state == 1:
		self.notch_B_2.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch3_B_state == 0:
		self.notch_B_3.setStyleSheet(qss_notch_uncharmed)
	elif notch3_B_state == 1:
		self.notch_B_3.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch4_B_state == 0:
		self.notch_B_4.setStyleSheet(qss_notch_uncharmed)
	elif notch4_B_state == 1:
		self.notch_B_4.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch5_B_state == 0:
		self.notch_B_5.setStyleSheet(qss_notch_uncharmed)
	elif notch5_B_state == 1:
		self.notch_B_5.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch6_B_state == 0:
		self.notch_B_6.setStyleSheet(qss_notch_uncharmed)
	elif notch6_B_state == 1:
		self.notch_B_6.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch7_B_state == 0:
		self.notch_B_7.setStyleSheet(qss_notch_uncharmed)
	elif notch7_B_state == 1:
		self.notch_B_7.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch8_B_state == 0:
		self.notch_B_8.setStyleSheet(qss_notch_uncharmed)
	elif notch8_B_state == 1:
		self.notch_B_8.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	if notch9_B_state == 0:
		self.notch_B_9.setStyleSheet(qss_notch_uncharmed)
	elif notch9_B_state == 1:
		self.notch_B_9.setStyleSheet(qss_notch_charmed)
	else:
		return 0
        
	if notch10_B_state == 0:
		self.notch_B_10.setStyleSheet(qss_notch_uncharmed)
	elif notch10_B_state == 1:
		self.notch_B_10.setStyleSheet(qss_notch_charmed)
	else:
		return 0
        
	if notch11_B_state == 0:
		self.notch_B_11.setStyleSheet(qss_notch_uncharmed)
	elif notch11_B_state == 1:
		self.notch_B_11.setStyleSheet(qss_notch_charmed)
	else:
		return 0

	qss_overcharmed_A = """
		QLabel {
			border-image: url("Image/notches/overcharmed_A.png") 0 0 0 0 strech strech; } """

	qss_overcharmed_B = """
		QLabel {
			border-image: url("Image/notches/overcharmed_B.png") 0 0 0 0 strech strech; } """

	qss_normal_charmed = """
		QLabel {
			border-image: url("Image/notches/normal.png") 0 0 0 0 strech strech; } """

	if state["charmed_notchNum_A"] < 12:
		self.overcharmed_A.setStyleSheet(qss_normal_charmed)
	else:
		self.overcharmed_A.setStyleSheet(qss_overcharmed_A)


	if state["charmed_notchNum_B"] < 12:
		self.overcharmed_B.setStyleSheet(qss_normal_charmed)
	else:
		self.overcharmed_B.setStyleSheet(qss_overcharmed_B)