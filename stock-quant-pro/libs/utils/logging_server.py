#!/usr/bin/env python

# from logging.handlers import RotatingFileHandler

import cPickle
import logging.config
import socket
import struct
import traceback
import platform
import os

if __name__ == "__main__":
    if platform.system() == "Linux":
        log_path = '/var/quant'
    else:
        log_path = 'd:\quant'    
    logging.config.fileConfig(log_path + os.sep + "logging_server.conf")
    log = logging.getLogger()
    
    host = ''
    port = 12345
    
    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    so.bind((host, port))
    
    while 1:
        try:
            msg = so.recv(8192)
            offset = struct.calcsize(">L")
            slen = struct.unpack(">L", msg[0:offset])[0]
#             print slen, len(msg)
            record = logging.makeLogRecord(cPickle.loads(msg[offset:]))
            log.handle(record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()
