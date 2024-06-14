from imap_tools import MailBox

def get_msg(email_name: str, email_password: str) -> str:
    email_url = 'imap.rambler.ru'

    with MailBox(email_url).login(email_name, email_password, 'INBOX') as mailbox:
        for msg in mailbox.fetch(limit=1, reverse=True):
            text = msg.text
            html = msg.html
            return text or html or ''

def main():
    email_name = 'x'
    email_password = 'x'

    print(get_msg(email_name, email_password))


if __name__ == '__main__':
    main()
