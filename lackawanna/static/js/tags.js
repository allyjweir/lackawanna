$(document).ready(function() {
	// Required for all interaction with the API (SECURITY!!)
	$.ajaxSetup({
		headers: {
			'X-CSRFToken': $.cookie('csrftoken')
		}
	});

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
	    $("#tags-modal").modal('hide');
	});

	// Update the tag display to show the latest set of tags in Lackawanna retrieved using AJAX.
	updateTagDisplay = function(updated_data) {
	    console.log("Updating Tag display!")
	    var display = $("#tag-display");
	    display.empty()
	    for (i=0; i < updated_data.tags.length; i++) {
	        $.ajax("/apiv1/tags/", {
	            type: "GET",
	            dataType: "json",
	            data: {
	                id: updated_data.tags[i]
	            },
	            error: function(jqXHR, textStatus, errorThrown) {
	                return console.log("Couldn't retrieve the tags: " + textStatus);
                    alert("Could not retrieve the latest tags from the server. Please refresh the page and try again. If this continues to fail, please contact support.")
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
	    return $.ajax("/apiv1/tags/", {
	        type: "GET",
	        dataType: "json",
	        error: function(jqXHR, textStatus, errorThrown) {
	            return console.log("Couldn't retrieve the tags: " + textStatus);
                alert("Could not retrieve the latest tags from the server. Please refresh the page and try again. If this continues to fail, please contact support.")
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
	    $('#new-tag-modal').modal('hide');
	})});
