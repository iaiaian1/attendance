// Copyright (c) 2023, iaiaian1 and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Membership', {
	// checkDate: function (){
	//	// frm.doc.registration_date_end < frm.doc.registration_date_start && frappe.throw("Registration date end cant be earlier than start.")
	// 	if (frm.doc.registration_date_end < frm.doc.registration_date_start){
	// 		console.log("bruh")
	// 		debugger
	// 		// frappe.throw has no callback function, clear before throw. Bug is double throw message.
	// 		frm.set_value("registration_date_end", "")
	// 		frappe.throw("Registration date end cant be earlier than start date.")
	// 	}
	// },

	on_load: function(frm) {
		frm.set_value("registration_date_start", frappe.datetime.nowdate())
		// frappe.throw("seomthing")
	},
	registration_date_end: function(frm){
		frm.call(
			{
				doc: frm.doc,
				method: 'check_date',
				always: function (response) {
					if(response.message != undefined){
						frappe.throw(response.message)
					}
				},
				// This gives unable to handle success response frappe
				// callback: function (response) {
				// 	if(response.message != undefined){
				// 		frappe.throw(response.message)
				// 	}
				// 	// consoles.log(response)
				// },
			}
		)
	},
	registration_date_start: function(frm){
		frm.call(
			{
				doc: frm.doc,
				method: 'check_date',
				// args: {
				// 	msg: "Registration date end cant be earlier than start."
				// },
				always: function (response) {
					if(response.message != undefined){
						frappe.throw(response.message)
					}
				},
			}
		)
	},

	// before_save: function(frm){
	// 	frappe.throw("bruh")
	// }
});
