import logging


app_logger = logging.getLogger(__name__)
app_logger.setLevel(logging.INFO)

log_handler = logging.StreamHandler()
log_formatter = logging.Formatter("%(levelname)s [%(filename)s:%(lineno)d] %(message)s")
log_handler.setFormatter(log_formatter)

# add handler to logger
app_logger.addHandler(log_handler)
