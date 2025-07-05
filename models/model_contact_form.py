import smtplib
from email.message import EmailMessage

class ContactFormSender:
    def __init__(self, form_data,
                 smtp_server='serwer2518763.home.pl',
                 smtp_port=587,
                 smtp_user='biuro@solarnedachy.eu',
                 smtp_password='solar8375001onboard'):
        # Dane SMTP
        self.smtp_server   = smtp_server
        self.smtp_port     = smtp_port
        self.smtp_user     = smtp_user
        self.smtp_password = smtp_password

        # Dane z formularza
        self.name    = form_data.get('name', '').strip()
        self.email   = form_data.get('email', '').strip()
        self.phone   = form_data.get('phone', '').strip()
        self.message = form_data.get('textarea', '').strip()

        # Wewnętrzne flagi walidacji
        self.name_valid    = self.valid_name(self.name)
        self.phone_valid   = self.valid_phone(self.phone)
        self.message_valid = len(self.message) >= 10

    def valid_name(self, name):
        return len(name) > 3

    def valid_phone(self, phone):
        return phone.isdigit()

    def is_valid(self):
        # Ogólna flaga poprawności
        return all([self.name_valid, self.phone_valid, self.message_valid])

    def error_name_message(self):
        # Lista komunikatów błędów
        errors = []
        if not self.name_valid:
            errors.append("Imię musi mieć więcej niż 3 znaki.")
        if not self.phone_valid:
            errors.append("Telefon musi składać się tylko z cyfr.")
        if not self.message_valid:
            errors.append("Wiadomość musi zawierać co najmniej 10 znaków.")
        return errors

    def send(self):
        if not self.is_valid():
            raise ValueError("Formularz jest niepoprawny, nie wysyłam maila")

        msg = EmailMessage()
        msg['From']    = self.email
        msg['To']      = self.smtp_user
        msg['Subject'] = f"Kontakt od {self.name} – tel. {self.phone} email. {self.email}"
        msg.set_content(self.message)

        if self.smtp_port == 465:
            smtp = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
        else:
            smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

        smtp.login(self.smtp_user, self.smtp_password)
        smtp.send_message(msg)
        smtp.quit()
