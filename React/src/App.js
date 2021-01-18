
 import "bulma";
import Trade from "./Trade";
import Landing from "./Landing";
import { BrowserRouter, Redirect, Route, Switch } from "react-router-dom";
import { useState } from "react";
import "./App.css"

function App() {
  const [Username, SetUsername] = useState("Jhon Doe");
  const [Stock, SetStock] = useState(" ");
  const [Logged, SetLoged] = useState(false);
  return (
    <BrowserRouter>
        <div className="App">
          <Switch>
            <Route path="/trade">
              <Protec 
                username={Username}
                Stock={Stock}
                log={Logged}
                SUN={SetUsername}
                SST={SetStock}
                SL={SetLoged}/>
            </Route>
            <Route path="/">
              <Landing
                username={Username}
                Stock={Stock}
                log={Logged}
                SUN={SetUsername}
                SST={SetStock}
                SL={SetLoged}
              />
            </Route>
          </Switch>
        </div>
    </BrowserRouter>
  );
}

const Protec = ({log,...props}) => {
  return (log) ? (<Trade {...props}/>) :(<Redirect to="/"/>) 
}

export default App;
