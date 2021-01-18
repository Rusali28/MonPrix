import { Link } from "react-router-dom";
import "../node_modules/react-vis/dist/style.css";
import {
  XYPlot,
  LineSeries,
  VerticalGridLines,
  HorizontalGridLines,
  XAxis,
  YAxis,
  MarkSeries,
} from "react-vis";
import { useHistory } from "react-router-dom";
import { useState, useEffect } from "react";
import FrontBanner from "./Components/FrontBanner";

const Trade = (props) => {
  let h = useHistory();
  const [Data, setData] = useState({
    res_data: 0,
    buy: 0,
    sell: 0,
  });

  const [st, setst] = useState(props.Stock);

  // useEffect(() => {
  //   fetch("http://localhost:3000/api")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setText(data.time);
  //     });
  // },[]);

  useEffect(() => {
    fetch("http://localhost:3000/api/checkstock", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ Stock: st }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.fail === 0) {
          alert("we can't find this stock try again");
          h.push("/");
        }
        setData(data);
      });
  }, []);

  return (
    <>
      <FrontBanner />
      <div className="Cen card">
        <h1 className="title">Trade</h1>
        <strong>{st}</strong>

        <br />
        <h3 className="tag is-warning is-large">Bot </h3>
        <p>Profit: {(Data.risk - 1) * 100}% </p>
        <div className="button">
          <Link to="/">Reset</Link>
        </div>
        <div className="coloumns">
          <div className="coloumn mar">
          <XYPlot height={300} width={1200}>
            <VerticalGridLines />
            <HorizontalGridLines />
            <XAxis />
            <YAxis />
            <LineSeries data={Data.res_data} />
            <MarkSeries className="mark-series-example" data={Data.buy} color= "#4bdb71" />
            <MarkSeries className="mark-series-example" data={Data.sell} color="#ed425c" />
          </XYPlot>
          </div>
        </div>
        <div className="coloumns">
          <div className=" mar button  is-success coloumn">Buy</div>
          <div className="mar button is-danger is-coloumn">Sell</div>
          <h6 className="is-primary">Bot purchased and sold</h6>
        </div>
      </div>
    </>
  );
};

export default Trade;
