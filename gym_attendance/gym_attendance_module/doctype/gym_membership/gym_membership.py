# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMembership(Document):
	# pass
	def before_save(self):
		isExists = frappe.db.exists("Gym Membership", {
			"member": self.member,
			"docstatus": 1,
			"registration_date_end": ('>', self.registration_date_start),
		})
		if isExists:
			frappe.throw("Gym Member has an ongoing subscription!")
		# frappe.throw("BRo")

	@frappe.whitelist()
	def check_date(self, msg):
		# when condition is true, set date end value and return throw message, creating a pseudo callbank for frappe.throw
		# Seperate conditionals for looks, can be one lined.
		if type(self.registration_date_end) is str and type(self.registration_date_start) is str:
			if self.registration_date_end < self.registration_date_start:
				self.registration_date_end = ""
				return "Registration date end cant be earlier than start."
					# frappe.throw(
					# 	title='Date Error',
					# 	msg=msg,
					# )