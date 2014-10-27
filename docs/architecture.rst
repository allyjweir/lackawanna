Architecture
=========

Lackawanna is an application with a clear division in functionality which has facilitated its division into specific applications. These apps each have a clear area of responsibility in creating a working system that meets the set requirements from the client.

**Core**
This holds commonly used resources and utilities. This is the home of the API URLConfs. All new API calls that are created need to be added to this document. This allows all of the calls to come under lackawanna.com/api/??? URL structure.

**Annotate**
This app is responsible for all types of annotation facilities as an analysis tool upon datapoints in the system. This means offering an API for the various front-end annotation libraries in use to store and retrieve annotations applied to a datapoint.

**Datapoint**
This is responsible for the storing and viewing of all types of datapoints be it PDF, audio, video, text, tweet. This includes having a robust viewing platform for all types of media as well as being able to add metadata and leave comments on the datapoint. In future releases, datapoints will be fully searchable and filterable.

**Transcript**
This app is to facilitate the transcription of datapoints. These themselves are almost specialised datapoints. Multiple transcripts are allowed per datapoint to allow users to make different interpretations of datapoints and to explore them fully to find new meaning. These are also commentable.

**Dashboard**
This is a simple portal to Lackawanna. This will likely be the most fluid of views once created. It's role is to inform users of the latest changes to projects, collections and datapoints they care about while giving them quick links to get working.

**Project**
This serves as a mechanism to organise datapoints around a central theme or event. This gives research direction. An example could be the London 2011 Riots.

**Collection**
Taking the example from project, it could be broken down into collections of datapoints within a project to allow for easier analysis and exploration.