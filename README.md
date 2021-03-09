# data-management-projects
database management and agent data entry tools

1. The SQL query tool is intended as a way for agents to learn SQL without having to get access to the MS SQL studio.  It's aimed at expanding skillsets for agents without having to directly become involved in a time-sensitive project.

2. The database management tool is the backend control that runs in dirty IDLE without a fancy interface.  The script includes functions for making, editing, and managing an SQL database outside of expensive software like MS SQL Management Studio.  The data entry and spreadsheet export tools rely on this tool to create the database that they query.

3. The parking survey tool is specific to a project at a company, it allows the usser to record true and false responses to five questions and then add verbatim comments from a customer, which are then sent to the database.  This tool uses a tkinter interface in order to make it easy for phone agents to use while they are working on other tasks.  It was originally implemented in a team of 14 and there were minimimal chances of simultaneous write requests to the database, and so no database handling solution is currently in use.

4. The spreadsheet export tool is designed to allow a manager to extract the data from the database in a CSV with some simple arithmetic done for analytics purposes so that it can be used by an analyst or manager to prepare slides for presentation with internal partners.  The tool does not currently create charts or prepare percentage figures of customer responses.  The survey data tool was a first pass at this idea that I stepped away from to work on other projects, it follows very similar ideas to the completed version.
