#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python_version : 3.13.0
#discription    : This is the main function of BP App.
#author         : stellalalalalalalalalala
#created        : 2025.06.30
#last modified  : 2025.07.02


import sys, os

basedir = os.path.dirname(__file__)
os.chdir(basedir)

from PyQt6 import QtWidgets, QtGui, QtCore, QtMultimedia
from PyQt6.QtWidgets import QWidget, QRadioButton
from PyQt6.QtGui import QPixmap, QPalette
from PyQt6.QtCore import pyqtSignal, QUrl, QSize
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from Code import ui_BP, init_state, update, reset, next

import json

state = {
	"team" : [0, 0],
	"binding_A" : [0, 0, 0],  # order:[nail, mask, soul], 0: origin, 1: chosen, 2: faded, 3: disable
	"binding_B" : [0, 0, 0],
	"charm_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # charm order, 0: unequipped, 1: equipped
	"charm_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"notch_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # notch order, 0: uncharmed, 1: charmed
	"notch_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"charmed_notchNum_A" : 0,
	"charmed_notchNum_B" : 0,
	"equip_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # charm order, charm number
	"equip_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"step" : 0,  # 0<=step<=18
	"round" : 0,  # 0<=round <=2
	"Fury" : True
}

build = {
	"chosen_A" : [], 
	"current_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"round_1_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"round_2_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

	"chosen_B" : [],
	"current_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"round_1_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	"round_2_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}


class window_reset(QWidget, reset.Ui_ask_reset):
	win_reset_closed = pyqtSignal()

	def __init__(self):
		super(window_reset, self).__init__()
		self.setupUi(self)
		
		global state
		self.yes.clicked.connect(self.reset_yes)
		self.no.clicked.connect(self.close)

	def reset_yes(self):
		global state
		global build

		state = {
			"team" : [0, 0],
			"binding_A" : [0, 0, 0],  # order:[nail, mask, soul], 0: origin, 1: chosen, 2: faded, 3: disable
			"binding_B" : [0, 0, 0],
			"charm_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # charm order, 0: unequipped, 1: equipped
			"charm_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			"notch_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # notch order, 0: uncharmed, 1: charmed
			"notch_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			"charmed_notchNum_A" : 0,
			"charmed_notchNum_B" : 0,
			"equip_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # charm order, charm number
			"equip_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			"step" : 0,  # 0<=step<=18
			"round" : 0,  # 0<=round <=2
			"Fury" : True
		}

		build = {
			"chosen_A" : [], 
			"current_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			"round_1_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			"round_2_A" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

			"chosen_B" : [],
			"current_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			"round_1_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			"round_2_B" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		}

		self.win_reset_closed.emit()
		self.close()


class window_next(QWidget, next.Ui_ask_next):
	win_next_closed = pyqtSignal()

	def __init__(self):
		super(window_next, self).__init__()
		self.setupUi(self)
		
		self.yes.clicked.connect(self.next_yes)
		self.no.clicked.connect(self.close)

	def next_yes(self):
		self.win_next_closed.emit()
		self.close()


class window_BP(QWidget, ui_BP.Ui_BP):

	def __init__(self):
		super(window_BP, self).__init__()

		self.aspect_ratio = 16/9
		self.resize(1920, 1080)

		self.setupUi(self)

		global state
		global build
		init_state.init_state(self, state, build)

		self.A_first.clicked.connect(self.update_order_A)
		self.B_first.clicked.connect(self.update_order_B)
	
		self.actionyes.triggered.connect(self.deactivate_Fury)
		self.actionno.triggered.connect(self.activate_Fury)

		self.actionTeam_A1.triggered.connect(self.pick_Team_A1)
		self.actionTeam_A2.triggered.connect(self.pick_Team_A2)
		self.actionTeam_A3.triggered.connect(self.pick_Team_A3)
		self.actionTeam_A4.triggered.connect(self.pick_Team_A4)
		self.actionTeam_B1.triggered.connect(self.pick_Team_B1)
		self.actionTeam_B2.triggered.connect(self.pick_Team_B2)
		self.actionTeam_B3.triggered.connect(self.pick_Team_B3)
		self.actionTeam_B4.triggered.connect(self.pick_Team_B4)

		self.button_reset.clicked.connect(self.reset_state)
		self.button_confirm.clicked.connect(self.confirm_state)
		self.button_next.clicked.connect(self.next_round)

		self.reset = window_reset()
		self.next = window_next()

		self.binding_nail_A.clicked.connect(self.update_nail_A)
		self.binding_mask_A.clicked.connect(self.update_mask_A)
		self.binding_soul_A.clicked.connect(self.update_soul_A)

		self.binding_nail_B.clicked.connect(self.update_nail_B)
		self.binding_mask_B.clicked.connect(self.update_mask_B)
		self.binding_soul_B.clicked.connect(self.update_soul_B)

		self.charm_A_1.clicked.connect(self.update_charm_A_1)
		self.charm_A_2.clicked.connect(self.update_charm_A_2)
		self.charm_A_3.clicked.connect(self.update_charm_A_3)
		self.charm_A_4.clicked.connect(self.update_charm_A_4)
		self.charm_A_5.clicked.connect(self.update_charm_A_5)
		self.charm_A_6.clicked.connect(self.update_charm_A_6)
		self.charm_A_7.clicked.connect(self.update_charm_A_7)
		self.charm_A_8.clicked.connect(self.update_charm_A_8)
		self.charm_A_9.clicked.connect(self.update_charm_A_9)
		self.charm_A_10.clicked.connect(self.update_charm_A_10)
		self.charm_A_11.clicked.connect(self.update_charm_A_11)
		self.charm_A_12.clicked.connect(self.update_charm_A_12)
		self.charm_A_13.clicked.connect(self.update_charm_A_13)
		self.charm_A_14.clicked.connect(self.update_charm_A_14)
		self.charm_A_15.clicked.connect(self.update_charm_A_15)
		self.charm_A_16.clicked.connect(self.update_charm_A_16)
		self.charm_A_17.clicked.connect(self.update_charm_A_17)
		self.charm_A_18.clicked.connect(self.update_charm_A_18)
		self.charm_A_19.clicked.connect(self.update_charm_A_19)
		self.charm_A_20.clicked.connect(self.update_charm_A_20)
		self.charm_A_21.clicked.connect(self.update_charm_A_21)
		self.charm_A_22.clicked.connect(self.update_charm_A_22)
		self.charm_A_23.clicked.connect(self.update_charm_A_23)
		self.charm_A_24.clicked.connect(self.update_charm_A_24)
		self.charm_A_25.clicked.connect(self.update_charm_A_25)
		self.charm_A_26.clicked.connect(self.update_charm_A_26)
		self.charm_A_27.clicked.connect(self.update_charm_A_27)
		self.charm_A_28.clicked.connect(self.update_charm_A_28)
		self.charm_A_29.clicked.connect(self.update_charm_A_29)
		self.charm_A_30.clicked.connect(self.update_charm_A_30)
		self.charm_A_31.clicked.connect(self.update_charm_A_31)
		self.charm_A_32.clicked.connect(self.update_charm_A_32)
		self.charm_A_33.clicked.connect(self.update_charm_A_33)
		self.charm_A_34.clicked.connect(self.update_charm_A_34)
		self.charm_A_35.clicked.connect(self.update_charm_A_35)
		self.charm_A_36.clicked.connect(self.update_charm_A_36)
		self.charm_A_37.clicked.connect(self.update_charm_A_37)
		self.charm_A_38.clicked.connect(self.update_charm_A_38)
		self.charm_A_39.clicked.connect(self.update_charm_A_39)	

		self.charm_B_1.clicked.connect(self.update_charm_B_1)
		self.charm_B_2.clicked.connect(self.update_charm_B_2)
		self.charm_B_3.clicked.connect(self.update_charm_B_3)
		self.charm_B_4.clicked.connect(self.update_charm_B_4)
		self.charm_B_5.clicked.connect(self.update_charm_B_5)
		self.charm_B_6.clicked.connect(self.update_charm_B_6)
		self.charm_B_7.clicked.connect(self.update_charm_B_7)
		self.charm_B_8.clicked.connect(self.update_charm_B_8)
		self.charm_B_9.clicked.connect(self.update_charm_B_9)
		self.charm_B_10.clicked.connect(self.update_charm_B_10)
		self.charm_B_11.clicked.connect(self.update_charm_B_11)
		self.charm_B_12.clicked.connect(self.update_charm_B_12)
		self.charm_B_13.clicked.connect(self.update_charm_B_13)
		self.charm_B_14.clicked.connect(self.update_charm_B_14)
		self.charm_B_15.clicked.connect(self.update_charm_B_15)
		self.charm_B_16.clicked.connect(self.update_charm_B_16)
		self.charm_B_17.clicked.connect(self.update_charm_B_17)
		self.charm_B_18.clicked.connect(self.update_charm_B_18)
		self.charm_B_19.clicked.connect(self.update_charm_B_19)
		self.charm_B_20.clicked.connect(self.update_charm_B_20)
		self.charm_B_21.clicked.connect(self.update_charm_B_21)
		self.charm_B_22.clicked.connect(self.update_charm_B_22)
		self.charm_B_23.clicked.connect(self.update_charm_B_23)
		self.charm_B_24.clicked.connect(self.update_charm_B_24)
		self.charm_B_25.clicked.connect(self.update_charm_B_25)
		self.charm_B_26.clicked.connect(self.update_charm_B_26)
		self.charm_B_27.clicked.connect(self.update_charm_B_27)
		self.charm_B_28.clicked.connect(self.update_charm_B_28)
		self.charm_B_29.clicked.connect(self.update_charm_B_29)
		self.charm_B_30.clicked.connect(self.update_charm_B_30)
		self.charm_B_31.clicked.connect(self.update_charm_B_31)
		self.charm_B_32.clicked.connect(self.update_charm_B_32)
		self.charm_B_33.clicked.connect(self.update_charm_B_33)
		self.charm_B_34.clicked.connect(self.update_charm_B_34)
		self.charm_B_35.clicked.connect(self.update_charm_B_35)
		self.charm_B_36.clicked.connect(self.update_charm_B_36)
		self.charm_B_37.clicked.connect(self.update_charm_B_37)
		self.charm_B_38.clicked.connect(self.update_charm_B_38)
		self.charm_B_39.clicked.connect(self.update_charm_B_39)	

	def update_order_A(self):
		self.A_first.setChecked(True)
		self.A_first.setText("A队先手")
		self.B_first.setChecked(False)
		self.B_first.setText("")

	def update_order_B(self):
		self.A_first.setChecked(False)
		self.A_first.setText("")
		self.B_first.setChecked(True)
		self.B_first.setText("B队先手")

	def deactivate_Fury(self):
		global state
		state["Fury"] = False
		update.update_charm.update_charm(self, state, build)

	def activate_Fury(self):
		global state
		state["Fury"] = True
		update.update_charm.update_charm(self, state, build)

	def pick_Team_A1(self):
		global state
		state["team"][0] = 1
		update.update_team.update_team(self, state)

	def pick_Team_A2(self):
		global state
		state["team"][0] = 2
		update.update_team.update_team(self, state)

	def pick_Team_A3(self):
		global state
		state["team"][0] = 3
		update.update_team.update_team(self, state)

	def pick_Team_A4(self):
		global state
		state["team"][0] = 4
		update.update_team.update_team(self, state)

	def pick_Team_B1(self):
		global state
		state["team"][1] = 1
		update.update_team.update_team(self, state)

	def pick_Team_B2(self):
		global state
		state["team"][1] = 2
		update.update_team.update_team(self, state)

	def pick_Team_B3(self):
		global state
		state["team"][1] = 3
		update.update_team.update_team(self, state)

	def pick_Team_B4(self):
		global state
		state["team"][1] = 4
		update.update_team.update_team(self, state)

	def reset_state(self):
		global state
		global build
		
		win = self.reset
		win.setWindowTitle("确认重置 by Stellalalalalalalalalala")
		win.setWindowIcon(QtGui.QIcon(os.path.join(basedir, "Image/developer/ghost.png")))
		qss_icon= """ QLabel {border-image: url("Image/developer/reset.png") 0 0 0 0 strech strech; } """
		win.icon_stella.setStyleSheet(qss_icon)
		win.win_reset_closed.connect(self.update_all)
		win.show()

	def update_all(self):
		global state
		global build

		self.A_first.setChecked(False)
		self.B_first.setChecked(False)
		self.A_first.setText("A队先手")
		self.B_first.setText("B队先手")

		update.update_team.update_team(self, state)
		update.update_binding.update_binding(self, state)
		update.update_notch.update_notch(self, state)
		update.update_equip.update_equip(self, state, build)
		update.update_round1.update_round1(self, state, build)
		update.update_round2.update_round2(self, state, build)
		update.update_charm.update_charm(self, state, build)
		update.update_operation.update_operation(self, state)

	def confirm_state(self):
		global state
		global build
		
		if state["step"] == 0:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)
			update.update_binding.update_binding(self, state)
			update.update_charm.update_charm(self, state, build)

		elif state["step"] == 1:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)
			update.update_binding.update_binding(self, state)
			update.update_charm.update_charm(self, state, build)
			self.play_sound_binding()

		elif  state["step"] == 2:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)
			update.update_binding.update_binding(self, state)
			update.update_charm.update_charm(self, state, build)
			self.play_sound_binding()

		elif  state["step"] == 3:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)
			if self.A_first.isChecked():
				self.update_Equip_A()
			if self.B_first.isChecked():
				self.update_Equip_B()

		elif  state["step"] == 4:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_B()
			if self.B_first.isChecked():
				self.update_Equip_A()

		elif  (state["step"] == 5) & self.A_first.isChecked():
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			for i_charm in range(len(state["charm_B"])):
				if state["charm_B"][i_charm] == 1:
					state["charm_B"][i_charm] = 2
			
			update.update_charm.update_charm(self, state, build)

			for i_chosen in range(len(build["chosen_B"])):
				for i_equip in range(len(state["equip_B"])):
					if state["equip_B"][i_equip] == 0:
						state["equip_B"][i_equip] = 1
						build["current_B"][i_equip] = build["chosen_B"][i_chosen]
						break

			update.update_equip.update_equip(self, state, build)
			self.play_sound_charm()

		elif  (state["step"] == 6) & self.A_first.isChecked():
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			for i_charm_A in range(len(state["charm_A"])):
				if state["charm_A"][i_charm_A] == 1:
					state["charm_A"][i_charm_A] = 2
					state["charm_B"][i_charm_A] = 2
				if (i_charm_A + 1 ) in build["chosen_B"]:
					state["charm_A"][i_charm_A] = 2		

			update.update_charm.update_charm(self, state, build)

			for i_chosen in range(len(build["chosen_A"])):
				for i_equip in range(len(state["equip_A"])):
					if state["equip_A"][i_equip] == 0:
						state["equip_A"][i_equip] = 1
						build["current_A"][i_equip] = build["chosen_A"][i_chosen]
						break

			update.update_equip.update_equip(self, state, build)

			build["chosen_A"] = []
			build["chosen_B"] = []
			self.play_sound_charm()

		elif  (state["step"] == 5) & self.B_first.isChecked():
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			for i_charm in range(len(state["charm_A"])):
				if state["charm_A"][i_charm] == 1:
					state["charm_A"][i_charm] = 2
			
			update.update_charm.update_charm(self, state, build)

			for i_chosen in range(len(build["chosen_A"])):
				for i_equip in range(len(state["equip_A"])):
					if state["equip_A"][i_equip] == 0:
						state["equip_A"][i_equip] = 1
						build["current_A"][i_equip] = build["chosen_A"][i_chosen]
						break

			update.update_equip.update_equip(self, state, build)
			self.play_sound_charm()

		elif  (state["step"] == 6) & self.B_first.isChecked():
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			for i_charm_B in range(len(state["charm_B"])):
				if state["charm_B"][i_charm_B] == 1:
					state["charm_B"][i_charm_B] = 2
					state["charm_A"][i_charm_B] = 2
				if (i_charm_B + 1 ) in build["chosen_A"]:
					state["charm_B"][i_charm_B] = 2		

			update.update_charm.update_charm(self, state, build)

			for i_chosen in range(len(build["chosen_B"])):
				for i_equip in range(len(state["equip_B"])):
					if state["equip_B"][i_equip] == 0:
						state["equip_B"][i_equip] = 1
						build["current_B"][i_equip] = build["chosen_B"][i_chosen]
						break

			update.update_equip.update_equip(self, state, build)

			build["chosen_A"] = []
			build["chosen_B"] = []
			self.play_sound_charm()

		elif  state["step"] == 7:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_B()
			if self.B_first.isChecked():
				self.update_Equip_A()

		elif  state["step"] == 8:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_A()
			if self.B_first.isChecked():
				self.update_Equip_B()

		elif  state["step"] == 9:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)
				 
			if self.A_first.isChecked():
				self.update_Equip_B()
			if self.B_first.isChecked():
				self.update_Equip_A()

		elif  state["step"] == 10:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_A()
			if self.B_first.isChecked():
				self.update_Equip_B()

		elif  state["step"] == 11:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_A()
			if self.B_first.isChecked():
				self.update_Equip_B()

		elif  state["step"] == 12:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_B()
			if self.B_first.isChecked():
				self.update_Equip_A()

		elif  state["step"] == 13:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_A()
			if self.B_first.isChecked():
				self.update_Equip_B()

		elif  state["step"] == 14:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_B()
			if self.B_first.isChecked():
				self.update_Equip_A()

		elif  state["step"] == 15:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_B()
			if self.B_first.isChecked():
				self.update_Equip_A()

		elif  state["step"] == 16:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)

			if self.A_first.isChecked():
				self.update_Equip_A()
			if self.B_first.isChecked():
				self.update_Equip_B()

		elif  state["step"] == 17:
			state["step"] = state["step"] + 1
			update.update_team.update_team(self, state)
			update.update_operation.update_operation(self, state)
			self.play_sound_charm()
		else:
			return 0


	def start_next(self):
		win = self.next
		win.setWindowTitle("开启下一局 by Stellalalalalalalalalala")
		win.setWindowIcon(QtGui.QIcon("Image/developer/ghost.png"))
		qss_icon= """ QLabel {border-image: url("Image/developer/next.png") 0 0 0 0 strech strech; } """
		win.icon_stella.setStyleSheet(qss_icon)
		win.win_next_closed.connect(self.next_round)
		win.show()


	def next_round(self):
		global state
		global build

		for i_binding_A in range(len(state["binding_A"])):
			if state["binding_A"][i_binding_A] == 1:
				state["binding_A"][i_binding_A] = 3
			elif state["binding_A"][i_binding_A] == 2:
				state["binding_A"][i_binding_A] = 0

		for i_binding_B in range(len(state["binding_B"])):
			if state["binding_B"][i_binding_B] == 1:
				state["binding_B"][i_binding_B] = 3
			elif state["binding_B"][i_binding_B] == 2:
				state["binding_B"][i_binding_B] = 0

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		state["charmed_notchNum_A"] = 0
		state["charmed_notchNum_B"] = 0

		build["chosen_A"] = []
		build["chosen_B"] = []

		if state["round"] == 0:
			build["round_1_A"] = build["current_A"]
			build["round_1_B"] = build["current_B"]

			if self.A_first.isChecked():
				self.A_first.setChecked(False)
				self.B_first.setChecked(True)
			if self.B_first.isChecked():
				self.A_first.setChecked(True)
				self.B_first.setChecked(False)

		elif state["round"] == 1:
			build["round_2_A"] = build["current_A"]
			build["round_2_B"] = build["current_B"]
		else:
			build["round_1_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			build["round_1_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			build["round_2_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			build["round_2_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		build["current_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		build["current_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		state["charm_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		state["charm_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		for i_charm_A in range(len(state["charm_A"])):
			if ((i_charm_A + 1) in build["round_1_A"]) or ((i_charm_A + 1) in build["round_2_A"]):
				state["charm_A"][i_charm_A] = 2
			else:
				state["charm_A"][i_charm_A] = 0

		for i_charm_B in range(len(state["charm_B"])):
			if ((i_charm_B + 1) in build["round_1_B"]) or ((i_charm_B + 1) in build["round_2_B"]):
				state["charm_B"][i_charm_B] = 2
			else:
				state["charm_B"][i_charm_B] = 0			

		state["equip_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		state["equip_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		state["step"] = 0

		if state["round"] < 2:
			state["round"] = state["round"] + 1
		else:
			state["round"] = 0
			state["team"] = [0, 0]
			self.score_A.setText("")
			self.score_B.setText("")
			state["binding_A"] = [0, 0, 0]
			state["binding_B"] = [0, 0, 0]

		update.update_team.update_team(self, state)
		update.update_binding.update_binding(self, state)
		update.update_notch.update_notch(self, state)
		update.update_equip.update_equip(self, state, build)
		update.update_round1.update_round1(self, state, build)
		update.update_round2.update_round2(self, state, build)
		update.update_charm.update_charm(self, state, build)
		update.update_operation.update_operation(self, state)


	def update_nail_A(self):
		global state

		if (state["binding_A"][0] == 0) or (state["binding_A"][0] == 2):
			state["binding_A"][0] = 1
			if state["binding_A"][1] < 3:
				state["binding_A"][1] = 2
			if state["binding_A"][2] < 3:
				state["binding_A"][2] = 2
		elif state["binding_A"][0] == 1:
			state["binding_A"][0] = 0
			if state["binding_A"][1] < 3:
				state["binding_A"][1] = 0
			if state["binding_A"][2] < 3:
				state["binding_A"][2] = 0
		else:
			return 0			
        
		update.update_binding.update_binding(self, state)

	def update_mask_A(self):
		global state

		if (state["binding_A"][1] == 0) or (state["binding_A"][1] == 2):
			state["binding_A"][1] = 1
			if state["binding_A"][0] < 3:
				state["binding_A"][0] = 2
			if state["binding_A"][2] < 3:
				state["binding_A"][2] = 2
		elif state["binding_A"][1] == 1:
			state["binding_A"][1] = 0
			if state["binding_A"][0] < 3:
				state["binding_A"][0] = 0
			if state["binding_A"][2] < 3:
				state["binding_A"][2] = 0
		else:
			return 0	

		update.update_binding.update_binding(self, state)

	def update_soul_A(self):
		global state

		if (state["binding_A"][2] == 0) or (state["binding_A"][2] == 2):
			state["binding_A"][2] = 1
			if state["binding_A"][0] < 3:
				state["binding_A"][0] = 2
			if state["binding_A"][1] < 3:
				state["binding_A"][1] = 2
		elif state["binding_A"][2] == 1:
			state["binding_A"][2] = 0
			if state["binding_A"][0] < 3:
				state["binding_A"][0] = 0
			if state["binding_A"][1] < 3:
				state["binding_A"][1] = 0
		else:
			return 0	

		update.update_binding.update_binding(self, state)

	def update_nail_B(self):
		global state

		if (state["binding_B"][0] == 0) or (state["binding_B"][0] == 2):
			state["binding_B"][0] = 1
			if state["binding_B"][1] < 3:
				state["binding_B"][1] = 2
			if state["binding_B"][2] < 3:
				state["binding_B"][2] = 2
		elif state["binding_B"][0] == 1:
			state["binding_B"][0] = 0
			if state["binding_B"][1] < 3:
				state["binding_B"][1] = 0
			if state["binding_B"][2] < 3:
				state["binding_B"][2] = 0
		else:
			return 0			
        
		update.update_binding.update_binding(self, state)

	def update_mask_B(self):
		global state

		if (state["binding_B"][1] == 0) or (state["binding_B"][1] == 2):
			state["binding_B"][1] = 1
			if state["binding_B"][0] < 3:
				state["binding_B"][0] = 2
			if state["binding_B"][2] < 3:
				state["binding_B"][2] = 2
		elif state["binding_B"][1] == 1:
			state["binding_B"][1] = 0
			if state["binding_B"][0] < 3:
				state["binding_B"][0] = 0
			if state["binding_B"][2] < 3:
				state["binding_B"][2] = 0
		else:
			return 0	

		update.update_binding.update_binding(self, state)

	def update_soul_B(self):
		global state

		if (state["binding_B"][2] == 0) or (state["binding_B"][2] == 2):
			state["binding_B"][2] = 1
			if state["binding_B"][0] < 3:
				state["binding_B"][0] = 2
			if state["binding_B"][1] < 3:
				state["binding_B"][1] = 2
		elif state["binding_B"][2] == 1:
			state["binding_B"][2] = 0
			if state["binding_B"][0] < 3:
				state["binding_B"][0] = 0
			if state["binding_B"][1] < 3:
				state["binding_B"][1] = 0
		else:
			return 0	

		update.update_binding.update_binding(self, state)

	def update_charm_A_1(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_1"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][0] == 0:
			state["charm_A"][0] = 1
			build["chosen_A"].append(1)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][0] == 1:
			state["charm_A"][0] = 0
			build["chosen_A"].remove(1)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_2(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_2"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][1] == 0:
			state["charm_A"][1] = 1
			build["chosen_A"].append(2)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][1] == 1:
			state["charm_A"][1] = 0
			build["chosen_A"].remove(2)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_3(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_3"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][2] == 0:
			state["charm_A"][2] = 1
			build["chosen_A"].append(3)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][2] == 1:
			state["charm_A"][2] = 0
			build["chosen_A"].remove(3)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_4(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_4"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][3] == 0:
			state["charm_A"][3] = 1
			build["chosen_A"].append(4)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][3] == 1:
			state["charm_A"][3] = 0
			build["chosen_A"].remove(4)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_5(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_5"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][4] == 0:
			state["charm_A"][4] = 1
			build["chosen_A"].append(5)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][4] == 1:
			state["charm_A"][4] = 0
			build["chosen_A"].remove(5)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_6(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_6"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][5] == 0:
			state["charm_A"][5] = 1
			build["chosen_A"].append(6)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][5] == 1:
			state["charm_A"][5] = 0
			build["chosen_A"].remove(6)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_7(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_7"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][6] == 0:
			state["charm_A"][6] = 1
			build["chosen_A"].append(7)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][6] == 1:
			state["charm_A"][6] = 0
			build["chosen_A"].remove(7)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_8(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_8"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][7] == 0:
			state["charm_A"][7] = 1
			build["chosen_A"].append(8)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][7] == 1:
			state["charm_A"][7] = 0
			build["chosen_A"].remove(8)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_9(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_9"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][8] == 0:
			state["charm_A"][8] = 1
			build["chosen_A"].append(9)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][8] == 1:
			state["charm_A"][8] = 0
			build["chosen_A"].remove(9)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_10(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_10"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][9] == 0:
			state["charm_A"][9] = 1
			build["chosen_A"].append(10)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][9] == 1:
			state["charm_A"][9] = 0
			build["chosen_A"].remove(10)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_11(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_11"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][10] == 0:
			state["charm_A"][10] = 1
			build["chosen_A"].append(11)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][10] == 1:
			state["charm_A"][10] = 0
			build["chosen_A"].remove(11)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_12(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_12"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][11] == 0:
			state["charm_A"][11] = 1
			build["chosen_A"].append(12)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][11] == 1:
			state["charm_A"][11] = 0
			build["chosen_A"].remove(12)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_13(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_13"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][12] == 0:
			state["charm_A"][12] = 1
			build["chosen_A"].append(13)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][12] == 1:
			state["charm_A"][12] = 0
			build["chosen_A"].remove(13)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_14(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_14"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][13] == 0:
			state["charm_A"][13] = 1
			build["chosen_A"].append(14)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][13] == 1:
			state["charm_A"][13] = 0
			build["chosen_A"].remove(14)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_15(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_15"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][14] == 0:
			state["charm_A"][14] = 1
			build["chosen_A"].append(15)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][14] == 1:
			state["charm_A"][14] = 0
			build["chosen_A"].remove(15)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_16(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_16"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][15] == 0:
			state["charm_A"][15] = 1
			build["chosen_A"].append(16)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][15] == 1:
			state["charm_A"][15] = 0
			build["chosen_A"].remove(16)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_17(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_17"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][16] == 0:
			state["charm_A"][16] = 1
			build["chosen_A"].append(17)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][16] == 1:
			state["charm_A"][16] = 0
			build["chosen_A"].remove(17)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_18(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_18"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][17] == 0:
			state["charm_A"][17] = 1
			build["chosen_A"].append(18)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][17] == 1:
			state["charm_A"][17] = 0
			build["chosen_A"].remove(18)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_19(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_19"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][18] == 0:
			state["charm_A"][18] = 1
			build["chosen_A"].append(19)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][18] == 1:
			state["charm_A"][18] = 0
			build["chosen_A"].remove(19)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_20(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_20"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][19] == 0:
			state["charm_A"][19] = 1
			build["chosen_A"].append(20)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][19] == 1:
			state["charm_A"][19] = 0
			build["chosen_A"].remove(20)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_21(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_21"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][20] == 0:
			state["charm_A"][20] = 1
			build["chosen_A"].append(21)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][20] == 1:
			state["charm_A"][20] = 0
			build["chosen_A"].remove(21)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_22(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_22"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][21] == 0:
			state["charm_A"][21] = 1
			build["chosen_A"].append(22)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][21] == 1:
			state["charm_A"][21] = 0
			build["chosen_A"].remove(22)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_23(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_23"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][22] == 0:
			state["charm_A"][22] = 1
			build["chosen_A"].append(23)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][22] == 1:
			state["charm_A"][22] = 0
			build["chosen_A"].remove(23)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_24(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_24"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][23] == 0:
			state["charm_A"][23] = 1
			build["chosen_A"].append(24)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][23] == 1:
			state["charm_A"][23] = 0
			build["chosen_A"].remove(24)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_25(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_25"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][24] == 0:
			state["charm_A"][24] = 1
			build["chosen_A"].append(25)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][24] == 1:
			state["charm_A"][24] = 0
			build["chosen_A"].remove(25)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_26(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_26"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][25] == 0:
			state["charm_A"][25] = 1
			build["chosen_A"].append(26)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][25] == 1:
			state["charm_A"][25] = 0
			build["chosen_A"].remove(26)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_27(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_27"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][26] == 0:
			state["charm_A"][26] = 1
			build["chosen_A"].append(27)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][26] == 1:
			state["charm_A"][26] = 0
			build["chosen_A"].remove(27)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_28(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_28"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][27] == 0:
			state["charm_A"][27] = 1
			build["chosen_A"].append(28)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][27] == 1:
			state["charm_A"][27] = 0
			build["chosen_A"].remove(28)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_29(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_29"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][28] == 0:
			state["charm_A"][28] = 1
			build["chosen_A"].append(29)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][28] == 1:
			state["charm_A"][28] = 0
			build["chosen_A"].remove(29)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_30(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_30"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][29] == 0:
			state["charm_A"][29] = 1
			build["chosen_A"].append(30)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][29] == 1:
			state["charm_A"][29] = 0
			build["chosen_A"].remove(30)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_31(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_31"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][30] == 0:
			state["charm_A"][30] = 1
			build["chosen_A"].append(31)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][30] == 1:
			state["charm_A"][30] = 0
			build["chosen_A"].remove(31)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_32(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_32"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][31] == 0:
			state["charm_A"][31] = 1
			build["chosen_A"].append(32)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][31] == 1:
			state["charm_A"][31] = 0
			build["chosen_A"].remove(32)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_33(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_33"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][32] == 0:
			state["charm_A"][32] = 1
			build["chosen_A"].append(33)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][32] == 1:
			state["charm_A"][32] = 0
			build["chosen_A"].remove(33)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_34(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_34"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][33] == 0:
			state["charm_A"][33] = 1
			build["chosen_A"].append(34)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][33] == 1:
			state["charm_A"][33] = 0
			build["chosen_A"].remove(34)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_35(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_35"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][34] == 0:
			state["charm_A"][34] = 1
			build["chosen_A"].append(35)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][34] == 1:
			state["charm_A"][34] = 0
			build["chosen_A"].remove(35)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_36(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_36"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][35] == 0:
			state["charm_A"][35] = 1
			build["chosen_A"].append(36)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][35] == 1:
			state["charm_A"][35] = 0
			build["chosen_A"].remove(36)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_37(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_37"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][36] == 0:
			state["charm_A"][36] = 1
			build["chosen_A"].append(37)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][36] == 1:
			state["charm_A"][36] = 0
			build["chosen_A"].remove(37)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_38(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_38"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][37] == 0:
			state["charm_A"][37] = 1
			build["chosen_A"].append(38)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][37] == 1:
			state["charm_A"][37] = 0
			build["chosen_A"].remove(38)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_A_39(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_39"]

		state["notch_A"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_A"][38] == 0:
			state["charm_A"][38] = 1
			build["chosen_A"].append(39)
			for i  in range(min(state["charmed_notchNum_A"] + notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"]  = state["charmed_notchNum_A"] + notch_num
		elif state["charm_A"][38] == 1:
			state["charm_A"][38] = 0
			build["chosen_A"].remove(39)
			for i  in range(min(state["charmed_notchNum_A"] - notch_num, 11)):
				state["notch_A"][i] = 1
			state["charmed_notchNum_A"] = state["charmed_notchNum_A"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_1(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_1"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][0] == 0:
			state["charm_B"][0] = 1
			build["chosen_B"].append(1)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][0] == 1:
			state["charm_B"][0] = 0
			build["chosen_B"].remove(1)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_2(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_2"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][1] == 0:
			state["charm_B"][1] = 1
			build["chosen_B"].append(2)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][1] == 1:
			state["charm_B"][1] = 0
			build["chosen_B"].remove(2)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_3(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_3"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][2] == 0:
			state["charm_B"][2] = 1
			build["chosen_B"].append(3)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][2] == 1:
			state["charm_B"][2] = 0
			build["chosen_B"].remove(3)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_4(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_4"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][3] == 0:
			state["charm_B"][3] = 1
			build["chosen_B"].append(4)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][3] == 1:
			state["charm_B"][3] = 0
			build["chosen_B"].remove(4)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_5(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_5"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][4] == 0:
			state["charm_B"][4] = 1
			build["chosen_B"].append(5)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][4] == 1:
			state["charm_B"][4] = 0
			build["chosen_B"].remove(5)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_6(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_6"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][5] == 0:
			state["charm_B"][5] = 1
			build["chosen_B"].append(6)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][5] == 1:
			state["charm_B"][5] = 0
			build["chosen_B"].remove(6)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_7(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_7"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][6] == 0:
			state["charm_B"][6] = 1
			build["chosen_B"].append(7)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][6] == 1:
			state["charm_B"][6] = 0
			build["chosen_B"].remove(7)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_8(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_8"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][7] == 0:
			state["charm_B"][7] = 1
			build["chosen_B"].append(8)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][7] == 1:
			state["charm_B"][7] = 0
			build["chosen_B"].remove(8)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_9(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_9"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][8] == 0:
			state["charm_B"][8] = 1
			build["chosen_B"].append(9)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][8] == 1:
			state["charm_B"][8] = 0
			build["chosen_B"].remove(9)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_10(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_10"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][9] == 0:
			state["charm_B"][9] = 1
			build["chosen_B"].append(10)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][9] == 1:
			state["charm_B"][9] = 0
			build["chosen_B"].remove(10)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_11(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_11"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][10] == 0:
			state["charm_B"][10] = 1
			build["chosen_B"].append(11)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][10] == 1:
			state["charm_B"][10] = 0
			build["chosen_B"].remove(11)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_12(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_12"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][11] == 0:
			state["charm_B"][11] = 1
			build["chosen_B"].append(12)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][11] == 1:
			state["charm_B"][11] = 0
			build["chosen_B"].remove(12)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_13(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_13"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][12] == 0:
			state["charm_B"][12] = 1
			build["chosen_B"].append(13)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][12] == 1:
			state["charm_B"][12] = 0
			build["chosen_B"].remove(13)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_14(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_14"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][13] == 0:
			state["charm_B"][13] = 1
			build["chosen_B"].append(14)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][13] == 1:
			state["charm_B"][13] = 0
			build["chosen_B"].remove(14)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_15(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_15"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][14] == 0:
			state["charm_B"][14] = 1
			build["chosen_B"].append(15)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][14] == 1:
			state["charm_B"][14] = 0
			build["chosen_B"].remove(15)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_16(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_16"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][15] == 0:
			state["charm_B"][15] = 1
			build["chosen_B"].append(16)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][15] == 1:
			state["charm_B"][15] = 0
			build["chosen_B"].remove(16)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_17(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_17"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][16] == 0:
			state["charm_B"][16] = 1
			build["chosen_B"].append(17)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][16] == 1:
			state["charm_B"][16] = 0
			build["chosen_B"].remove(17)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_18(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_18"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][17] == 0:
			state["charm_B"][17] = 1
			build["chosen_B"].append(18)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][17] == 1:
			state["charm_B"][17] = 0
			build["chosen_B"].remove(18)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_19(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_19"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][18] == 0:
			state["charm_B"][18] = 1
			build["chosen_B"].append(19)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][18] == 1:
			state["charm_B"][18] = 0
			build["chosen_B"].remove(19)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_20(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_20"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][19] == 0:
			state["charm_B"][19] = 1
			build["chosen_B"].append(20)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][19] == 1:
			state["charm_B"][19] = 0
			build["chosen_B"].remove(20)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_21(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_21"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][20] == 0:
			state["charm_B"][20] = 1
			build["chosen_B"].append(21)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][20] == 1:
			state["charm_B"][20] = 0
			build["chosen_B"].remove(21)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_22(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_22"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][21] == 0:
			state["charm_B"][21] = 1
			build["chosen_B"].append(22)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][21] == 1:
			state["charm_B"][21] = 0
			build["chosen_B"].remove(22)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_23(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_23"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][22] == 0:
			state["charm_B"][22] = 1
			build["chosen_B"].append(23)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][22] == 1:
			state["charm_B"][22] = 0
			build["chosen_B"].remove(23)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_24(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_24"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][23] == 0:
			state["charm_B"][23] = 1
			build["chosen_B"].append(24)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][23] == 1:
			state["charm_B"][23] = 0
			build["chosen_B"].remove(24)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_25(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_25"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][24] == 0:
			state["charm_B"][24] = 1
			build["chosen_B"].append(25)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][24] == 1:
			state["charm_B"][24] = 0
			build["chosen_B"].remove(25)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_26(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_26"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][25] == 0:
			state["charm_B"][25] = 1
			build["chosen_B"].append(26)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][25] == 1:
			state["charm_B"][25] = 0
			build["chosen_B"].remove(26)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_27(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_27"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][26] == 0:
			state["charm_B"][26] = 1
			build["chosen_B"].append(27)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][26] == 1:
			state["charm_B"][26] = 0
			build["chosen_B"].remove(27)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_28(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_28"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][27] == 0:
			state["charm_B"][27] = 1
			build["chosen_B"].append(28)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][27] == 1:
			state["charm_B"][27] = 0
			build["chosen_B"].remove(28)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_29(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_29"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][28] == 0:
			state["charm_B"][28] = 1
			build["chosen_B"].append(29)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][28] == 1:
			state["charm_B"][28] = 0
			build["chosen_B"].remove(29)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_30(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_30"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][29] == 0:
			state["charm_B"][29] = 1
			build["chosen_B"].append(30)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][29] == 1:
			state["charm_B"][29] = 0
			build["chosen_B"].remove(30)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_31(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_31"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][30] == 0:
			state["charm_B"][30] = 1
			build["chosen_B"].append(31)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][30] == 1:
			state["charm_B"][30] = 0
			build["chosen_B"].remove(31)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_32(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_32"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][31] == 0:
			state["charm_B"][31] = 1
			build["chosen_B"].append(32)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][31] == 1:
			state["charm_B"][31] = 0
			build["chosen_B"].remove(32)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_33(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_33"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][32] == 0:
			state["charm_B"][32] = 1
			build["chosen_B"].append(33)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][32] == 1:
			state["charm_B"][32] = 0
			build["chosen_B"].remove(33)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_34(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_34"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][33] == 0:
			state["charm_B"][33] = 1
			build["chosen_B"].append(34)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][33] == 1:
			state["charm_B"][33] = 0
			build["chosen_B"].remove(34)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_35(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_35"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][34] == 0:
			state["charm_B"][34] = 1
			build["chosen_B"].append(35)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][34] == 1:
			state["charm_B"][34] = 0
			build["chosen_B"].remove(35)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_36(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_36"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][35] == 0:
			state["charm_B"][35] = 1
			build["chosen_B"].append(36)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][35] == 1:
			state["charm_B"][35] = 0
			build["chosen_B"].remove(36)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_37(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_37"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][36] == 0:
			state["charm_B"][36] = 1
			build["chosen_B"].append(37)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][36] == 1:
			state["charm_B"][36] = 0
			build["chosen_B"].remove(37)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_38(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_38"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][37] == 0:
			state["charm_B"][37] = 1
			build["chosen_B"].append(38)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][37] == 1:
			state["charm_B"][37] = 0
			build["chosen_B"].remove(38)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_charm_B_39(self):
		global state
		global build

		with open("Text/CharmData.json", "r") as file:
			charmData = json.load(file)

		notch_num = charmData["notch_39"]

		state["notch_B"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		if state["charm_B"][38] == 0:
			state["charm_B"][38] = 1
			build["chosen_B"].append(39)
			for i  in range(min(state["charmed_notchNum_B"] + notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"]  = state["charmed_notchNum_B"] + notch_num
		elif state["charm_B"][38] == 1:
			state["charm_B"][38] = 0
			build["chosen_B"].remove(39)
			for i  in range(min(state["charmed_notchNum_B"] - notch_num, 11)):
				state["notch_B"][i] = 1
			state["charmed_notchNum_B"] = state["charmed_notchNum_B"] - notch_num
		else:
			return 0

		update.update_charm.update_charm(self, state, build)
		update.update_notch.update_notch(self, state)

	def update_Equip_A(self):
		global state
		global build

		for i_charm in range(len(state["charm_A"])):
			if state["charm_A"][i_charm] == 1:
				state["charm_A"][i_charm] = 2
				state["charm_B"][i_charm] = 2
		
		update.update_charm.update_charm(self, state, build)

		for i_chosen in range(len(build["chosen_A"])):
			for i_equip in range(len(state["equip_A"])):
				if state["equip_A"][i_equip] == 0:
					state["equip_A"][i_equip] = 1
					build["current_A"][i_equip] = build["chosen_A"][i_chosen]
					break

		update.update_equip.update_equip(self, state, build)

		build["chosen_A"] = []
		self.play_sound_charm()

	def update_Equip_B(self):
		global state
		global build

		for i_charm in range(len(state["charm_B"])):
			if state["charm_B"][i_charm] == 1:
				state["charm_B"][i_charm] = 2
				state["charm_A"][i_charm] = 2
		
		update.update_charm.update_charm(self, state, build)

		for i_chosen in range(len(build["chosen_B"])):
			for i_equip in range(len(state["equip_B"])):
				if state["equip_B"][i_equip] == 0:
					state["equip_B"][i_equip] = 1
					build["current_B"][i_equip] = build["chosen_B"][i_chosen]
					break

		update.update_equip.update_equip(self, state, build)

		build["chosen_B"] = []
		self.play_sound_charm()

	def play_sound_binding(self):
		self.player = QMediaPlayer()
		self.audio = QAudioOutput()
		self.player.setAudioOutput(self.audio)
		self.player.setSource(QUrl.fromLocalFile("Sound/binding.mp3"))
		self.audio.setVolume(100)
		self.player.play()


	def play_sound_charm(self):
		self.player = QMediaPlayer()
		self.audio = QAudioOutput()
		self.player.setAudioOutput(self.audio)
		self.player.setSource(QUrl.fromLocalFile("Sound/charmed.mp3"))
		self.audio.setVolume(100)
		self.player.play()


	def resizeEvent(self, event):
		new_width = event.size().width()
		new_height = event.size().height()
		adjusted_height = int(new_width / self.aspect_ratio)
		self.resize(QSize(new_width, adjusted_height))
		super().resizeEvent(event)


def main():
	app = QtWidgets.QApplication(sys.argv)
	win = window_BP()
	#win.setMaximumSize(1920, 1080)
	win.setFixedSize(1920, 1080)
	win.setWindowTitle("2025 渔村杯 BP赛小工具 by Stellalalalalalalalalala(史黛拉啦啦啦)")
	win.setWindowIcon(QtGui.QIcon("Image/developer/ghost.png"))
	win.show()
	sys.exit(app.exec())


if __name__ == "__main__":
	main()