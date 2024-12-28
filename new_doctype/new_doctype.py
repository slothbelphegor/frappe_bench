# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NewDoctype(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.custom.doctype.product_detail.product_detail import ProductDetail
		from frappe.types import DF

		customer: DF.Data
		details: DF.Table[ProductDetail]
		order_number: DF.Data | None
		status: DF.Literal["Pending", "Completed", "Cancelled"]
	# end: auto-generated types
	pass
