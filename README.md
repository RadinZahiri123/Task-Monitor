# Task Monitor 

#### Description:  

My project, "Task Monitor", is a web application I created on VS code, using python, html, CSS, and JavaScript. It's designed for a diverse user base, with a focus on students and busy adults, providing an accessible solution for organizing tasks and commitments. This application aims to relieve the challenge of remembering and coordinating multiple tasks, such as assignments, exams, meetings, and appointments, through a centralized Web App platform.  

The functionality of this program includes activity, input, storage, editing, and sorting. Users can enter tasks, events, and appointments with details like name and date, stored in a local database for easy access. When the user wishes to delete a task, they can simply click on the trash icon, and it will completely erase all the data related to that task from the database. Users can manage and modify tasks based on their ever-changing schedules, ensuring flexibility in task handling. Tasks can be organized based on time, status, or date, depending on which sorting option the user prefers. 

In total, this program contains eight files that contribute to the program. The python file, app.py, is the backend application file. This Flask app handles user registration, login, task management (adding, deleting, editing), and logout functionalities. It uses Flask's session management for user authentication, stores user data using passwords, and manages tasks in a list. The app includes routes for rendering HTML templates, processing form data, and redirecting users based on their actions.  

There are five html files that each handle their own specific purposes in the web application. Each use a linked stylesheet and script for styling and interactivity, and each file dynamically performs actions based on data passed from the Flask backend. Index.html displays the "homepage" which contains the task list, as well as elements for managing tasks such as sorting options, edit and delete functionalities, and an add task button. The add_task.html and edit_task.html share many similarities. Both pages are triggered from the index page, and they both have a form with input fields for task name and date, along with a submit button. The form action is set to post data back to the '/' route for processing. Additionally, there's a link to navigate back to the task list page. The last two html files, LoginPage.html, and Registration.html are also quite similar. They include a form with input fields like username and password, along with a submit button. Since these were the last two files I created, I used inline styling and scripting for the sake of simplicity.  

Last but not least, is the script.js file and the styles.css file that complete the front-end side of this program. They provide the functionality and the style of the user interface for this web application. The script handles the functionality of the program, ranging from sorting the tasks, to toggling task completion status. All around, it's designed to enhance user interaction and task organization within the application. The CSS file includes the style for the overall layout, taking care of the containers, lists, buttons, etc. It's main goal and purpose is to enhance the user interface and create a pleasant and appealing design. 

As a summary, this Task Monitor has achieved many goals. Firstly, it correctly and safely incorporates the use of a local database to save user information. Users create an account that generates a unique id via the registration page, in which they then accordingly use to login to the application. This task monitor has successfully created the ability for users to add, and view their tasks, including the name and date. It has also given users the ability to edit, mark as complete, and delete their tasks. Users can sort their added tasks by alphabetical order, completion status, or due date. If a user desires, they can trigger the dark mode setting by clicking on the top left button. All in all, the task monitor has achieved the goal of a helpful, functionating and interactive web application. 
