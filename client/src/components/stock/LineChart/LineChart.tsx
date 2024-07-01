import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title, 
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title, 
);

type Props = {
    chartData : any;
    myTitle : string; 
    data : any;
}

const LineChart = ({chartData, myTitle, data} : Props) => {
  const options = {
      responsive: true,
      plugins: {
        title: {
            display: true,
            text: `${myTitle} Price Data (${data.ticker})`,
            padding: {
              top: 10,
              bottom: 10,
            },
            font: {
              size: 20,
            }
        },
        legend: {
          display: true,
        }, 
        tooltips: {
            mode: 'index',
            intersect: false
        },
        hover: {
            mode: 'index',
            intersect: false
        },
        scales: {
          xAxes: [{
            display: true,
            scaleLabel: {
              display: true,
            }
          }],
          yAxes: [{
            display: true,
            scaleLabel: {
              display: true,
              labelString: 'Prices',
            },
          }]
        }
      },
    };
    return <Line data={chartData} options={options}/>
}

export default LineChart;
