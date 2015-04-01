$(document).ready(function() {
    // Required for all interaction with the API (SECURITY!!)
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        }
    });

    // Changes the saved search button's appearance if hovering over it.
    $('#saved-search').hover(
        function() {
            $(this).toggleClass('btn-default');
            $(this).toggleClass('btn-danger');
            $(this).html("<i class='fa fa-times'></i> Remove saved search");
        }, function() {
            $(this).toggleClass('btn-default');
            $(this).toggleClass('btn-danger');
            $(this).text("Saved search");
        }
    );

    // Changes the saved search button's appearance if hovering over it.
    $('#save-search').hover(
        function() {
            $(this).toggleClass('btn-default');
            $(this).toggleClass('btn-primary');
        }, function() {
            $(this).toggleClass('btn-default');
            $(this).toggleClass('btn-primary');
        }
    );

    // Lets the user save a search so that it can be quickly recalled later. If successful it hides the 'save'
    // button and replaces it with a 'saved' button that if clicked will remove the saved search from the system.
    $('#save-search').on('click', function() {
        var search_term = $('#search-term').text();
        $.ajax("/apiv1/savedsearch/", {
            type: "POST",
            dataType: "json",
            data: {
                search_term: search_term
            },
            error: function(jqXHR, textStatus, errorThrown) {
                return console.log("Couldn't save the user's search: " + textStatus);
            },
            success: function(savedsearch, textStatus, jqXHR) {
                console.log("new savedsearch created!: " + savedsearch.id);
                $('#save-search').attr('style', 'display:none;');
                $('#saved-search').attr('style', 'display:inline;');
                $('#savedsearch-pk').text(savedsearch.id);
            }
        });
    });

    // Used when trying to remove a saved search from the system. If successful it will hide the 'saved'
    // status button and then reveal a button allowing the user to 'save' it as a saved search.
    $('#saved-search').on('click', function() {
        var savedsearch_pk = $('#savedsearch-pk').text();
        if (savedsearch_pk == "0") {
            return console.log('error: saved search pk is invalid');
        }
        else {
            $.ajax(('/apiv1/savedsearch/' + savedsearch_pk), {
                type: "DELETE",
                error: function(jqXHR, textStatus, errorThrown) {
                    return console.log("Failed to delete user's saved search: " + textStatus);
                },
                success: function(textStatus, jqXHR) {
                    console.log('successfully removed saved search');
                    $('#saved-search').attr('style', 'display:none;');
                    $('#save-search').attr('style', 'display:inline;');
                }
            });
        }

    });

    $('#id_q').addClass('form-control');

});
