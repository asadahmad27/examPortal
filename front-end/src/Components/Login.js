import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';
import '../App.css';
import { fetchUser } from '../utils/mockAPI';
import axios from 'axios';
import { axiosConfig } from '../utils/API';

const Login = () => {

    const navigate = useNavigate();
    const [showPassword, setShowPassword] = useState(false);
    const [fields, setFields] = useState({
        email: "",
        password: "",
    });
    const [error, setError] = useState("");
    const handleChange = (e) => {
        console.log(e.target)
        const { value, name } = e.target;
        setFields({
            ...fields,
            [name]: value,
        });
    };
    // const onSubmit = (e) => {

    //     // console.log("eisdj", fields)
    //     // e.preventDefault();

    //     // //mock API and mock function
    //     // const userData = fetchUser(fields.email, fields.password);
    //     // console.log(userData)
    //     // if (userData?.status) {
    //     //     setError("");
    //     //     navigate(`/details/${userData.id}`);
    //     // } else {
    //     //     setError("Email or password is incorrect");
    //     // }
    //     // // ;
    // };

    const onSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await axios.post('http://localhost:5000/UserLogin', fields, axiosConfig)
            if (res) {
                const { data } = res;
                console.log(data)
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
        <form onSubmit={onSubmit}>
            <div className='FormBg'>
                <div className='loginExaminer'>
                    <style>
                        <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css' />
                    </style>
                    <div className="bg-img">
                        <div className="content">
                            <header><h1 style={{ color: "white", fontFamily: "'Poppins', sans-serif", fontWeight: "600" }}>Log In form</h1></header>
                            <header type="PI" style={{ color: "white" }}>Enter your registered mail and password:</header>


                            <div className="maindiv">
                                <span className="fa fa-user"></span>
                                <input type="text" name='email' className="fa input-box" placeholder='Enter Email' required onChange={handleChange
                                } />
                            </div>

                            <div className="maindiv">
                                <span className='fa fa-lock'></span>
                                <input type="password" className="pass-key" id='pass-key' name='password' placeholder='Password' required onChange={handleChange} />
                                <span className='show' id='show'>Show</span>
                            </div>

                            <div className="pass">
                                <a href="/user-signup">Don't have an account? Sign up</a>
                            </div>

                            <button type="submit" className="submit-btn" >Login</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    )
}

export default Login