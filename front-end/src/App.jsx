import './App.css';

import { useRef } from 'react';
import { ToastContainer } from './components';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ManageInformation } from './pages';

function App() {
  const toast = useRef().current.addToast;

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index path='/manage/information' element={<ManageInformation toast={toast} />} />
        </Routes>
      </BrowserRouter>

      <ToastContainer ref={toastRef} />
    </>
  )
}

export default App
