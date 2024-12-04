import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';

function App() {

  const [tasks, setTasks] = useState([]);

  // タスクを取得する関数
  useEffect(() => {
    fetch('http://127.0.0.1:5000/tasks')  // バックエンドのエンドポイント
      .then(response => response.json())
      .then(data => setTasks(data))
      .catch(error => console.error('Error:', error));
  }, []);

  
  return (
    <div className="App">
      <h1>就活タスク管理ツール</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.task_id}>
            <strong>企業名:</strong> {task.company_name} | 
            <strong> 締切日:</strong> {task.deadline} | 
            <strong> 状態:</strong> {task.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
