
import smtplib
import mimetypes
import email
import email.mime.application

def main():
    createMail()


def readFile(filePath,filename,fileType,msg):
    fp=open(filePath,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype=fileType)
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)
    print 'finishedreading ' + fileType
    return msg
    
def createMail():
    sender = 'jmiritk@gmail.com'
    receiver=str(raw_input('Pleaser Enter Receiver ')).lower().strip()
    bcc = 'jmiritk@gmail.com'
    #change pwd!!!!
    password = 'Not my real password'
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = 'CV for Developer Position - Mirit Kashti '
    msg['From'] = sender
    msg['To'] = receiver
    msg['Bcc'] = bcc
    body = email.mime.Text.MIMEText("""This mail was sent to you by a Python program I wrote. \n\nHope you like it!  \n\nThe code is in my GitHub Account - jmiritk\n\n Many Thanks,  \n\n Mirit""")
    msg.attach(body)
    print 'attached mail body ' 
  
    #read Word
    word_fpath='C:\Users\Mirit\Desktop\Python\MiritKashti_07.01_English_Hebrew.docx'
    word_fname = 'MiritKashti_07.01_English_Hebrew.docx'
    sub_type='docx'
    msg = readFile(word_fpath,word_fname,sub_type,msg)

    #read PDF
    pdf_fpath='C:\Users\Mirit\Desktop\Python\MiritKashti_07.01_English_Hebrew.pdf'
    pdf_fname = 'MiritKashti_07.01_English_Hebrew.pdf'
    sub_type='pdf'
    readFile(pdf_fpath,pdf_fname,sub_type,msg)
    sendMail(sender,receiver,password,msg)
    


def sendMail(sender,receiver,password,msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender,password)
    server.sendmail(sender,[receiver], msg.as_string())
    server.quit()
    print 'sent :-)'
    















main()






