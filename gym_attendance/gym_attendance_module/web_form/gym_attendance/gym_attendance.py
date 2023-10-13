from __future__ import unicode_literals

import frappe

def get_context(context):
	
	def on_save(self):
		frappe.throw("bruh")

	# pass
