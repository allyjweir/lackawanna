// Generated by CoffeeScript 1.8.0
(function() {
  $('[data-toggle="tooltip"]').tooltip()


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


  $('#projects-dropdown').on('click', function() {
      var current_user = $('#user-pk').text();
      $.ajax("/apiv1/projects/", {
          type: "GET",
          dataType: "json",
          data: {
              owner: current_user
          },
          error: function(jqXHR, textStatus, errorThrown) {
              return console.log("Couldn't access the user's projects: " + textStatus);
          },
          success: function(projects, textStatus, jqXHR) {
              console.log("User's projects retrieved");
              $('#projects-loading').attr('style', 'display:none;');

              // If the user has no projects then let them know and suggest to create one.
              if (projects.length === 0) {
                  $('#projects-dropdown > ul').append("<li class='projects-result disabled'><a href='#'>You have no projects</a></li>")

              }
              // Else enumerate these with links to each project.
              else {
                  for (i=0; i<projects.length; i++) {
                      // The search interface expects its query to have '+' rather than spaces. This makes the conversion.
                      $('#projects-dropdown > ul').append("<li class='projects-result'><a href='/projects/" + projects[i].slug + "'>" + projects[i].name + "</a></li>")
                  }
              }
              // Append the dropdown with a link to create a new project. This shoud display regardless of if a user has pre-existing projects.
              $('#projects-dropdown > ul').append("<li role='presentation' class='dropdown-header projects-result'>New Project</li>");
              $('#projects-dropdown > ul').append("<li role='presentation' class='projects-result'><a href='/projects/create/'><i class='fa fa-plus'></i> Create a new project</a></li>");
          }
      });
      $(this).on('click', function() {
          $('.projects-result').remove();
          $('#projects-loading').attr('style', 'display:inline;');
      })
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

              // If the user has no saved searches then let them know
              if (savedsearches.length === 0) {
                  $('#savedsearch-dropdown > ul').append("<li class='savedsearch-result disabled'><a href='#'>You have no saved searches.</a></li>")
              }
              // Else list their saved searches, giving links to them
              else {
                  for (i=0; i<savedsearches.length; i++) {
                      // The search interface expects its query to have '+' rather than spaces. This makes the conversion.
                      var search_term_plus = savedsearches[i].search_term.replace(/\s+/g, '+');
                      $('#savedsearch-dropdown > ul').append("<li class='savedsearch-result'><a href=/search/?q=" + search_term_plus + ">" + savedsearches[i].search_term + " </a></li>")
                  }
              }
          }
      });
      $(this).on('click', function() {
          $('.savedsearch-result').remove();
          $('#savedsearch-loading').attr('style', 'display:inline;');
      })
  });

}).call(this);
