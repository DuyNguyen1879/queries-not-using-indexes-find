
#### queries-not-using-indexes-find
These python and bash scripts are useful to find missing indexes(slow queries) in a automated way.  

- Assumed python3 is already installed. 
- Assumed Linux, Apache, MySQL is already working perfectly. 
- The application may have written in any programming langauage(PHP, Python, node-js, vue-js etc.). Only pre-condition is- it's database should be mysql
- Assumed that you have already enabled the slow-query and general-query log in the mysql. If not then enable these queries in the local machine(not on the production):
- mysql conf file localtion: /etc/mysql/my.cnf
- `sudo nano /etc/mysql/my.cnf`

- append the following content to my.cnf file (Below the [mysqld] section)

`slow_query_log = 1` <br>
`slow_query_log_file = /var/log/mysql/localhost-slow.log
long_query_time = 0
log_queries_not_using_indexes
general_log_file        = /var/log/mysql/mysql.log
general_log             = 1`

// restart the mysql:
sudo service mysql restart

// go to required script file locations, from terminal
cd queries-not-using-indexes-find

// change permission of localhost-slow.log, mysql.log file
sudo chmod -v 777 /var/log/mysql/localhost-slow.log /var/log/mysql/mysql.log 

// empty the file localhost-slow.log, mysql.log
> /var/log/mysql/mysql.log && > /var/log/mysql/localhost-slow.log && echo "clear-all-db-logs"

// load your web application (eg http://local.myapplication.com) from browser(or postman). 
// do login.
// do all kind of oprations in your appliation(like all button clicks, form-submission, file-upload, all pages reloads, all api-calls etc.) so that all kind of possible queries gets run on the database and logged into localhost-slow.log (Since long_query_time = 0).  

// run the following command from the terminal
python3 generateMySqlProfilerScript.py
// it will take /var/log/mysql/localhost-slow.log as input. 
// It will extract USE, SELECT, UPDATE, DELETE, INSERT, REPLACE statements.
// It will prepends EXPLAIN with the query and will output explain-query.txt

// run the following command from the terminal
mysql -vvv -hlocalhost -uadmin -p12345678 mydatabasename < explain-query.txt >  explain-output.txt
// it will take explain-query.txt as input sql file and will output explain-output.txt with explain statements
// here admin is the mysql username
// 12345678 is the mysql password

// run the following command from the terminal
python3 indexes-mismatching.py  > final-output.txt
// it will take explain-output.txt as input , will find 'NULL condition true' and 'Not using all keys' statements and will output final-output.txt file.


