import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../App.css";
import axios from "axios";
import { axiosConfig } from "../utils/API";

const ExaminerLogin = () => {
  const navigate = useNavigate();
  const [showPassword, setShowPassword] = useState(false);
  const [fields, setFields] = useState({
    email: "",
    password: "",
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
      const res = await axios.post(
        "http://localhost:5000/ExaminerLogin",
        fields,
        axiosConfig
      );
      if (res) {
        const { data } = res;

        if (data.error) {
          setError(data.error);
        } else {
          setError("");
          navigate("/home");
        }
      }
    } catch (err) {
      setError(err.message);
      console.log(err);
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div className="FormBg">
        <div className="ExaminerLoginExaminer">
          <style>
            <link
              rel="stylesheet"
              href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
            />
          </style>
          <div className="bg-img">
            <div className="content">
              <header>
                <h1
                  style={{
                    color: "white",
                    fontFamily: "'Poppins', sans-serif",
                    fontWeight: "600",
                  }}
                >
                  Examiner Log In form
                </h1>
              </header>
              <header type="PI" style={{ color: "white" }}>
                Enter your registered mail and password:
              </header>

              <div className="maindiv">
                <span className="fa fa-user"></span>
                <input
                  type="text"
                  name="email"
                  className="fa input-box"
                  placeholder="Enter Email"
                  required
                  onChange={handleChange}
                />
              </div>

              <div className="maindiv">
                <span className="fa fa-lock"></span>
                <input
                  type="password"
                  className="pass-key"
                  id="pass-key"
                  name="password"
                  placeholder="Password"
                  required
                  onChange={handleChange}
                />
                <span className="show" id="show">
                  Show
                </span>
              </div>

              <div className="pass">
                <a href="/examiner-signup">Don't have an account? Sign up</a>
              </div>

              <button type="submit" className="submit-btn">
                ExaminerLogin
              </button>
            </div>
          </div>
        </div>
      </div>
    </form>
  );
};

export default ExaminerLogin;
