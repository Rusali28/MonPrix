import "./App.css";
import "bulma";
import Trade from "./Trade";
import Landing from "./Landing";
import { BrowserRouter, Route, Switch } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Switch>
          <Route path="/trade">
            <Trade />
          </Route>
          <Route path="/">
            <Landing />
          </Route>
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
