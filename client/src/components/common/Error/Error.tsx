import React from 'react';
import Typography from '@mui/material/Typography';

type Props = {
    errorMsg: string; 
}

const Error = ({errorMsg} : Props) => {
    return (
        <Typography variant="h2" component="div" color="error" sx={{ flexGrow: 1 }}>
            {errorMsg}
        </Typography>
    )
}

export default Error;
