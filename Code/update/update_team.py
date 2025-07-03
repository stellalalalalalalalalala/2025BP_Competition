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

def update_team(self, state):

	team_A = state.get("team")[0]
	team_B = state.get("team")[1]

	round = state.get("round")
	step = state.get("step")

	if team_A != 0:
		with open("Text/Team_" + str(team_A) + ".json", "r", encoding = "utf-8") as file:
			team_A_Data = json.load(file)

		self.Name_A.setText(team_A_Data.get("name_Team"))
		self.Name_A1.setText(team_A_Data.get("name_member1"))
		self.Name_A2.setText(team_A_Data.get("name_member2"))
		self.Name_A3.setText(team_A_Data.get("name_member3"))

	else:
		self.Name_A.setText("AAAAAAAAAA")
		self.Name_A1.setText("AAAAAAAAA1")
		self.Name_A2.setText("AAAAAAAAA2")
		self.Name_A3.setText("AAAAAAAAA3")

	if team_B != 0:
		with open("Text/Team_" + str(team_B) + ".json", "r", encoding = "utf-8") as file:
			team_B_Data = json.load(file)

		self.Name_B.setText(team_B_Data.get("name_Team"))
		self.Name_B1.setText(team_B_Data.get("name_member1"))
		self.Name_B2.setText(team_B_Data.get("name_member2"))
		self.Name_B3.setText(team_B_Data.get("name_member3"))

	else:
		self.Name_B.setText("BBBBBBBBB")
		self.Name_B1.setText("BBBBBBBBB1")
		self.Name_B2.setText("BBBBBBBBB2")
		self.Name_B3.setText("BBBBBBBBB3")

	qss_highlight = """
		QLabel {
			border-image: url("Image/name_highlight.png")  0 0 0 0 stretch stretch;
			color: #FFFFFF;  }"""

	qss_plain = """
		QLabel {
			border-image: url("Image/name_plain.png") 0 0 0 0 strech stretch; 
			color: #000000; }"""

	if round == 0:

		self.Name_A1.setStyleSheet(qss_plain)
		self.Name_A2.setStyleSheet(qss_plain)
		self.Name_A3.setStyleSheet(qss_plain)

		self.Name_B1.setStyleSheet(qss_plain)
		self.Name_B2.setStyleSheet(qss_plain)
		self.Name_B3.setStyleSheet(qss_plain)

		if step == 0:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 1:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 2:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 3:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 4:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 5:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 6:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 7:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 8:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 9:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 10:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 11:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 12:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 13:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		elif step == 14:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 15:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_highlight)

		elif step == 16:
			self.Name_A1.setStyleSheet(qss_highlight)
			self.Name_B1.setStyleSheet(qss_plain)

		else:
			self.Name_A1.setStyleSheet(qss_plain)
			self.Name_B1.setStyleSheet(qss_plain)

	elif round == 1:

		self.Name_A1.setStyleSheet(qss_plain)
		self.Name_A2.setStyleSheet(qss_plain)
		self.Name_A3.setStyleSheet(qss_plain)

		self.Name_B1.setStyleSheet(qss_plain)
		self.Name_B2.setStyleSheet(qss_plain)
		self.Name_B3.setStyleSheet(qss_plain)

		if step == 0:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 1:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 2:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_highlight)

		elif step == 3:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 4:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_highlight)

		elif step == 5:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 6:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_highlight)

		elif step == 7:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_highlight)

		elif step == 8:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 9:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_highlight)

		elif step == 10:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 11:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 12:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_highlight)

		elif step == 13:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 14:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_highlight)

		elif step == 15:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_plain)

		elif step == 16:
			self.Name_A2.setStyleSheet(qss_highlight)
			self.Name_B2.setStyleSheet(qss_plain)

		else:
			self.Name_A2.setStyleSheet(qss_plain)
			self.Name_B2.setStyleSheet(qss_plain)

	elif round == 2:

		self.Name_A1.setStyleSheet(qss_plain)
		self.Name_A2.setStyleSheet(qss_plain)
		self.Name_A3.setStyleSheet(qss_plain)

		self.Name_B1.setStyleSheet(qss_plain)
		self.Name_B2.setStyleSheet(qss_plain)
		self.Name_B3.setStyleSheet(qss_plain)

		if step == 0:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 1:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 2:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_highlight)

		elif step == 3:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 4:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_highlight)

		elif step == 5:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 6:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_highlight)

		elif step == 7:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_highlight)

		elif step == 8:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 9:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_highlight)

		elif step == 10:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 11:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 12:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_highlight)

		elif step == 13:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 14:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_highlight)

		elif step == 15:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_plain)

		elif step == 16:
			self.Name_A3.setStyleSheet(qss_highlight)
			self.Name_B3.setStyleSheet(qss_plain)

		else:
			self.Name_A3.setStyleSheet(qss_plain)
			self.Name_B3.setStyleSheet(qss_plain)

	else:
		self.Name_A1.setStyleSheet(qss_plain)
		self.Name_A2.setStyleSheet(qss_plain)
		self.Name_A3.setStyleSheet(qss_plain)

		self.Name_B1.setStyleSheet(qss_plain)
		self.Name_B2.setStyleSheet(qss_plain)
		self.Name_B3.setStyleSheet(qss_plain)
