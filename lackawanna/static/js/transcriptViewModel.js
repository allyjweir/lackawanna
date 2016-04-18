function transcriptViewModel() {
    var self = this;

    self.selectedTranscript = ko.observable();
    self.editableTranscriptName = ko.observable("");
    self.editableTranscriptText = ko.observable("");

    // Used to manage state
    self.isViewing = ko.observable(false);
    self.isEditing = ko.observable(false);
    self.isCreating = ko.observable(false);
    self.isSubmitting = ko.observable(false);
    self.isLoading = ko.observable(false);

    // Used for UI stuff
    self.addedNewTranscript = ko.observable(false);
    self.deletedTranscript = ko.observable(false);
    self.successfulUpdatedTranscript = ko.observable(false);

    self.doingStuff = ko.computed(function() {
      return self.isCreating() || self.isViewing() || self.isEditing() || self.isLoading();
    });

    self.createNewTranscript = function() {
        self.isCreating(true);
    };

    var resetTranscriptForm = function() {
        self.editableTranscriptName("");
        self.editableTranscriptText("");
    };

    self.discardNewTranscript = function() {
        var discardChoice = confirm("Are you sure you want to discard this new transcript. Any changes will be lost!");
        if (discardChoice) {
            self.isCreating(false);
            resetTranscriptForm();
        }
    };

    self.submitNewTranscript = function() {
        submitNewTranscriptForm();
    };

    $( document ).ajaxStart(function() {
        self.isSubmitting(true);
    });

    $( document ).ajaxStop(function() {
        self.isSubmitting(false);
    });

    /**
     * Opens the editing interface for the current selectedTranscript
     */
    self.editTranscript = function() {
      self.isCreating(true);
      self.isEditing(true);
      self.editableTranscriptName(self.selectedTranscript().name);
      self.editableTranscriptText(self.selectedTranscript().text);
    };

    self.stopEditing = function() {
      var choice = confirm("Are you sure you want to stop editing? Any changes will be lost!");
      if (choice) {
        self.isEditing(false);
        self.selectedTranscript(null);
      }
    };

    self.updateTranscript = function() {
      submitUpdatedTranscript();
    }

    self.viewTranscript = function(id) {
      console.log("you clicked view transcript");
      retrieveTranscript(id);
      self.isViewing(true);
    };

    self.stopViewing = function() {
      self.isViewing(false);
      self.selectedTranscript(false);
    };

    self.deleteSelectedTranscript = function() {
      if (confirm("Are you sure you want to delete this transcript?")) {
        deleteTranscript(self.selectedTranscript().pk);
      } else {
        alert("Okay, will not delete transcript.");
      }
    }

    var retrieveTranscript = function(id) {
      self.isLoading(true);
      var url = '/apiv1/transcripts/' + id;
      $.ajax(url, {
        type: "GET",
        dataType: "json",
        success: function(data) {
          self.selectedTranscript(data);
          self.isLoading(false);
        },
        error: function() {
          self.isLoading(false);
          console.log("Failed to query the API for the requested transcript");
          alert("Failed to retrieve the transcript you requested. Please refresh, try again. If issues continue, please contact support.");
        }
      });
    };

    var deleteTranscript = function(pk) {
      console.log("deleting a transcript");
      self.isViewing(false);
      self.isLoading(true);
      var url = "/apiv1/transcripts/" + pk;
      $.ajax(url, {
        type: "DELETE",
        dataType: "json",
        success: function(data) {
          self.isLoading(false);
          self.selectedTranscript(null);
          self.deletedTranscript(true);
        },
        error: function(data) {
          self.isViewing(true);
          self.isLoading(false);
          alert("Failed to delete transcript. Please try again or contact support.");
        }
      });
    }

    var submitUpdatedTranscript = function() {
      self.isSubmitting(true);
      self.selectedTranscript().name = self.editableTranscriptName();
      self.selectedTranscript().text = self.editableTranscriptText();
      var data = self.selectedTranscript();
      var url = '/apiv1/transcripts/' + self.selectedTranscript().pk;
      $.ajax(url, {
          type: "PUT",
          dataType: "json",
          data: data,
          success: function() {
              console.log('SUCCESSfully updated transcript');
              self.isViewing(false);
              self.isCreating(false);
              self.isEditing(false);
              self.successfulUpdatedTranscript(true);
              self.selectedTranscript(null);
          },
          error: function() {
              console.log('FAILED to update transcript');
              alert("Failed to update your transcript. Don't worry, your transcript isn't lost! Please try re-submitting it. If this continues to fail, please contact support.");
          }
      });
    }

    var submitNewTranscriptForm = function() {
        var data = {};
        data.datapoint  = $('#pk').text();
        data.owner = $('#user-pk').text();
        data.name = self.editableTranscriptName();
        data.text = self.editableTranscriptText();
        var url = '/apiv1/transcripts/';
        $.ajax(url, {
            type: "POST",
            dataType: "json",
            data: data,
            success: function() {
                console.log('SUCCESSfully made new transcript');
                resetTranscriptForm();
                self.addedNewTranscript(true);
                self.isCreating(false);
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
