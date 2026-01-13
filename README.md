"Notify App – Smart Notification & Alert System"
--> Overview
Notify App is a Python-based background notification system that monitors incoming notifications (such as emails or alerts from different platforms) and forwards only important messages to Telegram based on predefined keywords.
The goal of this app is to serve as a central notification hub, ensuring you never miss critical updates, such as job offers, projects, deals, or salary-related messages.

--> Key Features
1) Reads incoming emails using IMAP
2) Filters messages based on custom keywords (e.g. job, project, salary, deal)
3) Ignores irrelevant notifications automatically
4) Sends matched alerts instantly to Telegram
5) Runs continuously as a background worker
6) Cloud-deployable (PythonAnywhere, Railway, Render, etc.) 

--> How It Works (Concept)
A) The app connects to your email inbox using IMAP
B) It fetches new/unread messages
C) The email subject/body is scanned for predefined keywords
D) If a keyword is found:
    The notification is forwarded to Telegram
E) If no keyword is found:
    The message is ignored
F) The process repeats at a fixed interval (e.g. every 60 seconds)

--> Technologies Used
I) Python 3
II) imaplib & email (built-in libraries)
III) requests (for Telegram Bot API)
IV) Telegram Bot API
V) Cloud platforms (PythonAnywhere / Railway / Render)

--> Environment Variables
For security reasons, sensitive data is stored using environment variables:
  EMAIL_USER	---->  Email address used for monitoring
  EMAIL_PASS ----> 	Email App Password
  TELEGRAM_TOKEN ---->	Telegram Bot Token
  TELEGRAM_CHAT_ID ---->	Telegram Chat ID
  
--> Use Cases
i) Job and freelance opportunity alerts
ii) Business deal or client notifications
iii) Salary, wage, or payment updates
iv) Centralized monitoring of important messages

--> Future Improvements
a) Support for WhatsApp / Instagram notifications via mobile forwarders
b) Duplicate alert prevention
c) Dashboard for keyword management
d) Multi-platform notification support
