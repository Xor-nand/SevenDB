import imaplib
import email
from email.header import decode_header

# account credentials -will be to be extracted from file.-
username = "tcdigitalagency@gmail.com"
password = "ubctaollcmnrjbqo"

#extract body from email msg (needs specific email-code)
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(1))
    else:
        return msg.get_payload(None,True)

#useless
def search(key,value):
    result, data = imap.search(None, key, '"({})"'.format(value))
#    print (data)
#    print (result)
    return data

def extractbody(mailcode)

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate imap
imap.login(username, password)

#collect status and messages from INBOX  (default)
status, messages = imap.select("INBOX")



#fetch all email data based on mail identifier
result, data = imap.fetch(b'17','(RFC822)')

#Now data contains all mail data of number b"n"
# print(data)

#raw data of email
raw = email.message_from_bytes(data[0][1])


#now collect the body of the email in raw data
#actual_body = get_body(raw)
#print (actual_body)

#data = search("FROM",'camerinipaolo31@gmail.com')




#readraw = raw.__str__()

Pars = 'Report di Chiusura Giornata'

body = raw.get_payload(0)
actual_body = body.get_payload(0)

print (actual_body)

f = open('/home/xornand/Documents/outputmail.txt', 'w')
f.write(actual_body.__str__())
f.close()
