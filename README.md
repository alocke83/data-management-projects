# data-management-projects
database management and agent data entry tools

1. The SQL query tool is the backend management script, it has functions for creating, editing, displaying, and backing up the database that the other tools rely upon.  It should be used first to create the database in the desired drive location.  Then the other tool codes must be updated with the database location in order to function.

2. The survey data tool is specific to a project at a company, it allows the usser to record true and false responses to five questions and then add verbatim comments from a customer, which are then sent to the database.  This tool uses a tkinter interface in order to make it easy for phone agents to use while they are working on other tasks.  It was originally implemented in a team of 14 and there were minimimal chances of simultaneous write requests to the database, and so no database handling solution is currently in use.

3. The spreadsheet export tool is designed to allow a manager to extract the data from the database in a CSV with some simple arithmetic done for analytics purposes so that it can be used by an analyst or manager to prepare slides for presentation with internal partners.  The tool does not currently create charts or prepare percentage figures of customer responses.
