from unittest import TestCase

from domain import Employee, Contact
from message_service import MessageService, TemplateMessageFormatter, EmailMessageSender, Email


class FakeMessageFormatter:
    def format(self, employee):
        return "Hello, sir!!"


class MessageSenderSpy:
    called = False

    def send(self, message_text, message_contact):
        self.called = True
        self.called_with = message_text
        self.message_contact = message_contact

    def wasNotCalled(self):
        return not self.called

    def wasCalledWith(self, message_text, contact):
        return self.called_with == message_text \
               and self.message_contact == contact

    def refresh(self):
        self.called = False
        self.called_with = None
        self.message_contact = None


class MessageServiceTest(TestCase):
    fake_message_formatter = FakeMessageFormatter()
    message_sender_spy = MessageSenderSpy()

    def setUp(self):
        self.message_service = MessageService(self.fake_message_formatter, self.message_sender_spy)

    def test_none_messages(self):
        self.message_service.send(None)

        self.assertTrue(self.message_sender_spy.wasNotCalled())

    def test_format_and_send(self):
        self.message_service.send([Employee("SURNAME", "NAME", Contact("contact@email.com"))])

        self.assertTrue(self.message_sender_spy.wasCalledWith("Hello, sir!!", Contact("contact@email.com")))

    def tearDown(self):
        self.message_sender_spy.refresh()


class TemplateMessageFormatterTest(TestCase):
    def setUp(self):
        self.message_formatter = TemplateMessageFormatter("Happy birthday, dear ::name::!")

    def test_format_correctly(self):
        formatted_message = self.message_formatter.format(Employee("Snow", "John", Contact("john@email.com")))

        self.assertEqual(formatted_message, "Happy birthday, dear John!")


class SMTPClientSpy:
    def sendEmail(self, email):
        self.sentEmail = email


class EmailMessageSenderTest(TestCase):
    smtp_client_spy = SMTPClientSpy()

    def setUp(self):
        self.email_message_sender = EmailMessageSender(self.smtp_client_spy, "human-resource@company.com")

    def test_send_a_message(self):
        self.email_message_sender.send("A message", Contact("contact@email.com"))

        self.assertEqual(self.smtp_client_spy.sentEmail,
                         Email("Happy Birthday!", "A message", "human-resource@company.com", "contact@email.com"))