
import smtplib
import mimetypes
import email
import email.mime.application

def main():
    createMail()


def readFile(filename,fileType,msg):
    fp=open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype=fileType)
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    print 'finishedreading ' + fileType
    
def createMail():
    sender = 'jmiritk@gmail.com'
    receiver=str(raw_input('Pleaser Enter Receiver ')).lower().strip()
    bcc = 'mirit3012@gmail.com'
    password = 'Not My Real Password :-)'
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = 'CV for Developer Position - Mirit Kashti '
    msg['From'] = sender
    msg['To'] = receiver
    msg['BCC'] = bcc
    body = email.mime.Text.MIMEText("""This is an auto mail sent by written Python program. \n Hope you like it!  \n The code is in my GitHub Account - jmiritk. """)
    msg.attach(body)

    #read Word
    word_fname='C:\Users\Mirit\Desktop\Python\MiritKashti_07.01_English_Hebrew.docx'
    sub_type='docx'
    readFile(word_fname,sub_type,msg)

    #read PDF
    pdf_fname='C:\Users\Mirit\Desktop\Python\MiritKashti_07.01_English_Hebrew.pdf'
    sub_type='pdf'
    readFile(pdf_fname,sub_type,msg)
    sendMail(sender,receiver,password,msg)
    


def sendMail(sender,receiver,password,msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender,password)
    server.sendmail(sender,[receiver], msg.as_string())
    server.quit()
    print 'Successfully Sent!'
    

main()






