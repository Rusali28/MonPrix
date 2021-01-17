import { Link } from "react-router-dom";
import "../node_modules/react-vis/dist/style.css";
import {
  XYPlot,
  LineSeries,
  VerticalGridLines,
  HorizontalGridLines,
  XAxis,
  YAxis
} 
from "react-vis";
import { useState, useEffect } from "react";

const Trade = () => {
  const [Data, setData] = useState([
    { x: 0, y: 8 },
    { x: 1, y: 5 },
    { x: 2, y: 4 },
    { x: 3, y: 9 },
    { x: 4, y: 1 },
    { x: 5, y: 7 },
    { x: 6, y: 6 },
    { x: 7, y: 3 },
    { x: 8, y: 2 },
    { x: 9, y: 0 },
  ]);

  useEffect(() => {
    fetch("/time")
      .then((res) => res.json())
      .then((data) => {
        setData(data.time);
      });
  }, []);

  return (
    <div>
      <h1>Trade</h1>
      <Link to="/">Reset</Link>
      <XYPlot height={300} width={300}>
        <VerticalGridLines />
        <HorizontalGridLines />
        <XAxis />
        <YAxis />
        <LineSeries data={Data} />
      </XYPlot>
    </div>
  );
};

export default Trade;
