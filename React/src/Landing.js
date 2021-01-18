// import { Link } from "react-router-dom";
import Form from "./Components/Form.js";
import "./App.css";
import FrontBanner from "./Components/FrontBanner.js";

const Landing = (props) => {
  return (
    <>
      <FrontBanner />
      <Form {...props}/>
    </>
  );
};

export default Landing;
