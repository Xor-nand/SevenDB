import imaplib
import email
from email.header import decode_header

# account credentials -will be to be extracted from file.-
def getcredentials(file):
    try:
        print("\nGrabbing credentials from File creds.txt")
        f = open(file, "r")
        listline = f.readlines()
        username = listline[0]
        password = listline[1]
        regmail = listline[2]
    except IOError:
        print("! File creds.txt does not exist, Insert credentials by hand:")
        username = input("username : ")
        password = input("password : ")
        regmail = input("Target email : ")
    return(username,password,regmail)
#check mail from (post erxtraction)
#extract body from email msg (needs specific email-code)\
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(1))
    else:
        return msg.get_payload(None,True)

def mailbackup(filename,body,emailcode):
    print ("\nbacking up mail no {} \n".format(emailcode))
    f = open(filename, 'w')
    f.write(body)
    print ("\nBackup done. outputmail.txt")
    f.close()
    return body

#useless
def search(key,value):
    result, data = imap.search(None, key, '"({})"'.format(value))
    print (type(data))
    print (type(data[0]))
    print (type(data[0][0]))
    print (data)
    print (data[0])
    print (data[0][0])
    #for i in data[0]:
    #    print(data[0][i],end=' ')
    #last_parsed from file
    last_parsed = 16
    datalist = data[0].decode()
    bitt = datalist.strip().split(' ')
    ##print(bitt)
    ##print(type(bitt))
    ##print(type(bitt[0]))
    ##bitte = int(bitt[0])
    ##print(type(bitte))
    for i in bitt:
        caca = int(i)
        if caca == last_parsed + 1:
            new_pars = caca
    new_pars = str(new_pars).encode()
    return new_pars

#load credentials from file cred.txt -email -passwd -mail address to search and parse
credfile = "creds.txt"
username, password, regmail = getcredentials(credfile)

#useroutput not needed
print ("\n>> Applying credentials : \nusername: {} \nselected mail: {}\n".format(username,regmail))

# create an IMAP4 class with SSL and auth, then select from INBOX  (default)
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
status, messages = imap.select("INBOX")

print ("====== DONE.\n")


#ciao = search('FROM','camerinipaolo31@gmail.com')
#final = bytes(str(ciao).encode())
#print(type(final))
#print(final)

#fetch all email data based on mail identifier (MOVE)
#result, data = imap.fetch(b'17','(RFC822)')
result, data = imap.fetch(search('FROM','camerinipaolo31@gmail.com'),'(RFC822)')

#raw data of email
raw = email.message_from_bytes(data[0][1])

body = raw.get_payload(0)
actual_body = body.get_payload(0)

mailbody = actual_body.__str__()

mmm = mailbackup("outputmail.txt",mailbody,"12")
