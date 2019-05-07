# Python-Interview-Questions
* Logger.info(msg) : This will log a message with level INFO on this logger.
* Logger.warning(msg) : This will log a message with level WARNING on this logger.
Logger.error(msg) : This will log a message with level ERROR on this logger.
Logger.critical(msg) : This will log a message with level CRITICAL on this logger.
Logger.log(lvl,msg) : This will Logs a message with integer level lvl on this logger.
Logger.exception(msg) : This will log a message with level ERROR on this logger.
Logger.setLevel(lvl) : This function sets the threshold of this logger to lvl. This means that all the messages below this level will be ignored.
Logger.addFilter(filt) : This adds a specific filter filt to the to this logger.
Logger.removeFilter(filt) : This removes a specific filter filt to the to this logger.
Logger.filter(record) : This method applies the logger’s filter to the record provided and returns True if record is to be processed. Else, it will return False.
Logger.addHandler(hdlr) : This adds a specific handler hdlr to the to this logger.
Logger.removeHandler(hdlr) : This removes a specific handler hdlr to the to this logger.
Logger.hasHandlers() : This checks if the logger has any handler configured or not.
