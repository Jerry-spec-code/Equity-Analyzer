import React from 'react';
import LineChart from '../LineChart/LineChart';

type Props = {
  data : any; 
}

const Graph = ({data} : Props) => {

  if (Object.keys(data).length === 0) {
    return <> </>
  }

  const possibleGraphs = ["Closing", "Opening", "High", "Low", "AdjClose", "Volume"];

  const stockData = (key : string, yVars : any) => {
    return {
      labels: data["x-data"],
      datasets: [
        {
            label: key,
            data: yVars["y-data"],
            fill: false, 
            borderColor: "chartreuse",
            lineTension: 0.1 
        },
        {
            label: "20 Day Moving Average",
            data: yVars["20-day-average"],
            fill: false, 
            borderColor: "red",
            lineTension: 0.1 
        },
        {
            label: "50 Day Moving Average",
            data: yVars["50-day-average"],
            fill: false, 
            borderColor: "blue",
            lineTension: 0.1 
        },
      ]
    } 
  };

  return (
    <p>
      <LineChart chartData={stockData("Closing", data["Closing"])} />          
      {/* {possibleGraphs.map((key : string) => {
        return (
          <LineChart chartData={stockData(key, data[key])} />          
        )
      })} */}
    </p>
  )
}

export default Graph;
