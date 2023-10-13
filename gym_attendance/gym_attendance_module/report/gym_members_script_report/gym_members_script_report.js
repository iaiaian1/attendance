// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Gym Members Script Report"] = {
	"filters": [
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
};
