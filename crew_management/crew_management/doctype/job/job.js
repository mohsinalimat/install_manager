// Copyright (c) 2021, Zirrus One and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job', {
    onload: function (frm) {
        if (frappe.user.has_role("System Manager") || frappe.user.has_role("Administrator")) {
            $('#navbar-breadcrumbs').removeClass('hide-item');
            $('.sidebar-toggle-btn').removeClass('hide-item');
            $('.layout-side-section').removeClass('hide-item');
            $('.menu-btn-group').removeClass('hide-item');
        } else if (frappe.user.has_role("Field Lead") || frappe.user.has_role("Field Lead")) {
            $('#navbar-breadcrumbs').addClass('hide-item');
            $('.sidebar-toggle-btn').addClass('hide-item');
            $('.layout-side-section').addClass('hide-item');
            $('.menu-btn-group').addClass('hide-item');
        }
    }
});
