import React, {useState} from 'react';
import PageHeader from './components/common/PageHeader/PageHeader';
import Sidebar from './components/common/Sidebar/Sidebar';
import Graph from './components/stock/Graph/Graph';
import Box from '@mui/material/Box';
import Error from './components/common/Error/Error';
import Tabs from './components/common/Tabs/Tabs';
import OptionForm from './components/option/Form/Form';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState(0);
  const [openDrawer, setOpenDrawer] = useState(true);
  const [data, setData] = useState({});
  const [errorMsg, setErrorMsg] = useState("");
  return (
    <div className="App">
      <PageHeader openDrawer={openDrawer} setOpenDrawer={setOpenDrawer}/>
      <Box ml={"43%"} mr={"5%"}>
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
