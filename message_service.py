class MessageService:
    def __init__(self, message_formatter, message_sender):
        self.message_formatter = message_formatter
        self.message_sender = message_sender

    def send(self, employees):
        if employees is not None:
            for employee in employees:
                self.message_sender.send(self.message_formatter.format(employee), employee.contact)


class Message:
    def __init__(self, message_text, contact):
        self.message_text = self.message_text
        self.contact = contact


class TemplateMessageFormatter:
    def __init__(self, template):
        self.template = template

    def format(self, employee):
        return self.template.replace("::name::", employee.name)


class Email:
    def __init__(self, subject, email_text, email_from, email_to):
        self.email_from = email_from
        self.email_to = email_to
        self.subject = subject
        self.email_text = email_text

    def __eq__(self, other):
        return self.subject == other.subject \
               and self.email_text == other.email_text \
               and self.email_to == other.email_to and self.email_from == other.email_from


class EmailMessageSender:
    subject = "Happy Birthday!"

    def __init__(self, SMTPClient, company_email):
        self.smtp_client = SMTPClient
        self.company_email = company_email

    def send(self, message_text, contact):
        self.smtp_client.sendEmail(
            Email(self.subject, message_text, self.company_email, contact.email))