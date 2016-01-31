function transcriptViewModel() {
    var self = this;

    self.isEditing = ko.observable(false);
    self.isSubmitting = ko.observable(false);
    self.addedNewTranscript = ko.observable(false);
    self.newTranscriptName = ko.observable("");
    self.newTranscriptText = ko.observable("");

    self.createNewTranscript = function() {
        self.isEditing(true);
    };

    var resetTranscriptForm = function() {
            self.newTranscriptName("");
            self.newTranscriptText("");
    };

    self.discardNewTranscript = function() {
        var discardChoice = confirm("Are you sure you want to discard this new transcript. Any changes will be lost!");
        if (discardChoice) {
            self.isEditing(false);
            resetTranscriptForm();
        }
    };

    self.submitTranscript = function() {
        submitTranscriptForm();
    };

    $( document ).ajaxStart(function() {
        self.isSubmitting(true);
    });

    $( document ).ajaxStop(function() {
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
                resetTranscriptForm();
                self.addedNewTranscript(true);
                self.isEditing(false);
            },
            error: function() {
                console.log('FAILED to make new transcript');
                alert("Failed to submit your new transcript. Don't worry, your transcript isn't lost! Please try re-submitting it. If this continues to fail, please contact support (Ally).");
            }
        });
    };
}

var transcriptViewModel = new transcriptViewModel();
ko.applyBindings(transcriptViewModel, $('#transcripts')[0]);
