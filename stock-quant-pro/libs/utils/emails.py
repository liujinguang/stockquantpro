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
import mimetypes
import smtplib


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

if __name__ == '__main__':
    pass