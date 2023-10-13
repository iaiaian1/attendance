# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if not filters:
		filters = {}

	columns, data = [], []

	columns = get_columns()
	data = get_filtered_data(filters)

	if not data:
		frappe.msgprint("No records found")
		return columns, data

	return columns, data

def get_columns():
	return [
		{
			"fieldname": "first_name",
			"label": "First Name",
			"fieldtype": "Data",
		},
		{
			"fieldname": "last_name",
			"label": "Last Name",
			"fieldtype": "Data",
		},
		{
			"fieldname": "age",
			"label": "Age",
			"fieldtype": "Data",
		}
	]

def get_filtered_data(filters):
	filter = get_filters(filters)
	filtered_data = frappe.get_all(
		doctype='Members',
		fields=['first_name', 'last_name', 'age'],
		filters=filter,
		order_by='first_name desc'
	)

	return filtered_data

def get_filters(filters):
	filter = {}
	for key, value in filters.items():
		if filters.get(key):
			filter[key]= value

	return filter