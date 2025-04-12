let todos = [
  { name: "Buy milk", completed: false },
  { name: "Go to the gym", completed: true },
  { name: "Read a book", completed: false },
  { name: "Write code", completed: true },
  { name: "Walk the dog", completed: false },
  {
    name:
      "Morbi pulvinar ullamcorper tortor, quis cursus quam.",
    completed: false,
  },
];

const addTodoForm = document.getElementById("add-todo-form");
const list = document.getElementById("todo-list");
const countSpan = document.getElementById("count");
const clearButton = document.getElementById("todos-clear");
const clearAllButton = document.getElementById("todos-clear");


function render() {
  list.innerHTML = "";

  todos.forEach((todo, index) => {
    const li = document.createElement("li");
    li.className = "todo__container";
    if (todo.completed) {
      li.classList.add("todo__container--completed");
    }
    li.innerHTML = `
      <div class="todo-element todo-name">${todo.name}</div>
      <button class="todo-element todo-button move-up" data-index="${index}">↑</button>
      <button class="todo-element todo-button move-down" data-index="${index}">↓</button>
      <button class="todo-element todo-button complete-btn" data-index="${index}">
        ${todo.completed ? "Revert" : "Done"}
      </button>
      <button class="todo-element todo-button remove-btn" data-index="${index}">Remove</button>`;

    list.appendChild(li);
  });

  updateCount();
}

function updateCount() {
  const remaining = todos.filter((t) => !t.completed).length;
  countSpan.textContent = remaining;
}

addTodoForm.addEventListener("submit", function (event) {
  event.preventDefault();
  const input = addTodoForm.querySelector('input[name="todo-name"]');
  const taskName = input.value.trim();
  if (taskName === "") return;

  todos.push({
    name: taskName,
    completed: false,
  });

  input.value = "";
  render();
});
  
clearAllButton.addEventListener("click", function (event) {
  event.preventDefault();
  todos = [];
  render();
});




render();