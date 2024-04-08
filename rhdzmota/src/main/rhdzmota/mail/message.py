from dataclasses import dataclass
from email.message import EmailMessage

__all__ = [
    "Message"
]


@dataclass
class Message:
    subject: str
    content: str
    author: str
    content_type: str

    @classmethod
    def content_plain_text(
            cls,
            subject: str,
            content: str,
            author: str,
    ) -> 'Message':
        return cls(
            subject=subject,
            content=content,
            author=author,
            content_type="text/plain",
        )

    @classmethod
    def content_html(
            cls,
            subject: str,
            content: str,
            author: str,
    ) -> 'Message':
        return cls(
            subject=subject,
            content=content,
            author=author,
            content_type="text/html",
        )

    def to_email_message(self, *recipient: str) -> EmailMessage:
        message = EmailMessage()
        message["From"] = self.author
        message["To"] = ", ".join(recipient)
        message["Subject"] = self.subject
        message.set_content(self.content)
        message.set_type(self.content_type)
        return message
