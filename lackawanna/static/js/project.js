$(document).ready(function() {
	$('#datapoint-tabs a:first').tab('show');

	$('#datapoint-table').DataTable();

	$('[data-toggle="tooltip"]').tooltip()
});
