import { Link } from "react-router-dom";

const Landing = () => {
  return (
    <div>
      <h1>Landing</h1>
      <Link to="/trade">Start now</Link>
    </div>
  );
};

export default Landing;