import React, {useState} from 'react';
import PageHeader from './components/PageHeader/PageHeader';
import Sidebar from './components/Sidebar/Sidebar';
import Graph from './components/Graph/Graph';
import Box from '@mui/material/Box';
import Error from './components/Error/Error';
import './App.css';

function App() {
  const [openDrawer, setOpenDrawer] = useState(true);
  const [data, setData] = useState({});
  const [errorMsg, setErrorMsg] = useState("");
  return (
    <div className="App">
      <PageHeader openDrawer={openDrawer} setOpenDrawer={setOpenDrawer}/>
      <Sidebar openDrawer={openDrawer} setOpenDrawer={setOpenDrawer} setData={setData} setErrorMsg={setErrorMsg}/>
      <Box ml={"17%"} mr={"5%"}>
        <Error errorMsg={errorMsg}/>
        <Graph data={data}/>
      </Box>
    </div>
  );
}

export default App;
