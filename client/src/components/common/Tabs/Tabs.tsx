import React, { useState } from 'react';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';

type Props = {
    setActiveTab : (args : number) => void;
}

const Options = ({setActiveTab} : Props) => {
    const [value, setValue] = useState("0");

    const handleChange = (event : React.SyntheticEvent, newValue : string) => {
        setValue(newValue);
        setActiveTab(parseInt(newValue));
    };

    const tabs = [
        "Daily Price Data",
        "Option Price Calculator"
    ];

    return (
        <Box sx={{ width: '100%' }}>
        <Tabs
            value={value}
            onChange={handleChange}
        >
            {tabs.map((text : string, index : number) => (
                <Tab value={index.toString()} label={text} />
            ))}
        </Tabs>
        </Box>
    );
}

export default Options; 