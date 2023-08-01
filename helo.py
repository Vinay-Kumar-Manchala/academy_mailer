#!/usr/bin/python3
# print("hi from ubuntu")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl



class SmtpMailer:
    @staticmethod
    def smtp_connector():
        try:
            # Create a secure SSL context
            context=ssl.create_default_context()
            print(context)
            mailServer = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
            print("mailserver")
            mailServer.login("optimusprime7675@gmail.com", "pxgmpjecnereptya")
            #mailServer = smtplib.SMTP("relay.nic.in", 25)
            # mailServer.login("prana.cpcb@gov.in", "Prana@987")
            return mailServer
        except Exception as e:
            print("exception in connector")
            print(str(e))

    @staticmethod
    def send_email_to_user(receiver_email_list, subject, content, cc_list=None):
        try:
            message = SmtpMailer.form_mime_multipart(receiver_email_list, cc_list, subject, content)
            SmtpMailer.send_mail_as_mime_message(message.as_string(), receiver_email_list)

        except Exception as e:
            print(str(e))
        return True

    @staticmethod
    def send_mail_as_mime_message(message, receiver_email_list):
        try:
            server_obj = SmtpMailer.smtp_connector()
            message1 = f"Academy rules ni patinchadi, time ipdu 7:00 PM, laptop close chesi PG ki pondi bois :) \n  \n Itlu, \n Python Academy."
            server_obj.sendmail(from_addr="optimusprime7675@gmail.com",
                                to_addrs=["vinaykumar.manchala@knowledgelens.com"],
                                msg=message)
            server_obj.quit()
        except Exception as e:
            print(str(e))

    @staticmethod
    def form_mime_multipart(receiver_email, cc_list, subject, body):
        try:
            message = MIMEMultipart()
            message["From"] = "Python Academy"
            message["To"] = ",".join(receiver_email)
            message["Subject"] = subject
            if cc_list not in [None, []]:
                message["Cc"] = ",".join(cc_list)
            message.attach(MIMEText(body, "plain"))
            return message
        except Exception as e:
            print(e)

all_mail = ["vinaykumar.manchala@knowledgelens.com", "chakri.nugala@knowledgelens.com", "shabarish.bhadrisetty@knowledgelens.com", "vamsikrishna.grandhi@knowledgelens.com", "harish.raju@knowledgelens.com", "gnana.prakash@knowledgelens.com"]

if True:
    SmtpMailer().send_email_to_user(all_mail, "Reminder Msg from Python Academy", f"Academy rules ni patinchadi, time ipdu 7:00 PM, laptop close chesi PG ki pondi bois :) \n\n Pandagow,\nItlu : Python Academy.")
