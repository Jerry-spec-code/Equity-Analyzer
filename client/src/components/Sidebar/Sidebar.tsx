import React from 'react';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import Divider from '@mui/material/Divider';
import Form from '../Form/Form';

type Props = {
    openDrawer : boolean;
    setOpenDrawer : (args : boolean) => void;
    setData : (args : any) => void;
    setErrorMsg : (args : string) => void;
}

const Sidebar = ({openDrawer, setOpenDrawer, setData, setErrorMsg}  : Props) => {
    const drawerWidth = "12%";
    return (
    <div> {openDrawer && (
    <Drawer
        sx={{
            width: drawerWidth,
            flexShrink: 0,
            '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
            },
        }}
        variant="persistent"
        anchor="left"
        open={openDrawer}
        >
        <IconButton sx={{justifyContent: "start"}} onClick={() => setOpenDrawer(!openDrawer)}>
            <ChevronLeftIcon fontSize="large" sx={{margin: "7px"}}/>
        </IconButton>
        <Divider />
        <br />
        <Form setData={setData} setErrorMsg={setErrorMsg}/>
    </Drawer>
    )}
    </div>
    )
}

export default Sidebar;
