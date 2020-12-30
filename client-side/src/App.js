import './App.css';
import { BrowserRouter } from "react-router-dom";

import Menu from "./Components/Menu/Menu"

function App() {
  return (
    <BrowserRouter>
      <div className="App">
          <Menu />
      </div>
    </BrowserRouter>
  );
}

export default App;
