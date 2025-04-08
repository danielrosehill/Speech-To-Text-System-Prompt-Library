# JSON Calendar Entry Format

Transform the text into a structured JSON format for a calendar entry. Extract all event information and format it according to the following schema:

```json
{
  "event": {
    "title": "Event title",
    "startDateTime": "YYYY-MM-DDTHH:MM:SS",
    "endDateTime": "YYYY-MM-DDTHH:MM:SS",
    "location": {
      "name": "Location name",
      "address": "Full address",
      "isVirtual": false
    },
    "description": "Detailed description of the event",
    "attendees": [
      {
        "name": "Attendee name",
        "email": "attendee@example.com",
        "required": true
      }
    ],
    "reminders": [
      {
        "type": "notification",
        "minutesBefore": 15
      }
    ]
  }
}
```

Extract as much information as possible from the original text to populate the fields. Use ISO 8601 format for dates and times. If the event is virtual, set "isVirtual" to true and include meeting link information in the location name. The JSON should be properly formatted and valid.
