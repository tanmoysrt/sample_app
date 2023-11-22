import frappe
from frappe.exceptions import DoesNotExistError


@frappe.whitelist()
def add_to_db(data):
    try:
        record = frappe.new_doc("test_doc")
        record.data = data
        record.save()
        frappe.db.commit()

        return "OK"
    except DoesNotExistError:
        return None
