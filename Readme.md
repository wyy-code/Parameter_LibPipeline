# Parameter Library Pipeline

The pipeline generates a new Parameter table from the manuscript.

To accomplish the task of extracting information from the PDF document and generating a new table with updated columns and values, we can break down the process into several steps:

* Extract Table from PDF: Identify and extract the specific table ("Table 3: Non-iterative results on two monolingual datasets") from the PDF document.

* Parse Table Data: Convert the extracted table into a structured format that can be manipulated programmatically, such as a pandas DataFrame.

* Update the Table Structure: Add new columns for the "dv" metric in the appropriate positions in the table's header row.

* Extract "dv" Values: Based on the provided implementation details, extract the "dv" values for different models and datasets.

* Populate the Table with "dv" Values: Fill in the new "dv" columns with the extracted values for each corresponding model.

* Save the Updated Table to CSV: Finally, save the updated table to a CSV file for further use or analysis.
