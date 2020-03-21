# Learn logging module

### Intro
- example-basicconfig: use `logging.basicConfig`
- example-fileconfig: use `logging.config.fileConfig`
- example-dictconfig: use `logging.config.dictConfig`
- logger_manager: implementing a logging wrapper


### logging module
- **Loggers** expose the interface that application code directly uses.
- **Handlers** send the log records (created by loggers) to the appropriate destination.
- **Filters** provide a finer grained facility for determining which log records to output.
- **Formatters** specify the layout of log records in the final output.


### syslog
##### syslog file location in my System(Ubuntu)
- /var/log/syslog
- /var/log/messages

##### syslog.conf
- **general**:  /etc/syslog.conf
- **Ubuntu**: /etc/rsyslog.conf


### Reference
- [logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)
- [logging.config — Logging configuration](https://docs.python.org/3/library/logging.config.html)
- [logging.handlers — Logging handlers](https://docs.python.org/3/library/logging.handlers.html)
- [How can I add an empty directory to a Git repository?](http://stackoverflow.com/questions/115983/how-can-i-add-an-empty-directory-to-a-git-repository)
- [How to configure logging to syslog in python?](http://stackoverflow.com/questions/3968669/how-to-configure-logging-to-syslog-in-python)
- [Where is syslog.conf?](http://askubuntu.com/questions/42152/where-is-syslog-conf)
