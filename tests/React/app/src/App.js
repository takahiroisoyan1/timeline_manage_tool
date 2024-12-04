import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';

function App() {

  const [tasks, setTasks] = useState([]);
  const [companyName, setCompanyName] = useState('');
  const [deadline, setDeadline] = useState('');
  const [status, setStatus] = useState('0');

  // タスクを取得する関数
  useEffect(() => {
    fetch('http://127.0.0.1:5000/tasks')  // バックエンドのエンドポイント
      .then(response => response.json())
      .then(data => setTasks(data))
      .catch(error => console.error('Error:', error));
  }, []);

  // タスクを追加する関数


  const handleSubmit = (e) => {
    e.preventDefault();

    const newTask = { company_name: companyName, deadline, status };
    fetch('http://127.0.0.1:5000/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newTask),
    })
      .then(response => response.json())
      .then(data => setTasks([...tasks, data]))
      .catch(error => console.error('Error:', error));

    setCompanyName('');
    setDeadline('');
  };


  return (
    <div className="App">
      <h1>就活タスク管理ツール</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          placeholder="企業名" 
          value={companyName} 
          onChange={(e) => setCompanyName(e.target.value)} 
        />
        <input 
          type="date" 
          value={deadline} 
          onChange={(e) => setDeadline(e.target.value)} 
        />
        <select 
          value={status} 
          onChange={(e) => setStatus(e.target.value)}
        >
          <option value="0">未着手</option>
          <option value="1">進行中</option>
          <option value="2">完了</option>
        </select>
        <button type="submit">タスクを追加</button>
      </form>
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
