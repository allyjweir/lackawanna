// Generated by CoffeeScript 1.8.0
var markCurrentCollections, populateCollections, updateDatapoint;

$(document).ready(function() {
    // Required for all interaction with the API (SECURITY!!)
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        }
    });

    // Initiate the tabs below the datapoint viewer
    $('#dataoint-tabs a:first').tab('show');

    // Initiate the xeditables to allow users to edit the datapoint's information
    $.fn.editable.defaults.mode = 'popup';
    $(".xeditable-datapoint-details").editable({
        emptytext: "Click to add detail",
        url: function(params) {
            var datapoint_pk, updated_data;
            updated_data = {};
            updated_data[params.name] = params.value;
            datapoint_pk = $("#pk").text();
            return updateDatapoint(datapoint_pk, updated_data);
        },
        success: function(response, newValue) {
            $('.editable-metadata').find( "i:last" ).remove();
        },
        error: function(response) {
            $('.editable-metadata').find( "i:last" ).remove();
        }
    });

    annotatorLoad();
});

function annotatorLoad() {
    var datapoint = $("#datapoint-text").annotator();

    // transcript.data('annotator').subscribe('rangeNormalizeFail', function (ann, range, err) { console.log(ann, range, err); })

    // Setup the Store plugin. Deals with retrieval and storage of annotations
    datapoint.annotator('addPlugin', 'Store', {
        // Define the URLs for actions related to annotations
        urls: {
            create: '/annotations/',
            update: '/annotations/:id',
            destroy: '/annotations/:id',
            search: '/annotations/search/'
        },

        prefix: '/apiv1',

        // Affix the pathname (i.e. '/datapoint/5' or '/transcript/2' to allow for specified retrieval later)
        annotationData: {
            'uri': window.location.pathname,
            'datapoint': $('#datapoint-pk').text()
        },

        loadFromSearch: {
            'uri': window.location.pathname
        }
    });
}

//  If the collections button is clicked, load the collections related to the datapoint and
$('#collections-button').click(function() {
    console.log("Collection Button clicked!");
    $("#collections-list").empty();
    $("div > #loading-spinner").show();
    $("#collections-save-button").button("reset");
    return populateCollections();
});

// Save action, collect all the collections that user selected, update those with the datapoint as a memeber
// or remove it
$("#collections-save-button").click(function() {
    var collection, datapoint_pk, selected, updated_data, _i, _len, _ref;
    $("#collections-save-button").button("loading");
    console.log("Save button Clicked");
    selected = [];
    _ref = $("#collections-list input:checkbox:checked");
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        collection = _ref[_i];
        selected.push($(collection).prop('value'));
    }
    datapoint_pk = $("#pk").text();
    updated_data = {
        "collections": selected
    };
    updateDatapoint(datapoint_pk, updated_data);
    $("#collections-save-button").button("reset");
    return $("#collection-Modal").hide();
});

// Populate the collections modal dialog
populateCollections = function() {
    return $.ajax("/apiv1/collections", {
        type: "GET",
        dataType: "json",
        data: {
            project: $("#project-pk").text()
        },
        error: function(jqXHR, textStatus, errorThrown) {
            return console.log("Couldn't retrieve the datapoint's project's collections (mouthful): " + textStatus);
        },
        success: function(data, textStatus, jqXHR) {
            var collection, _i, _len;
            for (_i = 0, _len = data.length; _i < _len; _i++) {
                collection = data[_i];
                $("#collections-list").append("<input type='checkbox' class='collection-checkbox' id='checkbox-" + collection.pk + "' value='" + collection.pk + "' /> " + collection.name + "<br />");
            }
            return markCurrentCollections();
        }
    });
};

// Marks the collections on the modal dialog that the datapoint is already a member of
markCurrentCollections = function() {
    return $.ajax("/apiv1/datapoints/" + ($("#pk").text()), {
        type: "GET",
        dataType: "json",
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Couldn't retrieve datapoint's info: " + textStatus);
            return null;
        },
        success: function(data, textStatus, jqXHR) {
            var collection, _i, _len, _ref;
            console.log("into success of dp: " + data.collections);
            _ref = data.collections;
            for (_i = 0, _len = _ref.length; _i < _len; _i++) {
                collection = _ref[_i];
                $("#collections-list > #checkbox-" + collection).prop('checked', 'true');
            }
            $("div #loading-spinner").hide();
            return $("div #collections-table").show();
        }
    });
};

// Display loading spinner when user clicks on tag button.
$("#tags-button").click(function() {
    console.log("Tags button clicked");
    $("#tags-list").empty();
    $("div > #loading-spinner").show();
    $("#tags-save-button").button("reset");
    return populateTags();
});

// Save action, collect all the collections that user selected, update those with the datapoint as a memeber
// or remove it
$("#tags-save-button").click(function() {
    var tag, datapoint_pk, selected, updated_data, _i, _len, _ref;
    $("#tags-save-button").button("loading");
    console.log("Save button Clicked");
    selected = [];
    _ref = $("#tags-list input:checkbox:checked");
    for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        tag = _ref[_i];
        selected.push($(tag).prop('value'));
    }
    datapoint_pk = $("#pk").text();
    updated_data = {
        "tags": selected
    };
    updateDatapoint(datapoint_pk, updated_data);
    $("#tags-save-button").button("reset");
    updateTagDisplay(updated_data);
    return $("#tags-modal").hide();
});

