import { Link } from "react-router-dom";
import Form from "./Components/Form.js";
import Navbar from "./Components/Navbar.js";

const Landing = () => {
  return (
    <>
    <section className="Section">
      <div className="hero is-medium is-primary is-bold">
       <Navbar />
        <div class="hero-body ">
          <h1 className="title is-size-1">MonPrix</h1>
          <h3 className="subtitle ">Start trading now</h3>
        </div>
      </div>
    </section>
    
        <Form />
        
     
    </>
  );
};

export default Landing;
