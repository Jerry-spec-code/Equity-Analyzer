import React from 'react';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { CircularProgress } from '@mui/material';

type Props = {
    clicked : boolean;
    setClicked : (args : boolean) => void;
}

const Btn = ({clicked, setClicked} : Props) => {
  return (
    <div>   
      <Button disabled={clicked} variant="contained" color="primary" sx={{textTransform: "None", width: "40%"}} onClick={() => {setClicked(true);}}>
        <Typography sx={{ fontSize: "large"}}>
            Calculate
        </Typography>
        {clicked && <CircularProgress sx={{ ml : "20px"}} color="primary" />}
      </Button>
    </div>
  )
}

export default Btn;
