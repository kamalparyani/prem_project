# File: custom_sales_order.py

from __future__ import unicode_literals
import frappe

def display_some_message(doc, method=None):
    #frappe.msgprint()
    frappe.throw("hellow throw")
    return 0

# def create_project_based_on_template(doctype, sales_order):
#     #frappe.throw("hellow world")
#     frappe.msgprint("how are you")
    
#     # Get the Sales Order document
#     sales_order_doc = frappe.get_doc(doctype, sales_order)
    
#     # Get the template item from the Item Master
#     template_item = frappe.get_value("Item", sales_order_doc.items.item_code, "custom_project_template")
    

    
#     if template_item:
#         # Create a new Project based on the template
#         project_doc = frappe.new_doc("Project")
#         project_doc.update({
#             "project_name": sales_order_doc.name + "-Project",  # You might want to customize this
#             "project_template": template_item,
#             # Add other fields as needed
#         })
#         project_doc.insert(ignore_permissions=True)  # Insert the project without permission checks
#         frappe.msgprint(f"Project {project_doc.name} created based on template {template_item}")
#     else:
#         frappe.msgprint("Template not found for the item in Sales Order.")


# def create_project_based_on_template(doctype, docname):
#     try:
#         # Get the Sales Order document
#         sales_order_doc = frappe.get_doc(doctype, docname)
        
#         # Ensure that the sales order document has an item code
#         if sales_order_doc.get("items"):
#             # Get the first item in the items list
#             item = sales_order_doc.get("items")[0]
            
#             # Get the template item from the Item Master
#             template_item = frappe.get_value("Item", item.item_code, "custom_project_template")
            
#             if template_item:
#                 # Create a new Project based on the template
#                 project_doc = frappe.new_doc("Project")
#                 project_doc.update({
#                     "project_name": sales_order_doc.name + "-Project",  # You might want to customize this
#                     "project_template": template_item,
#                     "sales_order": sales_order_doc.name,
#                     # Add other fields as needed
#                 })
#                 project_doc.insert(ignore_permissions=True)  # Insert the project without permission checks
#                 frappe.msgprint(f"Project {project_doc.name} created based on template {template_item}")
#             else:
#                 frappe.msgprint("Template not found for the item in Sales Order.")
#         else:
#             frappe.msgprint("No items found in the Sales Order.")
#     except Exception as e:
#         frappe.msgprint(f"Error: {e}")
def create_project_based_on_template(doctype, docname):
    try:
        # Get the Sales Order document
        sales_order_doc = frappe.get_doc(doctype, docname)
        
        # Ensure that the sales order document has items
        if sales_order_doc.get("items"):
            for item in sales_order_doc.get("items"):
                # Get the template item from the Item Master
                template_item = frappe.get_value("Item", item.item_code, "custom_project_template")
                
                if template_item:
                    # Create a new Project based on the template for each item
                    project_doc = frappe.new_doc("Project")
                    project_doc.update({
                        "project_name": sales_order_doc.get("transaction_date").strftime("%B") + "-" + item.item_code + "-Project",   # Customize as needed
                        "project_template": template_item,
                        "sales_order": sales_order_doc.name,  # Connect project to sales order
                        "customer": sales_order_doc.customer # connect customer to project
                        # Add other fields as needed
                    })
                    project_doc.insert(ignore_permissions=True)  # Insert the project without permission checks
                    frappe.msgprint(f"Project {project_doc.name} created based on template {template_item} for item {item.item_code}")
                else:
                    frappe.msgprint(f"No template found for item {item.item_code} in Sales Order.")
        else:
            frappe.msgprint("No items found in the Sales Order.")
    except Exception as e:
        frappe.msgprint(f"Error: {e}")
