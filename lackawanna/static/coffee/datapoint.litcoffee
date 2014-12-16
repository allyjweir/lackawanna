Datapoint Viewer
======
All of this code supports a user's interaction with the datapoint viewer. The core interactions it supports are:
1. Modifying the datapoint's metadata
2. Viewing the datapoint itself
3. Annotating the datapoint


	$(document).ready ->
		$('#dataoint-tabs a:first').tab('show')

		$.fn.editable.defaults.mode = 'inline'

		$("#author").editable
			url: (params) ->
				console.log("Time to save x-editable new stuff: #{params.update}")
				updated_data={}
				updated_data[params.name] = params.value
				datapoint_pk = $("#pk").text()
				updateDatapoint(datapoint_pk, updated_data)

		$("#source").editable
			url: (params) ->
				console.log("Time to save x-editable new stuff: #{params.update}")
				updated_data={}
				updated_data[params.name] = params.value
				datapoint_pk = $("#pk").text()
				updateDatapoint(datapoint_pk, updated_data)

		console.log("Page loaded")


Collection Update Modal
-----
#### Collections Button clicked
This is called when a user wants to modify what collection's that their datapoint is in/not in.

	$('#collections-button').click ->
		console.log("Collection Button clicked!")

Clear any previous data added to the collections-table div and make sure that the loading spinner is showing.

		$("div > #loading-spinner").show()
		$("#collections-list").empty()
		$("#collections-save-button").button("reset")

Now fill the modal with the latest information retrieved from the database

		populateCollections()

#### Collection Save/Update Button clicked

	$("#collections-save-button").click ->
		$("#collections-save-button").button("loading")
		console.log("Save button Clicked")

Extract all the selected collection's values (their pk) from the checkbox inputs.

		selected = []
		for collection in $("#collections-list input:checkbox:checked")
			selected.push($(collection).prop('value'))

Taking these we make a PATCH request to update a Datapoint's collections through the API.


		datapoint_pk = $("#pk").text()
		updated_data = {"collections": selected}

		updateDatapoint(datapoint_pk, updated_data)

		$("#collections-save-button").button("reset")
		$("#collection-Modal").hide()

This function retrieves the collections of a specific datapoint.

	populateCollections = () ->
		$.ajax "http://localhost:8080/apiv1/collections",
			type: "GET"
			dataType: "json"
			data: {project: $("#project-pk").text()}
			error: (jqXHR, textStatus, errorThrown) ->
				console.log("Couldn't retrieve the datapoint's project's collections (mouthful): #{textStatus}")

On _success_ insert HTML list into the model dialog for each collection

			success: (data, textStatus, jqXHR) ->
				for collection in data
					$("#collections-list").append(
						"<input type='checkbox' class='collection-checkbox' id='checkbox-#{collection.pk}' value='#{collection.pk}' /> #{collection.name}<br />
						")

Then mark the ones that the datapoint is already a member of

				markCurrentCollections()

Pizza Land is okay!!

	updateDatapoint = (datapoint_pk, updated_data) ->

		$.ajax "http://localhost:8080/apiv1/datapoints/#{datapoint_pk}",
			headers:{'X-CSRFToken':$.cookie('csrftoken')}
			type: "patch"
			dataType: "json"
			traditional:true
			data: updated_data
			error: (jqXHR, textStatus, errorThrown) ->
				console.log("failed to save updated datapoint: #{textStatus}")
				#Show a failure message and ask them to try again.
			success: (data, textStatus, jqXHR) ->
				console.log("successfully updated datapoint")
				#Show success message using bootstrap success bit.


	markCurrentCollections = () ->

Retrieve the current datapoint's collections to mark them

		$.ajax "http://localhost:8080/apiv1/datapoints/#{$("#pk").text()}",
			type: "GET"
			dataType: "json"

If it fails, show an error button to offer retry.

			error: (jqXHR, textStatus, errorThrown) ->
				console.log("Couldn't retrieve datapoint's info: #{textStatus}")
				return null

For each collection (their value is in an array in `data.collections`) mark the checkbox as ticked.

			success: (data, textStatus, jqXHR) ->
				console.log("into success of dp: #{data.collections}")
				for collection in data.collections
					$("#collections-list > #checkbox-#{collection}").prop('checked', 'true')
				$("div #loading-spinner").hide()
				$("div #collections-table").show()
