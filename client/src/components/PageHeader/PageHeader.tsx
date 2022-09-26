import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

type Props = {
    openDrawer : boolean;
    setOpenDrawer : (args : boolean) => void;
}

const PageHeader = ({openDrawer, setOpenDrawer}  : Props) => {
  return (   
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{backgroundColor: "ghostwhite"}}>
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="primary"
            aria-label="menu"
            sx={{ mr: 2 }}
            onClick={() => setOpenDrawer(!openDrawer)}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h5" component="div" color="primary" sx={{ flexGrow: 1 }}>
            Stock Market Trend Analyzer
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  )
}

export default PageHeader;
