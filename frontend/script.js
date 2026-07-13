const API_URL = `http://${window.location.hostname}:5000/tasks`;

async function loadTasks() {

    const response = await fetch(API_URL);

    const tasks = await response.json();

    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    tasks.forEach(task => {

        const li = document.createElement("li");

        li.innerHTML = `
            ${task.title}
            <button class="delete-btn" onclick="deleteTask(${task.id})">
                Delete
            </button>
        `;

        taskList.appendChild(li);

    });

}

async function addTask(){

    const input=document.getElementById("taskInput");

    const title=input.value.trim();

    if(title===""){

        alert("Please enter a task");

        return;
    }

    await fetch(API_URL,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            title:title
        })

    });

    input.value="";

    loadTasks();
}

async function deleteTask(id){

    await fetch(`${API_URL}/${id}`,{

        method:"DELETE"

    });

    loadTasks();

}

loadTasks();
