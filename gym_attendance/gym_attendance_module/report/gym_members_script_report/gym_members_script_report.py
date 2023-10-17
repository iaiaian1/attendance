# Copyright (c) 2023, iaiaian1 and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if not filters:
		filters = {}

	# Table data with filter/search
	columns = get_columns()
	data = get_filtered_data(filters)

	# Raw data for chart purposes.
	unfiltered_data = get_unfiltered_data()
	chart = get_chart(unfiltered_data)[0]
	report_summary = get_chart(unfiltered_data)[1]
	message = 'Gym Members Report'

	# If filter/search dont match anything
	if not data:
		frappe.msgprint("No records found")
		# In case that no data is returned, swap the columns and data to retain chart
		return data, columns, message, chart, report_summary

	# This is the REQUIRED order or return empty array []
	# https://discuss.frappe.io/t/script-report-python-file-returns-advanced-use/33489/4
	return columns, data, message, chart, report_summary

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
		order_by='first_name desc',
		# as_list=True
	)

	return filtered_data

def get_filters(filters):
	filter = []
	for key, value in filters.items():
		if filters.get(key):
			filter.append({key: ['like', f'{value}%']})
			# filter[key]= value

	# Return a list/array of field objects with key value pair of name : query. 
	return filter

def get_unfiltered_data():
	data = frappe.get_all(
		doctype='Members',
		fields=['first_name', 'last_name', 'age'],
		order_by='first_name desc',
	)

	return data

def get_chart(unfiltered_data):
	underage = 0
	legal_age = 0

	for member in unfiltered_data:
		for key, value in member.items():
			if key == 'age' :
				if value >= 18:
					legal_age += 1
				else:
					underage += 1

	chart = {
		'data':{
			'labels':['Underage','Legal Age'],
			'datasets':[
				#In axis-mixed charts you have to list the bar type first
				{'name': 'Members','values': [underage, legal_age]},
				# {'name':'Vowel','values':[0,1,0,0],'chartType':'line'}
			]
		},
		'type':'pie'
	}

	report_summary = [
		{"label":"Underage Gym Goer","value":underage,'indicator':'Red'},
		{"label":"Legal-age Gym Goer","value":legal_age,'indicator':'Blue'}
	]
	
	return chart, report_summary