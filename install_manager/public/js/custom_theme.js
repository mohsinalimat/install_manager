$(document).ready(function () {
    // in Frappe, theme is personalized to individual users. Them "light" is default if the user
    // has not chosen any other theme for himself/herself. Frappe doesn't provide any means (as of version 13)
    // to change the default theme (see file app.py in frappe framework). What we did here is kind of hacking.
    // The drawback of this hack is that: if a user switches his preferred theme to "light",
    // it will come back to this default "dark" when he presses F5!
    $('html').attr('data-theme', 'dark');
});

