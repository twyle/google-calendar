# google-calendar
## Overview
A python library for working with the google calendar. Allows the developer to programatically perform the following tasks:

- Schedule an event
- Find all scheduled events
- Search for specific scheduled events
- Delete or update scheduled events
- Create calendars

## Getting started
Tou use this library, you will need a Google (GMail) Account and Google Credentials. Follow the instructions in this short [article](https://medium.com/@lyle-okoth/how-to-get-a-google-api-key-d3c38649eaae) to get an API key.

#### Installing the library
```sh
pip install oryks-google-calendar
```
#### Schedulin an event
```python
from google_calendar import GoogleCalendar

client_secret: str = 'client_secret.json'
google_calendar: GoogleCalendar = GoogleCalendar(secret_file=client_secret)
google_calendar.authenticate()

print(google_calendar.quick_add('Meeting with emmanuel at 10.00 am tommorrow.'))
```
