import React, { useState, useEffect, ChangeEvent } from 'react'
import { TextField, Grid, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, FormGroup, FormControlLabel, Switch } from '@mui/material'
import OptionButton from "../Button/OptionButton"
import ROUTES from '../../config/api';

type Props = {
    show : boolean;
    setErrorMsg : (args : string) => void;
};

interface OptionData {
    status: string;
    monteCarloCallPrice: number;
    monteCarloPutPrice: number;
    blackScholesCallPrice: number | null;
    blackScholesPutPrice: number | null;
    deltaCall: number | null;
    deltaPut: number | null;
    gammaCall: number | null;
    gammaPut: number | null;
    vegaCall: number | null;
    vegaPut: number | null;
    thetaCall: number | null;
    thetaPut: number | null;
    rhoCall: number | null;
    rhoPut: number | null;
};  

interface OptionTable {
    option: string;
    put: number | null;
    call: number | null;
};

interface OptionFormInputs {
    underlyingPrice: string;
    strikePrice: string;
    interestRate: string;
    volatility: string;
    expires: string;
    runMonteCarlo: boolean;
};

interface FieldConfig {
    label: string;
    name: keyof OptionFormInputs;
}

const OptionForm = ({show, setErrorMsg} : Props) => {
    
    const [clicked, setClicked] = useState(false);
    const [data, setData] = useState<OptionData | null>(null);
    const [formData, setFormData] = useState<OptionFormInputs>({
        underlyingPrice: "100.0",
        strikePrice: "100.0",
        interestRate: "0.05", // Risk-free rate (5%)
        volatility: "0.20", // Volatility of the underlying asset (20%)
        expires: "1.0", // One year until expiry
        runMonteCarlo: false,
    });

    const defaultWidth = "40%";

    const fieldConfig : FieldConfig[] =  [
        {label: "Underlying price ($)", name: "underlyingPrice"},
        {label: "Strike price ($)", name: "strikePrice"},
        {label: "Risk-free interest rate (decimal)", name: "interestRate"},
        {label: "Volatility (decimal)", name: "volatility"},
        {label: "Maturity (years)", name: "expires"},
    ];

    const handleChange = (value : string | boolean, name: keyof OptionFormInputs) => {
        setFormData({
          ...formData,
          [name]: value,
        });
      };

    useEffect(() => {
        if (clicked) {
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json"},
                body: JSON.stringify(formData),
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
                            setData(null);
                        }
                        setClicked(false);
                    })
            }
            fetchData();
        }
    }, [clicked]);

    if (!show) {
        return <> </>
    }

    const Display = () => {
        if (data == null) {
            return <> </>
        }
        
        const table : OptionTable[] = [
            {option : "Monte Carlo", call : data.monteCarloCallPrice, put : data.monteCarloPutPrice },
            {option : "Black Scholes", call : data.blackScholesCallPrice, put : data.blackScholesPutPrice },
            {option : "Delta", call : data.deltaCall, put : data.deltaPut },
            {option : "Gamma", call : data.gammaCall, put : data.gammaPut },
            {option : "Vega", call : data.vegaCall, put : data.vegaPut },
            {option : "Theta", call : data.thetaCall, put : data.thetaPut },
            {option : "Rho", call : data.rhoCall, put : data.rhoPut },
        ];
        
          return (
            <TableContainer component={Paper}>
              <Table aria-label="option price table">
                <TableHead>
                  <TableRow>
                    <TableCell></TableCell>
                    <TableCell>Call Option</TableCell>
                    <TableCell>Put Option</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {table.map((row) => (
                    <TableRow key={row.option}>
                      <TableCell>{row.option}</TableCell>
                      <TableCell>{row.call}</TableCell>
                      <TableCell>{row.put}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          );
    }

    return (
        <div>
            <Grid container spacing={2}>
                <Grid item xs={6}>
                    <br />
                    <Grid container spacing={2}>
                        {fieldConfig.map((field) => {
                            return <Grid item xs={12}>
                                <TextField label={field.label} variant="outlined" value={formData[field.name]} size="small" sx={{ width: defaultWidth}} onChange={(e) => handleChange(e.target.value, field.name)} />
                            </Grid>
                        })}
                        <Grid item xs={12}>
                            <FormControlLabel control={<Switch checked={formData["runMonteCarlo"]} onChange={(e) => handleChange(e.target.checked, "runMonteCarlo")} />} label="Run Monte Carlo (will take longer to load)" />
                        </Grid>
                    </Grid>
                    <br />
                    <OptionButton clicked={clicked} setClicked={setClicked}/>
                </Grid>
                <Grid item xs={6}>
                    <br />
                    <Display />
                </Grid>
            </Grid>
        </div>
  )
}

export default OptionForm;
