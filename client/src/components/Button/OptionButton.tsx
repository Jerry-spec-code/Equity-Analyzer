import React from 'react';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { CircularProgress } from '@mui/material';

type Props = {
    clicked : boolean;
    setClicked : (args : boolean) => void;
    updateStates : () => void;
}

const Btn = ({clicked, setClicked, updateStates} : Props) => {
  return (
    <div>   
      <Button disabled={clicked} variant="contained" color="primary" sx={{textTransform: "None", width: "25%"}} onClick={() => {setClicked(true); updateStates();}}>
        <Typography sx={{ fontSize: "large"}}>
            Get call and put prices
        </Typography>
        {clicked && <CircularProgress sx={{ ml : "15px"}}color="primary" />}
      </Button>
    </div>
  )
}

export default Btn;
