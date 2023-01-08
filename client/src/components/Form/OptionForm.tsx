import React, { useState, useEffect } from 'react'
import { TextField } from '@mui/material'
import Typography from '@mui/material/Typography';
import OptionButton from "../Button/OptionButton"
import ROUTES from '../../config/api';

type Props = {
    show : boolean;
    setErrorMsg : (args : string) => void;
};

interface OptionData {
    status? : string;
    callPrice? : number;
    putPrice? : number;
};  

const OptionForm = ({show, setErrorMsg} : Props) => {
    
    const [clicked, setClicked] = useState(false);
    const [data, setData] = useState<OptionData>({});

    const [optionPrice, setOptionPrice] = useState("100.0");
    const [strikePrice, setStrikePrice] = useState("100.0");
    const [interestRate, setInterestRate] = useState("0.05"); // Risk-free rate (5%)
    const [volatility, setVolatility] = useState("0.20"); // Volatility of the underlying (20%)
    const [expires, setExpires] = useState("1.0");    // One year until expiry

    const [optionPriceTemp, setOptionPriceTemp] = useState("100.0");
    const [strikePriceTemp, setStrikePriceTemp] = useState("100.0");
    const [interestRateTemp, setInterestRateTemp] = useState("0.05"); // Risk-free rate (5%)
    const [volatilityTemp, setVolatilityTemp] = useState("0.20"); // Volatility of the underlying (20%)
    const [expiresTemp, setExpiresTemp] = useState("1.0");    // One year until expiry

    const defaultWidth = "20%";

    const inputMessages = [
        ["Underlying price", optionPrice],
        ["Strike price", strikePrice],
        ["Risk-free interest rate", interestRate],
        ["Volatility", volatility],
        ["Maturity (years)", expires],
    ];

    const updateStates = () => {
        setOptionPrice(optionPriceTemp);
        setStrikePrice(strikePriceTemp);
        setInterestRate(interestRateTemp);
        setVolatility(volatilityTemp);
        setExpires(expiresTemp);
    }

    useEffect(() => {
        if (clicked) {
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
                        setClicked(false);
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

    const Display = () => {
        if (Object.keys(data).length === 0) {
            return <> </>
        }

        const outputMessages = [
            ["Call Price", data.callPrice],
            ["Put Price", data.putPrice],
        ]

        return (
        <div>
            <Typography sx={{ mt: "14px", fontWeight: "bold" }} variant="h6">Input Data:</Typography>
            <ul style={{ display: "inline-block" }}>
                {inputMessages.map((input) => {
                    return <li style={{ textAlign : "left", fontSize: "16px", marginTop : "5px"}}>
                            {`${input[0]}: ${input[1]}`}
                        </li>
                })}
            </ul>
            <Typography sx={{fontWeight: "bold" }} variant="h6">Results:</Typography>
            <ul style={{ display: "inline-block" }}>
                {outputMessages.map((output) => {
                    return <li style={{ textAlign : "left", fontSize: "16px", marginTop : "5px"}}>
                            {`${output[0]}: ${output[1]}`}
                        </li>
                })}
            </ul>
        </div>
        )
    }

    let i = 0;

    return (
    <div>
      <br />
      <TextField variant="outlined" label={inputMessages[i++][0]} size="small" sx={{ width: defaultWidth }} onChange={(e) => update(e.target.value, setOptionPriceTemp)}></TextField>
      <TextField variant="outlined" label={inputMessages[i++][0]} size="small" sx={{ width: defaultWidth, ml : "1%" }} onChange={(e) => update(e.target.value, setStrikePriceTemp)}></TextField>
      <TextField variant="outlined" label={inputMessages[i++][0]} size="small" sx={{ width: defaultWidth, ml : "1%" }} onChange={(e) => update(e.target.value, setInterestRateTemp)}></TextField>
      <br />
      <br />
      <TextField variant="outlined" label={inputMessages[i++][0]} size="small" sx={{ width: defaultWidth }} onChange={(e) => update(e.target.value, setVolatilityTemp)}></TextField>
      <TextField variant="outlined" label={inputMessages[i++][0]} size="small" sx={{ width: defaultWidth, ml : "1%" }} onChange={(e) => update(e.target.value, setExpiresTemp)}></TextField>
      <br />
      <br />
      <OptionButton clicked={clicked} setClicked={setClicked} updateStates={updateStates}/>
      <Display />
    </div>
  )
}

export default OptionForm;
