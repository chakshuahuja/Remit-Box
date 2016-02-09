import sendgrid

sg = sendgrid.SendGridClient('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')

message = sendgrid.Mail()
message.add_to('Chakshu <test.chakshu@gmail.com>')
message.set_subject('Testing')
message.set_html('Hi')
message.set_text('Hello')
message.set_from('ahua.chaks <ahuja.chaks@gmail.com>')
status, msg = sg.send(message)
