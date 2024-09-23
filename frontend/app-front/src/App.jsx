import { useState } from 'react';
import './App.css';
// import './components/Form';

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Machine Learning MVP</h1>
      <div className="App">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </>
  )
}

export default App
