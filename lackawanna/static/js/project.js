$(document).ready(function() {
	// Enable Bootstrap's Panels
	$('#datapoint-tabs a:first').tab('show');

	// Enable datatables to work
	$('#datapoint-table').DataTable();

	// Enable Bootstrap's tooltips
	$('[data-toggle="tooltip"]').tooltip()
});
