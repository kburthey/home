#! python3
#sending an email

import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('gmail email', 'email password')
conn.sendmail('fromm_addr', 'to_addrs', 'Subject: ## \n\nMsg')
conn.quit()


'''
Gmail = smtp.gmail.com
Outlook.com/Hotmail.com = smtp-mail.outlook.com
Yahoo Mail = smtp.mail.yahoo.com
AT&T = smpt.mail.att.net (port 465)
Comcast = smtp.comcast.net
Verizon = smtp.verizon.net (port 465)


Full documentation at https://imapclient.readthedocs.org
http://www.magiksys.net/pyzmail
https://automatetheboringstuff.com/chapter16

'''
