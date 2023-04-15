import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Link
} from "react-router-dom";  //npm i react-router-dom 
import './App.css';
import Login from './Components/Login';
import Sidebar from './Components/Sidebar';
import ExaminerQualification from './Components/ExaminerQualification';
import ExaminerExp from './Components/ExaminerExp';
import Profile from './Components/Profile';
import Notifications from './Components/Notifications'
import RequestRecieved from './Components/RequestRecieved'
import AcceptedRequest from './Components/AcceptedRequest'
import UploadResult from './Components/UploadPaper'
import Home from './Components/Home';
import Navbar from './Components/Navbar'
import DuePaper from './Components/DuePaper';
import ResultPending from './Components/ResultPending';
import Settings from './Components/Settings';
import 'boxicons'
import { BrowserRouter } from "react-router-dom";
import UserDetailsPage from './Components/UserDetailsPage';
import UserSignup from './Components/UserSignup';
import ExaminerSignup from './Components/ExaminerSignup';
import ExaminerLogin from './Components/ExaminerLogin';

function App() {
  return (

    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/details/:user_id" element={<UserDetailsPage />} />
        <Route path="/user-signup" element={<UserSignup />} />
        <Route path="/examiner-signup" element={<ExaminerSignup />} />
        <Route path="/examiner-login" element={<ExaminerLogin />} />

        <Route path="/ExaminerQualification" element={<ExaminerQualification />} />
        <Route path="/ExaminerExp" element={<ExaminerExp />} />
        <Route path="/AcceptedRequest" element={<AcceptedRequest />} />
        <Route path="/RequestRecieved" element={<RequestRecieved />} />
        <Route path="/Notifications" element={<Notifications />} />
        <Route path="/Profile" element={<Profile />} />
        <Route path="/Home" element={<Home />} />
        <Route path="/DuePaper" element={<Home />} />
        <Route path="/ResultPending" element={<Home />} />
        <Route path="/UploadResult" element={<UploadResult />} />
      </Routes>

    </BrowserRouter>

  );
}

export default App
