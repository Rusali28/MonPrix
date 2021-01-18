import React from "react";
import { Redirect } from "react-router-dom";
import "../App.css";

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = { red: false };
    this.stocknames = ["AAPL", "BABA", "AMZN", "MSFT"];
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const id = event.target.name;
    console.log(this.props);
    if (id === "name") {
      this.props.SUN(event.target.value);
    } else {
      this.props.SST(event.target.value);
    }
  }

  handleSubmit(event) {
    event.preventDefault();
    this.props.SL(true);
    this.setState({ red: true });
  }

  render() {
    const { red } = this.state;

    if (red) {
      return <Redirect to="/trade" />;
    }
    return (
      <div className="Cen card" style={{ margin: "50px" }}>
        <form onSubmit={this.handleSubmit}>
          <h1 className="title">
            Hi,
            <input
              name="name"
              value={this.props.username}
              onChange={this.handleChange}
            />
          </h1>{" "}
          <br />
          <h2 className="subtitle">Look for a stock symbol to practice on</h2>
          <input
            name="stock"
            value={this.props.Stock}
            onChange={this.handleChange}
          />
          <input type="submit" value="Go" />
          <br /> <br />
          <h2 className="subtitle">Or, Choose some of the popular stocks</h2>
          <div className="flexcon">
          {this.stocknames.map((x) => {
            return (
              <a
              key={x}
              className="mar tag is-primary is-light is-medium"
              onClick={(e) => {
                this.props.SST(e.target.innerText);
              }}
              >
                {x}
              </a>
            );
          })}
          </div>
        </form>
        <br/>
        <h2 className="subtitle">Instructions</h2>
        <ul>
          <li>1. Choose the stock you want to invest in</li>
          <li>2. The Trading Bot helps you make a decision.</li>
          <li>
            3. You now learn by looking at where an AI bot traded money only by
            going through the charts.
          </li>
        </ul>
      </div>
    );
  }
}

export default Form;
