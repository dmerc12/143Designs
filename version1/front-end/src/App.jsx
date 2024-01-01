import './App.css';

import { useRef } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Home, Login, ManageUsers } from './pages';
import { Navbar, ToastContainer } from './components'

function App() {
  const toast = useRef();

  return (
    <>
      <Navbar toast={toast} />

      <BrowserRouter>
        <Routes>
          {/* <Route index path="/" element={<Home toast={toast}/>} />
          <Route index path="/home" element={<Home toast={toast}/>} /> */}
          <Route path='/login' element={<Login toast={toast} />} />
          <Route path='/manage/information' element={<ManageUsers toast={toast} />} />
          {/* <Route index path='/manage/requests' element={<ManageRequests toast={toast} />} /> */}
          {/* <Route index path='/manage/reviews' element={<ManageReviews toast={toast} />} /> */}
          {/* <Route index path='/manage/past/work' element={<ManagePastWork toast={toast} />} /> */}
          {/* <Route index path='/contact' element={<Contact toast={toast} />} /> */}
          {/* <Route index path='/reviews' element={<Reviews toast={toast} />} /> */}
          {/* <Route index path='/past/work' element={<PastWork toast={toast} />} /> */}

        </Routes>
      </BrowserRouter>

      <ToastContainer ref={toast} />
    </>
  )
}

export default App
