# UBC_Salary_Scrape


Pretty dirty code but it works...

The code looks through the UBC CONSOLIDATED FINANCIAL STATEMENTS .pdf and creates a dataframe of "name", "salary" and "expenses".
The output is simply a histogram of the salaries.

## How to run
1) Download [UBC's financial statements](https://finance.ubc.ca/sites/finserv.ubc.ca/files/FY20_Financial_Information_Act_Report.pdf) as a .pdf
2) Change line 15 to the path of the file 


## Improvement ideas
1) Use a gender guessing model to look at spread of pay between gender
2) Keeping in mind the [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) I would also need to split by department. 
