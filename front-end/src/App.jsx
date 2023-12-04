import './App.css';

import { useRef } from 'react';
import { ToastContainer } from './components';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Home, Login, ManageInformation } from './pages';
import { Navbar } from './components'

function App() {
  const toast = useRef().current.addToast;

  return (
    <>
      <Navbar toast={toast} />

      <BrowserRouter>
        <Routes>
          <Route index path="/" element={<Home toast={toast}/>} />
          <Route index path="/home" element={<Home toast={toast}/>} />
          <Route index path='/login' element={<Login toast={toast} />} />
          <Route index path='/manage/information' element={<ManageInformation toast={toast} />} />
        </Routes>
      </BrowserRouter>

      <ToastContainer ref={toastRef} />
    </>
  )
}

export default App
