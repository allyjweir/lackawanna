// Generated by CoffeeScript 1.8.0
(function() {
  $('#create-dropdown').tooltip();

  $("input.typeahead").typeahead({
      onSelect: function(item) {
          console.log(item);
      },
      ajax: {
          url: "/core/auto",
          timeout: 500,
          triggerLength: 1,
          method: "get",
          loadingClass: "loading-circle",

          preProcess: function (data) {
              if (data.success === false) {
                  console.log("Fail in autocomplete retrieval!")
            }
              // We good!
              console.log(data)
              return data;
          }
      }
  });

  $('#savedsearch-dropdown').on('click', function() {
      var current_user = $('#user-pk').text();
      $.ajax("/apiv1/savedsearch/", {
          type: "GET",
          dataType: "json",
          data: {
              owner: current_user
          },
          error: function(jqXHR, textStatus, errorThrown) {
              return console.log("Couldn't save the user's search: " + textStatus);
          },
          success: function(savedsearches, textStatus, jqXHR) {
              console.log("User's saved searches retrieved");
              $('#savedsearch-loading').attr('style', 'display:none;');

              for (i=0; i<savedsearches.length; i++) {
                  // The search interface expects its query to have '+' rather than spaces. This makes the conversion.
                  var search_term_plus = savedsearches[i].search_term.replace(/\s+/g, '+');
                  $('#savedsearch-dropdown > ul').append("<li class='savedsearch-result'><a href=/search/?q=" + search_term_plus + ">" + savedsearches[i].search_term + " </a></li>")
              }
          }
      });
      $(this).on('click', function() {
          $('.savedsearch-result').remove();
          $('#savedsearch-loading').attr('style', 'display:inline;');
      })
  });

}).call(this);
