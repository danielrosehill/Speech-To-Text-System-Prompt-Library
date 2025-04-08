# JSON To-Do List Format

Transform the text into a structured JSON format for a to-do list. Extract all tasks and related information and format them according to the following schema:

```json
{
  "todoList": {
    "title": "Title of the list",
    "createdDate": "YYYY-MM-DD",
    "tasks": [
      {
        "id": 1,
        "description": "Task description",
        "priority": "high|medium|low",
        "dueDate": "YYYY-MM-DD",
        "completed": false,
        "notes": "Additional notes or context"
      }
    ]
  }
}
```

Ensure all task descriptions are clear and actionable. Infer priority levels from context when possible. Include due dates if mentioned in the original text. Set all tasks as "completed": false by default. The JSON should be properly formatted and valid.
