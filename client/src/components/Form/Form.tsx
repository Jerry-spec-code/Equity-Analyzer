import React, {useState, useEffect} from 'react';
import dayjs, { Dayjs } from 'dayjs';
import Button from "../Button/Button";
import TextField from "@mui/material/TextField"
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker';
import ROUTES from '../../config/api';

type Props = {
    setData : (args : any) => void;
}

const Form = ({setData} : Props) => {

    const [clicked, setClicked] = useState(false);
    const [ticker, setTicker] = useState("");
    const [startDate, setStartDate] = useState<Dayjs | null>(dayjs('2022-08-18T21:11:54'));
    const [endDate, setEndDate] = useState<Dayjs | null>(dayjs('2022-08-18T21:11:54'),);

    const update = (value : string, setState : (args : string) => void) => {
        setState(value);
    }

    useEffect(() => {
        if (clicked) {
            setClicked(false);
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json"},
                body: JSON.stringify({ticker: ticker, startDate: startDate, endDate: endDate})
            }
            const fetchData = async () => {
                await fetch(ROUTES.getAllData, requestOptions)
                    .then((res) => res.json())
                    .then((data) => {
                        setData(data);
                        console.log(data);
                    })
            }
            fetchData();
        }
    }, [clicked])

    return (
    <div>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
        <TextField variant="outlined" label="Enter ticker" size="small" sx={{ width: "75%" }} onChange={(e) => update(e.target.value, setTicker)}></TextField>
        <br /><br />
        <DesktopDatePicker
          label="Enter start date"
          inputFormat="MM/DD/YYYY"
          value={startDate}
          onChange={(newValue: Dayjs | null) => setStartDate(newValue)}
          renderInput={(params) => <TextField sx={{ width: "75%" }} {...params} />}
        />
        <br /><br />
        <DesktopDatePicker
          label="Enter end date"
          inputFormat="MM/DD/YYYY"
          value={endDate}
          onChange={(newValue: Dayjs | null) => setEndDate(newValue)}
          renderInput={(params) => <TextField sx={{ width: "75%" }} {...params} />}
        />
        </LocalizationProvider>
        <br /><br />
        <Button setClicked={setClicked}/>
    </div>
    )
}

export default Form;
