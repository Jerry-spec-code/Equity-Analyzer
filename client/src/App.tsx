import React, {useState} from 'react';
import PageHeader from './components/PageHeader/PageHeader';
import Sidebar from './components/Sidebar/Sidebar';
import Graph from './components/Graph/Graph';
import './App.css';

function App() {
  const [openDrawer, setOpenDrawer] = useState(true);
  const [data, setData] = useState({});
  return (
    <div className="App">
      <PageHeader openDrawer={openDrawer} setOpenDrawer={setOpenDrawer}/>
      <Sidebar openDrawer={openDrawer} setOpenDrawer={setOpenDrawer} setData={setData}/>
      <Graph />
    </div>
  );
}

export default App;
