import "./App.css";
import Trade from "./Trade";
import Landing from "./Landing";
import { BrowserRouter, Route, Switch } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Switch>
          <Route path="/trade" component={Trade} exact />
          <Route path="/" component={Landing} />
          <Route component={Error} />
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
