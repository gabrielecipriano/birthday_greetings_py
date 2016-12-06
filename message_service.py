class MessageService:
    def __init__(self, message_formatter, message_sender):
        self._message_formatter = message_formatter
        self._message_sender = message_sender

    def send(self, employees):
        if employees is not None:
            for employee in employees:
                self._message_sender.send(self._message_formatter.format(employee), employee.contact)


class Message:
    def __init__(self, message_text, contact):
        self._message_text = self._message_text
        self._contact = contact


class TemplateMessageFormatter:
    def __init__(self, template):
        self._template = template

    def format(self, employee):
        return self._template.replace("::name::", employee.name)


class Email:
    def __init__(self, subject, email_text, email_from, email_to):
        self._email_from = email_from
        self._email_to = email_to
        self._subject = subject
        self._email_text = email_text

    def __eq__(self, other):
        return self._subject == other._subject \
               and self._email_text == other._email_text \
               and self._email_to == other._email_to and self._email_from == other._email_from


class EmailMessageSender:
    subject = "Happy Birthday!"

    def __init__(self, SMTPClient, company_email):
        self._smtp_client = SMTPClient
        self._company_email = company_email

    def send(self, message_text, contact):
        self._smtp_client.sendEmail(
            Email(self.subject, message_text, self._company_email, contact.email))