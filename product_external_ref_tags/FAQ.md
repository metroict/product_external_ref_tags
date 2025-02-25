# Frequently Asked Questions (FAQ)

## Q1: What problem does this module solve?
**A:** This module allows you to store customer-specific external references for products, simplifying order processing by automatically using the correct reference based on customer, product, or vendor information.

## Q2: How do I install the module?
**A:**  
1. Copy the module folder to your custom addons directory.
2. Update your Odoo app list.
3. Install the module from the Apps menu in Odoo.

## Q3: What are the prerequisites for this module?
**A:**  
- Odoo 17 Enterprise or Community.
- The core modules `sale_management`, `product`, and `purchase` must be installed.

## Q4: How is the sales order line description computed?
**A:**  
Based on the selected reference type:
- **Internal Ref:** Uses the product's default code.
- **External Ref:** Searches for a customer-specific external reference.
- **Vendor Ref:** Uses the vendor's product code and datasheet URL.

## Q5: What if a required external reference or vendor code is missing?
**A:**  
The module will raise a user error prompting you to add the missing reference, ensuring data consistency.

## Q6: How can I get support or request a feature?
**A:**  
For support or feature requests, please contact us at support@odoo.co.ke.

---

If you have further questions, please feel free to reach out!
