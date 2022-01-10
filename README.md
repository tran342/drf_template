# README #

This README would normally document whatever steps are necessary to get your application up and running.


## Tips

### To install mysqlclient (on Mac local) ###

```
brew install openssl
export PATH=$PATH:/usr/local/mysql/bin
LDFLAGS="-L/usr/local/opt/openssl/lib" pipenv install
```

### To install mssql-django (on Mac local) ###

Install Install the Microsoft ODBC driver for SQL Server (macOS)
```
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15
```

Choose the correct version here `2.3.9_1`
```
LDFLAGS="-L/opt/homebrew/Cellar/unixodbc/2.3.9_1/lib" CPPFLAGS="-I/opt/homebrew/Cellar/unixodbc/2.3.9_1/include" pipenv install mssql-django
```
