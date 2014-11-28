# Copyright (c) 2013, Web Notes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	condition = ""
	if filters.get("article"):
		condition += "where article = '{}'".format(filters.get("article"))

	columns, data = get_columns(), []

	transactions = frappe.db.sql("""
		select
			article, library_member, transaction_date
		from `tabLibrary Transaction` {0}
	""".format(condition), as_list=1)

	for d in transactions:
		if d[0]:
			article_author = frappe.db.get_value("Article", d[0], "author")
		data.append(d + [article_author])

	return columns, data


def get_columns():
	return [
		"Article:Link/Article:150",
		"Member:Link/Library Member:150",
		"Date:Date:100",
		"Author::120"
	]
