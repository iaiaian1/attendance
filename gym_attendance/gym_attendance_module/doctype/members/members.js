// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Members', {
	refresh: function(frm) {
		if (frm.is_new()){
			// Intro
			frm.set_intro('Fill up for new Gym Member', 'blue')
		}else{
			// Create membership button available only when form is not new.
			frm.add_custom_button("Create Membership", () => {
				// console.log("Foo")
				frappe.new_doc("Gym Membership", {
					// member: member can be shortened
					member: cur_frm.docname
				})
			})
		}
		// debugger
		// let dialog = new frappe.ui.Dialog(
		// 	{
		// 		title: "New Gym Membership",
		// 		fields: [
		// 			{
		// 				value: "Bruh",
		// 				fieldtype: "Link",
		// 				fieldname: "member",
		// 				label: "Member",
		// 				options: "Members"
		// 			},
		// 		],
		// 		primary_action_label: "Create Gym Membership",
		// 		primary_action: (data) => {
		// 			let { member } = data
		// 			console.log(member)

		// 			frappe.new_doc("Gym Membership", {
		// 				// member: member can be shortened
		// 				member
		// 			})
		// 		}
		// 	}
		// )
		// dialog.show()
		// Prompt when clicked
		// frappe.prompt(
		// 	// console.log(frm.doc.name)
		// 	// First param, fields
		// 	[
		// 		{
		// 			'fieldname': 'members',
		// 			'fieldtype': 'Link',
		// 			'label': 'Member',
		// 			'reqd': 1,
		// 			// {'fieldname': 'birth', 'fieldtype': 'Date', 'label': 'Birth Date', 'reqd': 1}
		// 		},
		// 		{
		// 			'fieldname': 'membership_type',
		// 			'fieldtype': 'Select',
		// 			'label': 'Membership Type',
		// 			'default': 'Regular',
		// 			'options': [
		// 				'Regular',
		// 				'Student'
		// 			],
		// 			'reqd': 1
		// 		},
		// 		{
		// 			'fieldname': 'registration_date_start',
		// 			'fieldtype': 'Date',
		// 			'label': 'Registration Date Start',
		// 			'reqd': 1
		// 		},
		// 		{
		// 			'fieldname': 'registration_date_end',
		// 			'fieldtype': 'Date',
		// 			'label': 'Registration Date End',
		// 			'reqd': 1
		// 		}
		// 	], // End of first param
		// 	// Start of 2nd param, function to call
		// 	function(values){
		// 		doc = frappe.new_doc('Gym Membership', {values})
		// 		// doc.title = 'New Task 2'
		// 		doc.insert()
		// 	}, // End of 2nd param, function to call
		// 	'Gym Membership Registration'
		// )
	}
});
