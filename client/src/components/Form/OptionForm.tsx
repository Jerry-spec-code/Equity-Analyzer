import React, { useState, useEffect } from 'react'
import { TextField } from '@mui/material'
import OptionButton from "../Button/OptionButton"
import ROUTES from '../../config/api';

type Props = {
    show : boolean;
    setErrorMsg : (args : string) => void;
};

const OptionForm = ({show, setErrorMsg} : Props) => {
    
    const [clicked, setClicked] = useState(false);
    const [data, setData] = useState({});

    const [optionPrice, setOptionPrice] = useState("100.0");
    const [strikePrice, setStrikePrice] = useState("100.0");
    const [interestRate, setInterestRate] = useState("0.05"); // Risk-free rate (5%)
    const [volatility, setVolatility] = useState("0.20"); // Volatility of the underlying (20%)
    const [expires, setExpires] = useState("1.0");    // One year until expiry

    const defaultWidth = "20%";

    useEffect(() => {
        if (clicked) {
            setClicked(false);
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json"},
                body: JSON.stringify({
                    optionPrice: optionPrice, 
                    strikePrice: strikePrice, 
                    interestRate: interestRate,
                    volatility: volatility,
                    expires: expires,
                })
            }
            const fetchData = async () => {
                await fetch(ROUTES.getOptionsData, requestOptions)
                    .then((res) => res.json())
                    .then((data) => {
                        console.log(data);
                        if (data.status === "success") {
                            setData(data);
                            setErrorMsg("");
                        }
                        else {
                            setErrorMsg(data.status);
                            setData({});
                        }
                    })
            }
            fetchData();
        }
    }, [clicked]);

    const update = (value : string, setState : (args : string) => void) => {
        setState(value);
    }

    if (!show) {
        return <> </>
    }

    return (
    <div>
      <br />
      <TextField variant="outlined" label="Option price" size="small" sx={{ width: defaultWidth }} onChange={(e) => update(e.target.value, setStrikePrice)}></TextField>
      <TextField variant="outlined" label="Strike price" size="small" sx={{ width: defaultWidth, ml : "1%" }} onChange={(e) => update(e.target.value, setStrikePrice)}></TextField>
      <TextField variant="outlined" label="Risk-free interest rate" size="small" sx={{ width: defaultWidth, ml : "1%" }} onChange={(e) => update(e.target.value, setStrikePrice)}></TextField>
      <br />
      <br />
      <TextField variant="outlined" label="Volatility" size="small" sx={{ width: defaultWidth }} onChange={(e) => update(e.target.value, setStrikePrice)}></TextField>
      <TextField variant="outlined" label="Years until expiry" size="small" sx={{ width: defaultWidth, ml : "1%" }} onChange={(e) => update(e.target.value, setStrikePrice)}></TextField>
      <br />
      <br />
      <OptionButton setClicked={setClicked}/>
    </div>
  )
}

export default OptionForm;
