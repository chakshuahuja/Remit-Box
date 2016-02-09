import poplib
from BeautifulSoup import BeautifulSoup as bs
import re

class UnreadEmailReader(object):
    def __init__(self,username=None, password=None):
        self.mail_box = poplib.POP3_SSL('pop.gmail.com',995)
        self.mail_box.user(username)
        self.mail_box.pass_(password)
        print 'Authenticated...'
        self.numMessages = len(self.mail_box.list()[1])
        self.prettify()

    @staticmethod
    def sexydump(response):
        from_val = None
        body_val = None
        for values in response:
            #print values
            from_obj = re.search('From:',values)
            body_obj = re.search('"ltr">(.*?)</',values)
            if from_obj is not None:
                from_val = re.search('<(\S+)>',values).group(1)
            #    print values
            if body_obj is not None:
                body_val = body_obj.group(1)
            #    print values
        return (from_val,body_val)

    def prettify(self):
        for email_index in range(self.numMessages):
            sender,body = UnreadEmailReader.sexydump(self.mail_box.retr(email_index+1)[1])
            print sender +':'+ body

    def __del__(self):
        self.mail_box.quit()
        print 'Quiting mailbox'

if __name__ == '__main__':
    x = UnreadEmailReader(username='remitbox40@gmail.com',password='123wasdw')

