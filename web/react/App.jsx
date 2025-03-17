import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Recommand from './components/pan_recommand.js';
function App() {
  return (
    <div className="App">
	<Routes>
          <Route path="/" element={<Recommand/>}/>
	</Routes>
    </div>
  );
}

export default App;
