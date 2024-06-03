
function sortTasks(criteria) {
    var taskList = document.querySelector('ul'); // get the task list element
    var tasks = taskList.querySelectorAll('li'); // get all task items
    tasks = Array.from(tasks); // convert NodeList to Array for easier manipulation

    tasks.sort(function(a, b) {
        var taskA, taskB;
        switch(criteria) {
            case 'name':
                taskA = a.textContent.trim().split(' - ')[0];
                taskB = b.textContent.trim().split(' - ')[0];
                return taskA.localeCompare(taskB); // sort by name
            case 'date':
                taskA = new Date(a.textContent.trim().split(' - ')[1]);
                taskB = new Date(b.textContent.trim().split(' - ')[1]);
                return taskA - taskB; // sort by date
            case 'status':
                taskA = a.classList.contains('completed-task');
                taskB = b.classList.contains('completed-task');
                return taskA && !taskB ? 1 : taskB && !taskA ? -1 : 0; // sort by status (completed tasks first)
        }
    });

    // clear the task list
    taskList.innerHTML = '';

    // append sorted tasks to the task list
    tasks.forEach(function(task) {
        taskList.appendChild(task);
    });
}

// function to toggle task completion status
function toggleCompletion(taskId) {
    var task = document.getElementById('task-' + taskId);
    task.classList.toggle('completed-task');
}

// function to handle drag start event
function dragStart(event) {
    event.dataTransfer.setData("text/plain", event.target.id);
}

// function to handle drag over event
function dragOver(event) {
    event.preventDefault();
}

// function to handle drop event
function drop(event) {
    event.preventDefault();
    const taskId = event.dataTransfer.getData("text/plain");
    const task = document.getElementById(taskId);
    const targetTaskId = event.target.closest('li').id;
    const targetTask = document.getElementById(targetTaskId);
    if (task && targetTask) {
        const taskList = document.querySelector('ul');
        taskList.insertBefore(task, targetTask.nextSibling);
    }
}

// function for dark mode
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', body.classList.contains('dark-mode') ? 'on' : 'off');
}

// Check if dark mode was enabled previously and apply it on page load
document.addEventListener('DOMContentLoaded', () => {
    const darkModeState = localStorage.getItem('darkMode');
    if (darkModeState === 'on') {
        toggleDarkMode();
    }
});   
