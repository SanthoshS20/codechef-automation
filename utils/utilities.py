import logging,constants

class Utilities:

  def __init__(self, logger_name, level_name):
    self.logger_name = logger_name
    self.level_name = level_name

  def set_logger(self):
    logger = logging.getLogger(self.logger_name)
    logger.setLevel(self.level_name)
    format = logging.Formatter("%(asctime)s %(filename)s %(funcName)s:%(lineno)d  %(message)s")
    file_handler = logging.FileHandler(constants.LOGS_DIRECTORY + constants.LOG_FILENAME)
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)
    return logger