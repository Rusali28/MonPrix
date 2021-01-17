import { Link } from "react-router-dom";

const Landing = () => {
  return (
    <div className="hero is-primary">
      <h1 className="title">Mon Prix</h1>
      
      <Link to="/trade">Start now</Link>
    </div>
  );
};

export default Landing;