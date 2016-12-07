# cblawson.github.io

## Synopsis

This project fetches the fantasy football scores of every team from each week, and then displays a box plot chart of all ten teams.

The Python code is run each week, collecting the scores from ESPN using nested loops and the BeautifulSoup library.
Then, the quartiles for the box plot are calculated for each team using the numpy library.
The teams are sorted by median (highest to lowest), and then saved as a txt file.

The data from the text file is then manually copied and pasted into the html file.
The NVD3 javascript library is used to display the box plot.

## Planned Features

In order to demonstrate my proficiency in R, the numpy code will likely be replaced by an R program that calculates and formats the data.
Also, the ability to view previous weeks' box plots would be a nice upgrade for those wanting to track their fantasy team's progress.
