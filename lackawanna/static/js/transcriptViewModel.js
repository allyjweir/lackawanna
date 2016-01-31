function transcriptViewModel() {
    var self = this;

    self.isEditing = ko.observable(false);
    self.isSubmitting = ko.observable(false);
    self.newTranscriptName = ko.observable("");
    self.newTranscriptText = ko.observable("");

    self.createNewTranscript = function() {
        self.isEditing(true);
    };

    self.discardNewTranscript = function() {
        var discardChoice = confirm("Are you sure you want to discard this new transcript. Any changes will be lost!");
        if (discardChoice) {
            self.isEditing(false);
            self.newTranscriptName("");
            self.newTranscriptText("");
        }
    };

    self.submitTranscript = function() {
        console.log("Going to submit");
        submitTranscriptForm();
        console.log("Have called the thing");
    };

    $( document ).ajaxStart(function() {
        self.isSubmitting(true);
    });

    $( document ).ajaxStart(function() {
        self.isSubmitting(false);
    });

    var submitTranscriptForm = function() {
        var data = {};
        data.datapoint  = $('#pk').text();
        data.owner = $('#user-pk').text();
        data.name = self.newTranscriptName();
        data.text = self.newTranscriptText();
        var url = '/apiv1/transcripts/';
        $.ajax(url, {
            type: "POST",
            dataType: "json",
            data: data,
            success: function() {
                console.log('SUCCESSfully made new transcript');
                //TODO: Go back to the list view and refresh the list.
            },
            error: function() {
                console.log('FAILED to make new transcript');
            }
        });
    };
}

var transcriptViewModel = new transcriptViewModel();
ko.applyBindings(transcriptViewModel, $('#transcripts')[0]);
