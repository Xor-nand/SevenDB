import imaplib
import email
from email.header import decode_header

# account credentials -will be to be extracted from file.-
def getcredentials(file):
    f = open(file, "r")
    listline = f.readlines()
    f.close()
    username = listline[0]
    password = listline[1]
    regmail = listline[2]
    return username, password, regmail

#extract body from email msg (needs specific email-code)
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(1))
    else:
        return msg.get_payload(None,True)

def mailbackup(body,emailcode):
    print ("====== BACKUP MAIL NO {} IN FILE\n".format(emailcode))
    f = open('outputmail.txt', 'w')
    f.write(body)
    print ("====== BACKUP DONE. outputmail.txt")
    f.close()
    return body

#useless
def search(key,value):
    result, data = imap.search(None, key, '"({})"'.format(value))
#    print (data)
#    print (result)
    return data

#load credentials from file cred.txt -email -passwd -mail address to search and parse
credentials = "cred.txt"
username, password, regmail = getcredentials(credentials)

#useroutput not needed
print ("\n====== CREDENTIALS ======\n\n > username: {} > email cassa: {}".format(username,regmail))

# create an IMAP4 class with SSL and auth, then select from INBOX  (default)
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
status, messages = imap.select("INBOX")

print ("====== DONE.\n")

#fetch all email data based on mail identifier (MOVE)
result, data = imap.fetch(b'17','(RFC822)')

#raw data of email
raw = email.message_from_bytes(data[0][1])

body = raw.get_payload(0)
actual_body = body.get_payload(0)

mailbody = actual_body.__str__()

mmm = mailbackup(mailbody,"12")
