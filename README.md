# Simple To-Do List  
**Description**  
This is a simple to-do list application where users can add, view, and delete tasks. It is designed to run in the terminal, providing a simple interface to manage daily tasks.  

**Features**  
- Add tasks to the to-do list.  
- View all tasks in the list.  
- Delete tasks by selecting their number.  
- Exit the application safely.  

**Requirements**  
- Python 3.x installed on your system.  

**How to Run**  
1. Clone or download the project to your local machine.  
2. Open the project folder in your terminal or preferred IDE.  
3. Run the Python script with the following command:  
   ```bash
   python todo_list.py
   ```  
4. Follow the instructions displayed on the terminal to:
   - Add tasks.
   - View tasks.
   - Delete tasks.
   - Exit the application.

**Code Explanation**  
- **display_menu()**: Displays the main menu options.  
- **main()**: The core function that manages the to-do list. It allows adding, viewing, and deleting tasks based on user input.  

**Example Usage**  
```
--- TO-DO LIST ---
1. Add a Task
2. View Tasks
3. Delete a Task
4. Exit
Choose an option: 1
Enter a new task: Buy groceries
'Buy groceries' has been added to your to-do list.

--- TO-DO LIST ---
1. Add a Task
2. View Tasks
3. Delete a Task
4. Exit
Choose an option: 2
Your Tasks:
1. Buy groceries
```

**Future Improvements**  
- Save tasks to a file for persistence between runs.  
- Add the ability to mark tasks as completed.  
- Implement a search feature to quickly find tasks.  

**License**  
This project is licensed under the MIT License.
