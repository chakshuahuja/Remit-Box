import re
import poplib
print "Connecting..."
import email
from email import parser
M = poplib.POP3_SSL('pop.gmail.com', 995)
print "Connected to pop.gmail.com"
M.getwelcome()
print
M.user("remitbox40@gmail.com")
M.pass_("123wasdw")
print "User chakshu authenticated."
numMessages = len(M.list()[1])
messages = [M.retr(i) for i in range(1, len(M.list()[1]) + 1)]
messages = ["\n".join(mssg[1]) for mssg in messages]

messages = [parser.Parser().parsestr(mssg) for mssg in messages]
for message in messages:
    subject = message['subject']
    email_from = message['From']
    email_to = message['To']
    b = email.message_from_string(str(message))
    if b.is_multipart():
        for payload in b.get_payload():
            # if payload.is_multipart(): ...
            body = payload.get_payload()
            break
    else:
        body = b.get_payload()
    print 'Subject:', subject, 'From:', email_from, 'To:', email_to, 'Body:', body.split('8870923027')[1]
M.quit()


