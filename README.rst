
=================================================
Product External References by Customer
=================================================

**Version:** 17.0.1.0.0 | **Price:** USD 150.8 | **License:** LGPL-3  

This module enables you to store and manage customer-specific external references for products. It enhances your sales and purchase processes by integrating additional reference data and vendor datasheet URLs into orders.


🚀 **Key Features**
---------------------
✅ **External References:**
   - Store multiple external references for each product, specific to customers.

✅ **Datasheet URL Integration:**
   - Manage and display datasheet URLs in supplier information, purchase orders, and sales orders.

✅ **Enhanced Sales Order Workflow:**
   - Add a **Recompute Descriptions** button to refresh order line descriptions based on:
     - Internal product reference.
     - Customer-specific external reference.
     - Vendor reference and datasheet URL.

✅ **Seamless Integration:**
   - Extends core Odoo models (`product.template`, `product.supplierinfo`, `purchase.order`, `sale.order`).
   - Works with minimal configuration.


📥 **Installation**
-------------------
1. **Copy the Module Folder:**
   - Place the `product_external_ref_tag` folder into your custom `addons` directory.

2. **Update the App List:**
   - Restart your Odoo server.
   - Go to **Apps** → Click **Update Apps List**.

3. **Install the Module:**
   - Search for **"Product External References by Customer"** in the Apps menu.
   - Click **Install**.


🚀 **Usage**
------------
### **Product Template**
🔹 **External References Tab:**
   - Manage customer-specific external references directly from the product template.

### **Supplier Information**
🔹 **Datasheet URL Field:**
   - View and edit datasheet URLs in supplier information forms and tree views.

### **Purchase Orders**
🔹 **Datasheet URL on Order Lines:**
   - Auto-fills based on vendor details when product or vendor changes.

### **Sales Orders**
🔹 **Reference Types Supported:**
   - **Internal Ref:** Uses the product's default internal reference.
   - **External Ref:** Fetches the customer-specific external reference.
   - **Vendor Ref:** Uses the vendor’s product code and datasheet URL.

🔹 **Recompute Descriptions Button:**
   - Allows users to refresh order line descriptions dynamically.


📸 **Screenshots**
------------------
.. image:: /product_external_ref_tags/static/description/product_template_tab.png
   :alt: External References tab on Product Template

.. image:: /product_external_ref_tags/static/description/supplier_info_url.png
   :alt: Datasheet URL in Supplier Info

.. image:: /product_external_ref_tags/static/description/sales_order_recompute.png
   :alt: Sales Order Recompute Button


💡 **FAQs**
-------------------
For frequently asked questions, check **FAQ.md**.


🛠 **Support**
-------------------
For support or feature requests, please contact:
📧 **Email:** support@odoo.co.ke  
🌐 **Website:** [metroict.com](https://odoo.co.ke)


📌 **Changelog**
-------------------
See **CHANGELOG.md** for version history.

---

