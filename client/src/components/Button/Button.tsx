import React from 'react';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

type Props = {
    setClicked : (args : boolean) => void
}

const Btn = ({setClicked} : Props) => {
  return (
    <div>   
      <Button variant="contained" color="primary" sx={{textTransform: "None", width: "75%"}} onClick={() => setClicked(true)}>
        <Typography sx={{ fontSize: "large"}}>
            Get Data
        </Typography>
      </Button>
    </div>
  )
}

export default Btn;
