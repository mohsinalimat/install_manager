let url = location.href;

$(document).ready(function () {
    checkFieldCrewWhiteList();
});

document.body.addEventListener('click', () => {
    requestAnimationFrame(() => {
        let currentRoute = location.href;
        checkFieldCrewWhiteList();
        if (url !== currentRoute) {
            url = location.href;
            if (!currentRoute.includes('job-management')) {
                $('#navbar-breadcrumbs').removeClass('hide-item');
                $('.navbar .container .job-title').addClass('hide-item')
            } else {
                $('.navbar .container .job-title').removeClass('hide-item')
                $('#navbar-breadcrumbs').addClass('hide-item');
            }
        }
    });
}, true);

function checkFieldCrewWhiteList() {
    const field_crew_url_white_list = [
        "app/user-profile",
        "app/job-management",
        "app/user/",
        "app/job/JOB-",
    ]
    if ((frappe.user.has_role("Field Lead") || frappe.user.has_role("Field Installer")) && !frappe.user.has_role("Back Office Staff")) {
        let inWhiteListUrl = false;
        field_crew_url_white_list.forEach(item => {
            if (location.href.includes(item)) {
                inWhiteListUrl = true;
            }
        })

        if (!inWhiteListUrl) {
            window.location.href = "/app/job-management"
        }
    }
}
