/* This page is used to list users within the system.
It also offers staff users the ability to set users to be active/inactive and to define their staff status.
*/

// Tie functions to each button type:
// - Activate Account
// - Deactivate Account
// - Grant Admin Priviledges
// - Revoke Admin Priviledges
//
// Force a page refresh after any change.
//
// Future Improvements:
// TODO: Pagination
// TODO: Remove refresh requirement
// TODO: Improve layout/style

$(document).ready(function() {
    // Required for all interaction with the API (SECURITY!!)
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        }
    });

    $(".activate").click(function() {
        updateUser($(this).attr('id'), {"is_active":"true"})
    });
    $(".deactivate").click(function() {
        updateUser($(this).attr('id'), {"is_active":"false"})
    });
    $(".make-admin").click(function() {
        updateUser($(this).attr('id'), {"is_staff":"true"})
    });
    $(".remove-admin").click(function() {
        updateUser($(this).attr('id'), {"is_staff":"false"})
    });
});

// Generic AJAX call to handle updates to a user's account
// Takes a username and a key/value pair of the data to be updated
// username: used to make the correct URL call to API
// updated_data: used to update the desired value (is_active, is_staff)
updateUser = function(username, updated_data) {
    return $.ajax("/apiv1/users/" + username + '/', {
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        },
        type: "patch",
        dataType: "json",
        traditional: true,
        data: updated_data,
        error: function(jqXHR, textStatus, errorThrown) {
            return console.log("failed to save updated user: " + textStatus);
        },
        success: function(data, textStatus, jqXHR) {
            return console.log("successfully updated user. Time to refresh page");
            window.location.reload(true)
        }
    });
}

$(document).ajaxStop(function(){
    window.location.reload();
});
