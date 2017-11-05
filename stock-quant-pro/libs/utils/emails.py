#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on Oct 30, 2017

@author: hadoop
'''

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import utils, encoders

from drawing.drawing_utils import draw_stock_with_candlestick_macd
from utils.log import log
from datetime import datetime

import mimetypes
import smtplib
import platform
import os

def get_attachment(filename):
    '''
    build attachment object
    '''
    fd = open(filename, 'rb')

    mimetype, mimeencoding = mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype = 'application/octet-stream'

    maintype, subtype = mimetype.split('/')

    if maintype == 'text':
        retval = MIMEText(fd.read(), _subtype=subtype)
    else:
        retval = MIMEBase(maintype, subtype)
        retval.set_payload(fd.read())
        encoders.encode_base64(retval)

    retval.add_header('Content-Disposition', 'attachment',
                      filename=filename.split('/')[-1])
    fd.close()

    return retval

def send_email(to_addr, subject, email_body, file_list=None):
    '''
    send the email to users
    '''

    html_start = '<font face="Courier New, Courier, monospace"><pre>'
    html_end = '</pre></font>'

    foot_msg = """
-------------------------------------------------------------------------<br/>
*** This message was auto-generated                                   ***<br/>
*** If you believe it was sent incorrectly, please e-mail             ***<br/>
*** Jinguang Liu (mailto:jliu@infinera.com)                           ***<br/>"""

    smtp_server = 'bruins.infinera.com'
    from_addr = 'jliu@infinera.com'


    msg = MIMEMultipart()

    msg['To'] = to_addr
    msg['From'] = 'Jinguang Liu <jliu@infinera.com>'
    msg['Subject'] = subject
    msg['Date'] = utils.formatdate(localtime=1)
    msg['Message-ID'] = utils.make_msgid()

    message = html_start + email_body + foot_msg + html_end

    body = MIMEText(message, _subtype='html', _charset='utf-8')
    msg.attach(body)

#     files = ['mime_get_basic.py']
    if file_list is not None:
        for filename in file_list:
            msg.attach(get_attachment(filename))

    s = smtplib.SMTP(smtp_server)
#     s.set_debuglevel(1)
    s.sendmail(from_addr, to_addr, msg.as_string())

def send_alert_email(entity, subject, body, k_type):
    '''
    Send email to alert
    '''
    code_id = entity.codeId
    log.info("send alert email: " + code_id + " " + subject)
    file_lst = []
    
    if platform.system() == "Linux":
        rdir = '/home/hadoop/quant/' + datetime.now().strftime("%Y-%m-%d")
    else:
        rdir = 'd:\\quant\\' + datetime.now().strftime("%Y-%m-%d")
        
    if not os.path.exists(rdir):
        os.mkdir(rdir)
    
    fname = rdir + os.sep + k_type + "-" + code_id + "-" + \
            entity.name.decode('utf-8').encode('gbk') + "-" + \
            datetime.now().strftime("%Y-%m-%d-%H-%M-") + ".png"
#     if platform.system() == "Linux":
#         fhead = rdir + os.sep + k_type + "-" + code_id + "-" + entity.name.decode('utf-8').encode('gbk') + "-" + datetime.now().strftime("%Y-%m-%d-%H-%M-")
#     else:
#         fhead = rdir + os.sep + code_id + "-" + datetime.now().strftime("%Y-%m-%d-%H-%M-")
    
#     fname = fhead + "-all-periods.png"
    if draw_stock_with_candlestick_macd(code_id, ("W", "D", "30", "15"), fname):
        file_lst.append(fname)
    
#     send_email("jliu@infinera.com", code_id + " " + subject, body)  

if __name__ == '__main__':
    pass