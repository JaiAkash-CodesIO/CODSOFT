 To-Do List Application (Python GUI)

A simple yet effective To-Do List application built using Python and Tkinter. This application allows users to manage their daily tasks by adding, deleting, and marking tasks as completed. Tasks are also saved locally, so they persist between 
Features
Add Tasks: Users can easily add tasks using the input field.
View Tasks: All tasks are displayed in a Listbox for easy access.
Mark as Complete: Users can mark tasks as completed, and the task will be visually updated.
Delete Tasks: Users can delete tasks from the list.
Persistent Storage: All tasks are saved to a JSON file, so they are available even after closing the application.

 Demo

Follow these instructions to get a copy of the project running on your local machine.

Prerequisites

You'll need Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/to-do-list-app.git
   ```

2. Navigate to the project directory:

     cd to-do-list-app

3. Install any necessary dependencies (Tkinter is built-in with Python, so no additional libraries are required).

4. Run the application:

   python to_do_list.py
 How to Use

1. Adding Tasks: Type a task into the input field and press the "Add Task" button to add it to the list.
2. Marking Tasks as Complete: Select a task from the list and click "Complete Task" to mark it as completed.
3. Deleting Tasks: Select a task from the list and click "Delete Task" to remove it from the list.
4. The tasks will be automatically saved and loaded from the `tasks.json` file upon exiting and reopening the application.

