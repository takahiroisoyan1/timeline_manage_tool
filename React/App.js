import React, { useState, useEffect } from 'react';

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  useEffect(() => {
    fetch('/tasks')
      .then(response => response.json())
      .then(data => setTasks(data));
  }, []);

  const addTask = () => {
    fetch('/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: tasks.length + 1, name: newTask, status: 0 }),
    })
      .then(response => response.json())
      .then(task => setTasks([...tasks, task]));
  };

  return (
    <div>
      <h1>タスク管理</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.name}</li>
        ))}
      </ul>
      <input
        type="text"
        value={newTask}
        onChange={e => setNewTask(e.target.value)}
      />
      <button onClick={addTask}>タスク追加</button>
    </div>
  );
}

export default App;
