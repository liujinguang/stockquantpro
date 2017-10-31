#!/usr/bin/env python


"""
This library contains modules for logging system.

if use it, plase add 2 lines below:

import logging
from Comms.log import log

then add log where you want to add

log.debug(40 * '*')
log.info(40 * '*')
log.warn(40 * '*')
log.error(40 * '*')
log.critical(40 * '*')
log.exception(40 * '*')  # this is commenly use to log the exception call stack

"""

import logging
import logging.config
import os
import platform

if platform.system() == "Linux":
    log_path = '/var/quant'
else:
    log_path = 'd:\quant'


if not os.path.exists(log_path):
    print "Error: make sure {0} is exists and have 'w' permission! try these cmds:\
        \nsudo mkdir -p {0}\nsudo chmod -R a+w {0}".format(log_path)
    exit(1)

logging.config.fileConfig(log_path + os.sep +"logging.conf")
log = logging.getLogger("quant")




