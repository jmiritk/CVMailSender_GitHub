
import smtplib
import email
import email.mime.application
import yaml


def main():
    receiver = getReceiverEmail()
    config = readConfig()
    msg = createMail(receiver, config)
    attachFile(config['word']['path'], config['word']['fname'], config['word']['ext'], msg)
    attachFile(config['pdf']['path'], config['pdf']['fname'], config['pdf']['ext'], msg)
    sendMail(config["mail_auth"]['email'], receiver, config["mail_auth"]['password'], msg)
    main()

def getReceiverEmail():
    return str(raw_input('Pleaser Enter Receiver ')).lower().strip()


def attachFile(filePath, filename, fileType, msg):
    with open(filePath, 'rb') as fp:
        att = email.mime.application.MIMEApplication(fp.read(), _subtype=fileType)
        fp.close()
        att.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(att)
        print 'finished reading' + fileType
        return msg

def readConfig():
    with open('C:/Users/Mirit/PycharmProjects/CvMailSender/config.yml', 'r') as f:
        config = yaml.load(f)
        return config

def createMail(receiver, config):
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = config["mail_content"]['subject']
    msg['From'] = config["mail_auth"]['email']
    msg['To'] = receiver
    msg['Bcc'] = config["mail_auth"]['bcc']
    body = email.mime.Text.MIMEText(config["mail_content"]['content'])
    msg.attach(body)
    print 'attached mail body '
    return msg

def sendMail(sender, receiver, password, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()
    print 'sent :-)'


main()






