import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
);

type Props = {
    chartData : any;
}

const LineChart = ({chartData} : Props) => {
    return <Line data={chartData} options={{maintainAspectRatio : false, responsive : true}} />
}

export default LineChart;
