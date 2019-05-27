# LogsAnalysis

The Logs Analysis use SQL queries to analyze the log data, and print out the answers to some questions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Getting started with vagrant
1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
2. Download and install [Virtual Box](https://www.virtualbox.org/wiki/Downloads).
3. Clone [Vagrant configuration](https://github.com/udacity/fullstack-nanodegree-vm).
4. Clone the content of this repository to your shared vagrant folder
5. Download database [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and move it to your shared vagrant folder.
6. Start your console from the vagrant folder
7. Run vagrant: ```$ vagrant up ```
8. Login to vagrant on the virtual machine: ```$ vagrant ssh```
9. Navigate to the shared folder on the virtual machine: ```$ cd /vagrant```
10. Start SQL Server and connect database named news within file newsdata.sql ```$ psql -d news -f newsdata.sql```
11. Launch application: ```$ python project.py```
12. Open file result.txt to view the query results 