// Update the tag display to show the latest set of tags in Lackawanna retrieved using AJAX.
updateTagDisplay = function(updated_data) {
    console.log("Updating Tag display!")
    var display = $("#tag-display");
    display.empty()
    for (i=0; i < updated_data.tags.length; i++) {
        $.ajax("/apiv1/tags", {
            type: "GET",
            dataType: "json",
            data: {
                id: updated_data.tags[i]
            },
            error: function(jqXHR, textStatus, errorThrown) {
                return console.log("Couldn't retrieve the tags: " + textStatus);
            },
            success: function(data, textStatus, jqXHR) {
                display.append ("<a href='/tags/" + data[0].slug + "/'><h3 style='display:inline;'><span class='label label-default tag'>" + data[0].name + "</span></h3></a> ")
            }
        });
    }
}

getTagName = function(tag_pk) {

};

// Populate the tags modal dialog
populateTags = function() {
    return $.ajax("/apiv1/tags", {
        type: "GET",
        dataType: "json",
        error: function(jqXHR, textStatus, errorThrown) {
            return console.log("Couldn't retrieve the tags: " + textStatus);
        },
        success: function(data, textStatus, jqXHR) {
            $("div #loading-spinner").hide();
            var tag, _i, _len;
            for (_i = 0, _len = data.length; _i < _len; _i++) {
                tag = data[_i];
                $("#tags-list").append("<input type='checkbox' class='tag-checkbox' id='checkbox-" + tag.pk + "' value='" + tag.pk + "' /> " + tag.name + "<br />");
            }
            return markCurrentTags();
        }
    });
};

// Marks the collections on the modal dialog that the datapoint is already a member of
markCurrentTags = function() {
    return $.ajax("/apiv1/datapoints/" + ($("#pk").text()), {
        type: "GET",
        dataType: "json",
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Couldn't retrieve datapoint's info: " + textStatus);
            return null;
        },
        success: function(data, textStatus, jqXHR) {
            var tags, _i, _len, _ref;
            console.log("into success of dp: " + data.tags);
            _ref = data.tags;
            for (_i = 0, _len = _ref.length; _i < _len; _i++) {
                tag = _ref[_i];
                $("#tags-list > #checkbox-" + tag).prop('checked', 'true');
            }
            return $("div #tags-list").show();
        }
    });
};

$('#new-tag-create-button').click(function() {
    console.log("new tag created button clicked!!!");
    var new_tag = $('#new-tag-input').val();
    console.log('variable is:' + new_tag);
    $('#new-tag').val('');
    $.ajax("/apiv1/tags/", {
        type: "POST",
        dataType: "json",
        data: {
            name: new_tag
        },
        error: function(jqXHR, textStatus, errorThrown) {
            return console.log("Couldn't retrieve the tags: " + textStatus);
        },
        success: function(tag, textStatus, jqXHR) {
            $('#new-tag-input').val('');  // Empty the new tag field in the modal so its empty for next time use.
            $("#tags-list").append("<input type='checkbox' class='tag-checkbox' checked='true' id='checkbox-" + tag.pk + "' value='" + tag.pk + "' /> " + tag.name + "<br />");
        }
    });
    $('#new-tag-modal').hide();
})


// Retrieves the latest information about the datapoint from the API.
getDatapoint = function () {
    return $.ajax('/apiv1/datapoints', {
        type: "GET",
        dataType: 'json',
        data: {
            pk: $('#datapoint-pk').text()
        },
        error: function(jqXHR, textStatus, errorThrown) {
            return console.log("Couldn't retrieve the datapoint: " + textStatus);
        },
        success: function(data, textStatus, jqXHR) {
            console.log("payload: " + data)
            return data;
        }
    });
};

// Update a datapoint with new data.
// This comes from the x-editables and tags
updateDatapoint = function(datapoint_pk, updated_data) {
    return $.ajax("/apiv1/datapoints/" + datapoint_pk + '/', {
        headers: {
            'X-CSRFToken': $.cookie('csrftoken')
        },
        type: "patch",
        dataType: "json",
        traditional: true,
        data: updated_data,
        error: function(jqXHR, textStatus, errorThrown) {
            return console.log("failed to save updated datapoint: " + textStatus);
        },
        success: function(data, textStatus, jqXHR) {
            return console.log("successfully updated datapoint");
        }
    });
};

// Append an x-editable field with a Font Awesome cog to make it obvious that it is editable.
$('.editable-metadata').hover(
    // .mouseenter function
    function() {
        $( this ).append("  <i class='fa fa-cog'></i>");
    },
    // .mouseexit function
    function() {
        $( this ).find( "i:last" ).remove();
    }
)

// Update a datapoints name in the breadcrumb header.
$('#name').change(function() {
    $('bread-name').text(this.text());
});
