import React, {useState} from 'react';
import PageHeader from './components/PageHeader/PageHeader';
import Sidebar from './components/Sidebar/Sidebar';
import Graph from './components/Graph/Graph';
import Box from '@mui/material/Box';
import Error from './components/Error/Error';
import Tabs from './components/Tabs/Tabs';
import OptionForm from './components/Form/OptionForm';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState(0);
  const [openDrawer, setOpenDrawer] = useState(true);
  const [data, setData] = useState({});
  const [errorMsg, setErrorMsg] = useState("");
  return (
    <div className="App">
      <PageHeader openDrawer={openDrawer} setOpenDrawer={setOpenDrawer}/>
      <Box ml={"40%"} mr={"5%"}>
        <Tabs setActiveTab={setActiveTab}/>
      </Box>
      <Sidebar openDrawer={openDrawer} setOpenDrawer={setOpenDrawer} setData={setData} setErrorMsg={setErrorMsg}/>
      <Box ml={"17%"} mr={"5%"}>
        <Error errorMsg={errorMsg}/>
        <Graph show={activeTab === 0} data={data}/>
        <OptionForm show={activeTab === 1} setErrorMsg={setErrorMsg}/>
      </Box>
    </div>
  );
}

export default App;
