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
from PyQt6.QtWidgets import QLabel

def update_operation(self, state):
	
	steps = {
		"step_0" : "未选择先手队伍，请重置后重新操作",
		"step_1" : "未选择先手队伍，请重置后重新操作",
		"step_2" : "未选择先手队伍，请重置后重新操作",
		"step_3" : "未选择先手队伍，请重置后重新操作",
		"step_4" : "未选择先手队伍，请重置后重新操作",
		"step_5" : "未选择先手队伍，请重置后重新操作",
		"step_6" : "未选择先手队伍，请重置后重新操作",
		"step_7" : "未选择先手队伍，请重置后重新操作",
		"step_8" : "未选择先手队伍，请重置后重新操作",
		"step_9" : "未选择先手队伍，请重置后重新操作",
		"step_10" : "未选择先手队伍，请重置后重新操作",
		"step_11" : "未选择先手队伍，请重置后重新操作",
		"step_12" : "未选择先手队伍，请重置后重新操作",
		"step_13" : "未选择先手队伍，请重置后重新操作",
		"step_14" : "未选择先手队伍，请重置后重新操作",
		"step_15" : "未选择先手队伍，请重置后重新操作",
		"step_16" : "未选择先手队伍，请重置后重新操作",
		"step_17" : "未选择先手队伍，请重置后重新操作"
		}

	if self.A_first.isChecked():

		steps = {
			"step_0" : "请输入两队得分，选择先手队伍",
			"step_1" : "A队为B队上锁",
			"step_2" : "B队为A队上锁",
			"step_3" : "A队为自己挑选护符，且对方禁用",
			"step_4" : "B队为自己挑选护符，且对方禁用",
			"step_5" : "A队为B队挑选护符，不超过四槽",
			"step_6" : "B队为A队挑选护符，不超过四槽",
			"step_7" : "B队为自己挑选护符，且对方禁用",
			"step_8" : "A队为自己挑选护符，且对方禁用",
			"step_9" : "B队为自己挑选护符，且对方禁用",
			"step_10" : "A队为自己挑选护符，且对方禁用",
			"step_11" : "A队为自己挑选护符，且对方禁用",
			"step_12" : "B队为自己挑选护符，且对方禁用",
			"step_13" : "A队为自己挑选护符，且对方禁用",
			"step_14" : "B队为自己挑选护符，且对方禁用",
			"step_15" : "B队为自己挑选护符，且对方禁用",
			"step_16" : "A队为自己挑选护符，且对方禁用",
			"step_17" : "挑选结束，比赛即将开始"
			}

	if self.B_first.isChecked():

		steps = {
			"step_0" : "请输入两队得分，选择先手队伍",
			"step_1" : "B队为A队上锁",
			"step_2" : "A队为B队上锁",
			"step_3" : "B队为自己挑选护符，且对方禁用",
			"step_4" : "A队为自己挑选护符，且对方禁用",
			"step_5" : "B队为A队挑选护符，不超过四槽",
			"step_6" : "A队为B队挑选护符，不超过四槽",
			"step_7" : "A队为自己挑选护符，且对方禁用",
			"step_8" : "B队为自己挑选护符，且对方禁用",
			"step_9" : "A队为自己挑选护符，且对方禁用",
			"step_10" : "B队为自己挑选护符，且对方禁用",
			"step_11" : "B队为自己挑选护符，且对方禁用",
			"step_12" : "A队为自己挑选护符，且对方禁用",
			"step_13" : "B队为自己挑选护符，且对方禁用",
			"step_14" : "A队为自己挑选护符，且对方禁用",
			"step_15" : "A队为自己挑选护符，且对方禁用",
			"step_16" : "B队为自己挑选护符，且对方禁用",
			"step_17" : "挑选结束，比赛即将开始"
			}

	round = state.get("round")
	step_current = state.get("step")

	if (round == 0) & (step_current == 0):
			self.current_operation.setText("请挑选参赛队伍，并决定先手队伍")
	else:
		if (round < 3) & (step_current < 18):
			text_operation = steps.get("step_" + str(step_current))
			self.current_operation.setText("第" + str(round+1) + "局: " + text_operation)
		else:
			self.current_operation.setText("ERROR")