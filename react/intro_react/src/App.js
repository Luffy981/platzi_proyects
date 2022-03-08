import React from 'react';
import { AppUI } from './appUI'
import { TodoProvider } from './TodoContext'
// import luffy from './TodoCounter'
// import './App.css';

// const defaultTodos = [
//   { text: 'Ver One Piece', completed: true },
//   { text: 'Estudiar', completed: false },
//   { text: 'Hablar con la hermosa Shannel', completed: true },
//   { text: 'Aprender React', completed: false }
// ];


function App() {

  return (
    <TodoProvider>
      <AppUI />
    </TodoProvider>
  );
}

export default App;
