#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python_version : 3.13.0
#discription    : This defines the initial state of BP.
#author         : stellalalalalalalalalala
#created        : 2025.06.30
#last modified  : 2025.07.03


from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QButtonGroup

from Code.update import *
import json


def init_state(self, state, build):
	QFontDatabase.addApplicationFont( "Image/W03.TTF")
	pixmap_background = QPixmap("Image/background_radiance.png")

	with open("Text/Team_1.json", "r", encoding = "utf-8") as file:
		team_1_Data = json.load(file)

	self.actionTeam_A1.setText(team_1_Data["name_Team"])
	self.actionTeam_B1.setText(team_1_Data["name_Team"])

	with open("Text/Team_2.json", "r", encoding = "utf-8") as file:
		team_2_Data = json.load(file)

	self.actionTeam_A2.setText(team_2_Data["name_Team"])
	self.actionTeam_B2.setText(team_2_Data["name_Team"])

	with open("Text/Team_3.json", "r", encoding = "utf-8") as file:
		team_3_Data = json.load(file)

	self.actionTeam_A3.setText(team_3_Data["name_Team"])
	self.actionTeam_B3.setText(team_3_Data["name_Team"])

	with open("Text/Team_4.json", "r", encoding = "utf-8") as file:
		team_4_Data = json.load(file)

	self.actionTeam_A4.setText(team_4_Data["name_Team"])
	self.actionTeam_B4.setText(team_4_Data["name_Team"])

	self.background.setPixmap(pixmap_background)

	self.score_A.setAlignment(Qt.AlignmentFlag.AlignCenter)
	self.score_B.setAlignment(Qt.AlignmentFlag.AlignCenter)

	self.A_first.setEnabled(True)
	self.B_first.setEnabled(True)

	self.A_first.setChecked(False)
	self.B_first.setChecked(False)

	self.equip_A_1.setEnabled(False)
	self.equip_A_2.setEnabled(False)
	self.equip_A_3.setEnabled(False)
	self.equip_A_4.setEnabled(False)
	self.equip_A_5.setEnabled(False)
	self.equip_A_6.setEnabled(False)
	self.equip_A_7.setEnabled(False)
	self.equip_A_8.setEnabled(False)
	self.equip_A_9.setEnabled(False)
	self.equip_A_10.setEnabled(False)
	self.equip_A_11.setEnabled(False)

	self.equip_B_1.setEnabled(False)
	self.equip_B_2.setEnabled(False)
	self.equip_B_3.setEnabled(False)
	self.equip_B_4.setEnabled(False)
	self.equip_B_5.setEnabled(False)
	self.equip_B_6.setEnabled(False)
	self.equip_B_7.setEnabled(False)
	self.equip_B_8.setEnabled(False)
	self.equip_B_9.setEnabled(False)
	self.equip_B_10.setEnabled(False)
	self.equip_B_11.setEnabled(False)

	self.charm_A_1.setEnabled(True)
	self.charm_A_2.setEnabled(True)
	self.charm_A_3.setEnabled(True)
	self.charm_A_4.setEnabled(True)
	self.charm_A_5.setEnabled(True)
	self.charm_A_6.setEnabled(True)
	self.charm_A_7.setEnabled(True)
	self.charm_A_8.setEnabled(True)
	self.charm_A_9.setEnabled(True)
	self.charm_A_10.setEnabled(True)
	self.charm_A_11.setEnabled(True)
	self.charm_A_12.setEnabled(True)
	self.charm_A_13.setEnabled(True)
	self.charm_A_14.setEnabled(True)
	self.charm_A_15.setEnabled(True)
	self.charm_A_16.setEnabled(True)
	self.charm_A_17.setEnabled(True)
	self.charm_A_18.setEnabled(True)
	self.charm_A_19.setEnabled(True)
	self.charm_A_20.setEnabled(True)
	self.charm_A_21.setEnabled(True)
	self.charm_A_22.setEnabled(True)
	self.charm_A_23.setEnabled(True)
	self.charm_A_24.setEnabled(True)
	self.charm_A_25.setEnabled(True)
	self.charm_A_26.setEnabled(True)
	self.charm_A_27.setEnabled(True)
	self.charm_A_28.setEnabled(True)
	self.charm_A_29.setEnabled(True)
	self.charm_A_30.setEnabled(True)
	self.charm_A_31.setEnabled(True)
	self.charm_A_32.setEnabled(True)
	self.charm_A_33.setEnabled(True)
	self.charm_A_34.setEnabled(True)
	self.charm_A_35.setEnabled(True)
	self.charm_A_36.setEnabled(True)
	self.charm_A_37.setEnabled(True)
	self.charm_A_38.setEnabled(True)
	self.charm_A_39.setEnabled(True)

	self.charm_B_1.setEnabled(True)
	self.charm_B_2.setEnabled(True)
	self.charm_B_3.setEnabled(True)
	self.charm_B_4.setEnabled(True)
	self.charm_B_5.setEnabled(True)
	self.charm_B_6.setEnabled(True)
	self.charm_B_7.setEnabled(True)
	self.charm_B_8.setEnabled(True)
	self.charm_B_9.setEnabled(True)
	self.charm_B_10.setEnabled(True)
	self.charm_B_11.setEnabled(True)
	self.charm_B_12.setEnabled(True)
	self.charm_B_13.setEnabled(True)
	self.charm_B_14.setEnabled(True)
	self.charm_B_15.setEnabled(True)
	self.charm_B_16.setEnabled(True)
	self.charm_B_17.setEnabled(True)
	self.charm_B_18.setEnabled(True)
	self.charm_B_19.setEnabled(True)
	self.charm_B_20.setEnabled(True)
	self.charm_B_21.setEnabled(True)
	self.charm_B_22.setEnabled(True)
	self.charm_B_23.setEnabled(True)
	self.charm_B_24.setEnabled(True)
	self.charm_B_25.setEnabled(True)
	self.charm_B_26.setEnabled(True)
	self.charm_B_27.setEnabled(True)
	self.charm_B_28.setEnabled(True)
	self.charm_B_29.setEnabled(True)
	self.charm_B_30.setEnabled(True)
	self.charm_B_31.setEnabled(True)
	self.charm_B_32.setEnabled(True)
	self.charm_B_33.setEnabled(True)
	self.charm_B_34.setEnabled(True)
	self.charm_B_35.setEnabled(True)
	self.charm_B_36.setEnabled(True)
	self.charm_B_37.setEnabled(True)
	self.charm_B_38.setEnabled(True)
	self.charm_B_39.setEnabled(True)

	self.current_operation.setText("START")

	self.button_reset.setEnabled(True)
	self.button_confirm.setEnabled(True)
	self.button_next.setEnabled(True)

	update_team.update_team(self, state)
	update_binding.update_binding(self, state)
	update_notch.update_notch(self, state)
	update_equip.update_equip(self, state, build)
	update_round1.update_round1(self, state, build)
	update_round2.update_round2(self, state, build)
	update_charm.update_charm(self, state, build)
	update_operation.update_operation(self, state)
