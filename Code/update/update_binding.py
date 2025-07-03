#!/usr/bin/env python
# -*- coding: utf-8 -*-
#python_version : 3.13.0
#discription    : This defines the action that updates push button for bindings.
#author         : stellalalalalalalalalala
#created        : 2025.06.30
#last modified  : 2025.07.03


from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton

def update_binding(self, state):

	if state["step"] == 1:
		step_A = False
		step_B = True
	elif state["step"] == 2:
		step_A = True
		step_B = False
	else:
		step_A = False
		step_B = False

	nail_A_state = state.get("binding_A")[0]
	mask_A_state = state.get("binding_A")[1]
	soul_A_state = state.get("binding_A")[2]

	nail_B_state = state.get("binding_B")[0]
	mask_B_state = state.get("binding_B")[1]
	soul_B_state = state.get("binding_B")[2]

	qss_nail_origin = """
		QPushButton {
			border-image: url("Image/bindings/nail.png") 0 0 0 0 strech strech; }
		QPushButton:hover {
			border-image: url("Image/bindings/nail_hoven.png") 0 0 0 0 strech strech; }
		QPushButton:pressed {
			border-image: url("Image/bindings/nail_chosen.png") 0 0 0 0 strech strech; } """

	qss_nail_chosen = """
		QPushButton {
			border-image: url("Image/bindings/nail_chosen.png") 0 0 0 0 strech strech; } """

	qss_nail_faded = """
		QPushButton {
			border-image: url("Image/bindings/nail_faded.png") 0 0 0 0 strech strech; }
		QPushButton:hover {
			border-image: url("Image/bindings/nail_hoven.png") 0 0 0 0 strech strech; } """

	qss_nail_disable = """
		QPushButton {
			border-image: url("Image/bindings/nail_disable.png") 0 0 0 0 strech strech; } """

	if nail_A_state == 0:
		self.binding_nail_A.setEnabled(True & step_A)
		self.binding_nail_A.setStyleSheet(qss_nail_origin)
	elif nail_A_state == 1:
		self.binding_nail_A.setEnabled(True & step_A)
		self.binding_nail_A.setStyleSheet(qss_nail_chosen)
	elif nail_A_state == 2:
		self.binding_nail_A.setEnabled(True & step_A)
		self.binding_nail_A.setStyleSheet(qss_nail_faded)
	elif nail_A_state == 3:
		self.binding_nail_A.setStyleSheet(qss_nail_disable)
		self.binding_nail_A.setEnabled(False)
	else:
		return 0

	if nail_B_state == 0:
		self.binding_nail_B.setEnabled(True & step_B)
		self.binding_nail_B.setStyleSheet(qss_nail_origin)
	elif nail_B_state == 1:
		self.binding_nail_B.setEnabled(True & step_B)
		self.binding_nail_B.setStyleSheet(qss_nail_chosen)
	elif nail_B_state == 2:
		self.binding_nail_B.setEnabled(True & step_B)
		self.binding_nail_B.setStyleSheet(qss_nail_faded)
	elif nail_B_state == 3:
		self.binding_nail_B.setStyleSheet(qss_nail_disable)
		self.binding_nail_B.setEnabled(False)
	else:
		return 0

	qss_mask_origin = """
		QPushButton {
			border-image: url("Image/bindings/mask.png") 0 0 0 0 strech strech; }
		QPushButton:hover {
			border-image: url("Image/bindings/mask_hoven.png") 0 0 0 0 strech strech; }
		QPushButton:pressed {
			border-image: url("Image/bindings/mask_chosen.png") 0 0 0 0 strech strech; } """

	qss_mask_chosen = """
		QPushButton {
			border-image: url("Image/bindings/mask_chosen.png") 0 0 0 0 strech strech; } """

	qss_mask_faded = """
		QPushButton {
			border-image: url("Image/bindings/mask_faded.png") 0 0 0 0 strech strech; }
		QPushButton:hover {
			border-image: url("Image/bindings/mask_hoven.png") 0 0 0 0 strech strech; } """

	qss_mask_disable = """
		QPushButton {
			border-image: url("Image/bindings/mask_disable.png") 0 0 0 0 strech strech; } """

	if mask_A_state == 0:
		self.binding_mask_A.setEnabled(True & step_A)
		self.binding_mask_A.setStyleSheet(qss_mask_origin)
	elif mask_A_state == 1:
		self.binding_mask_A.setEnabled(True & step_A)
		self.binding_mask_A.setStyleSheet(qss_mask_chosen)
	elif mask_A_state == 2:
		self.binding_mask_A.setEnabled(True & step_A)
		self.binding_mask_A.setStyleSheet(qss_mask_faded)
	elif mask_A_state == 3:
		self.binding_mask_A.setStyleSheet(qss_mask_disable)
		self.binding_mask_A.setEnabled(False)
	else:
		return 0

	if mask_B_state == 0:
		self.binding_mask_B.setEnabled(True & step_B)
		self.binding_mask_B.setStyleSheet(qss_mask_origin)
	elif mask_B_state == 1:
		self.binding_mask_B.setEnabled(True & step_B)
		self.binding_mask_B.setStyleSheet(qss_mask_chosen)
	elif mask_B_state == 2:
		self.binding_mask_B.setEnabled(True & step_B)
		self.binding_mask_B.setStyleSheet(qss_mask_faded)
	elif mask_B_state == 3:
		self.binding_mask_B.setStyleSheet(qss_mask_disable)
		self.binding_mask_B.setEnabled(False)
	else:
		return 0

	qss_soul_origin = """
		QPushButton {
			border-image: url("Image/bindings/soul.png") 0 0 0 0 strech strech; }
		QPushButton:hover {
			border-image: url("Image/bindings/soul_hoven.png") 0 0 0 0 strech strech; }
		QPushButton:pressed {
			border-image: url("Image/bindings/soul_chosen.png") 0 0 0 0 strech strech; } """

	qss_soul_chosen = """
		QPushButton {
			border-image: url("Image/bindings/soul_chosen.png") 0 0 0 0 strech strech; } """

	qss_soul_faded = """
		QPushButton {
			border-image: url("Image/bindings/soul_faded.png") 0 0 0 0 strech strech; }
		QPushButton:hover {
			border-image: url("Image/bindings/soul_hoven.png") 0 0 0 0 strech strech; } """

	qss_soul_disable = """
		QPushButton {
			border-image: url("Image/bindings/soul_disable.png") 0 0 0 0 strech strech; } """

	if soul_A_state == 0:
		self.binding_soul_A.setEnabled(True & step_A)
		self.binding_soul_A.setStyleSheet(qss_soul_origin)
	elif soul_A_state == 1:
		self.binding_soul_A.setEnabled(True & step_A)
		self.binding_soul_A.setStyleSheet(qss_soul_chosen)
	elif soul_A_state == 2:
		self.binding_soul_A.setEnabled(True & step_A)
		self.binding_soul_A.setStyleSheet(qss_soul_faded)
	elif soul_A_state == 3:
		self.binding_soul_A.setStyleSheet(qss_soul_disable)
		self.binding_soul_A.setEnabled(False)
	else:
		return 0

	if soul_B_state == 0:
		self.binding_soul_B.setEnabled(True & step_B)
		self.binding_soul_B.setStyleSheet(qss_soul_origin)
	elif soul_B_state == 1:
		self.binding_soul_B.setEnabled(True & step_B)
		self.binding_soul_B.setStyleSheet(qss_soul_chosen)
	elif soul_B_state == 2:
		self.binding_soul_B.setEnabled(True & step_B)
		self.binding_soul_B.setStyleSheet(qss_soul_faded)
	elif soul_B_state == 3:
		self.binding_soul_B.setStyleSheet(qss_soul_disable)
		self.binding_soul_B.setEnabled(False)
	else:
		return 0