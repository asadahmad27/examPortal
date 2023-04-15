import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from 'react-router-dom';
import { axiosConfig } from "../utils/API";

const ExaminerSignup = () => {
  const navigate = useNavigate()
  const [fields, setFields] = useState({
    username: "",
    email: "",
    password: "",
    institution: "",
  });

  const [error, setError] = useState("");
  const handleChange = (e) => {

    const { value, name } = e.target;
    setFields({
      ...fields,
      [name]: value,
    });
  };

  const onSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post('http://localhost:5000/ExaminerSignup', fields, axiosConfig)
      if (res) {
        const { data } = res;

        if (data.error) {

          setError(data.error);
        } else {
          setError("");
          navigate("/home")
        }
      }

    } catch (err) {
      setError(err.message)
      console.log(err)
    }

  };


  return (
    <div className="FormBg">
      <style>
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
        />
      </style>
      <div className="bg-img">
        <div className="content" style={{ height: "590px", width: "510px" }}>
          <h1
            style={{
              marginBottom: "25px",
              color: "white",
              fontFamily: "'Poppins', sans-serif",
              fontWeight: "900",
            }}
          >
            Examiner Sign Up form
          </h1>
          {/* <header type="PI"> Put your Personal Information to Sign Up!</header> */}
          <form onSubmit={onSubmit}>
            <div className="maindiv">
              <span className="fa fa-user"></span>
              <input
                type="text"
                className="input-box"
                placeholder="Enter User Name"
                name="username"
                required
                value={fields.username}
                onChange={handleChange}
              />
            </div>
            <div className="maindiv">
              <span className="fa fa-mail-bulk"></span>
              <input
                type="email"
                className="input-box"
                placeholder="Enter Email Address"
                name="email"
                required
                value={fields.email}
                onChange={handleChange}
              />
            </div>

            <div className="maindiv">
              <span className="fa fa-lock"></span>
              <input
                type="password"
                id="pass"
                className="input-box"
                placeholder="Enter Password"
                name="password"
                required
                value={fields.password}
                onChange={handleChange}
              />
            </div>
            <div className="maindiv">
              <span className="fa fa-school"></span>
              <input
                type="text"
                id="pass"
                className="input-box"
                placeholder="Enter Institution"
                name="institution"
                required
                value={fields.institution}
                onChange={handleChange}
              />
            </div>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <span id="messageError"></span>
            <button type="submit" className="submit-btn">
              Register
            </button>
          </form>
          <div className="pass">
            <a href="/examiner-login">Already have an account? Log in</a>
          </div>
        </div>
      </div>
    </div>
  );
};
export default ExaminerSignup;
