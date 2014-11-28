// Copyright (c) 2013, Web Notes and contributors
// For license information, please see license.txt

frappe.query_reports["Library Transactions"] = {
	"filters": [
		{
			"fieldname":"article",
			"label": __("Article"),
			"fieldtype": "Link",
			"options": "Article"
		}
	]
}
