// Retrieves the project's pk from the URL and populates the project field in the form automatically
$(document).ready(function() {
    var project_pk = getQueryVariable('project');
    $("#id_project").val(dp_pk);

});

function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
    console.log('Query variable %s not found', variable);
}
