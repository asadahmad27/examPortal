import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router";
import { fetchUserById } from "../utils/mockAPI";
import Avatar from "./avatar";
import ExperienceDetails from "./experience-details";
import QualificationDetails from "./qualification-details";
import UserDetails from "./user-details";
import Layout from "./Layout"

const UserDetailsPage = () => {
    const navigate = useNavigate();
    const { user_id } = useParams();
    const params = useParams();
    const [userDetails, setUserDetails] = useState({});

    console.log(params)
    const abc = 8;
    const getUserData = () => {


    };

    useEffect(() => {
        const data = fetchUserById(user_id);
        console.log(data)
        setUserDetails(data?.[0]);
    }, [user_id]);

    console.log(user_id)
    return (
        <Layout>
            <div className="d-flex align-items-end justify-content-end p-5">
                <button className="btn btn-primary" onClick={() => navigate("/")}>
                    Logout
                </button>
            </div>
            <div className="container py-5">
                <div className="row">

                    <div className="col-lg-3 col-md-6">

                        <Avatar
                            src={userDetails?.personal_details?.image}
                            name={userDetails?.personal_details?.name}
                        />
                    </div>
                    <div className="col-lg-9 col-md-6">
                        <h2 className="mb-4 mt-4 mt-md-0">User Details</h2>
                        <div className="card mb-4">

                            <UserDetails data={userDetails?.personal_details} />
                        </div>
                        <div className="row">
                            <div className="col-lg-6 col-12">
                                <h2 className="mb-4">Qualification Details</h2>
                                <div className="card">
                                    <QualificationDetails
                                        data={userDetails?.qualification_details}
                                    />
                                </div>
                            </div>
                            <div className="col-lg-6 col-12">
                                <h2 className="mb-4 mt-4 mt-md-0">Experience Details</h2>
                                <div className="card">
                                    <ExperienceDetails data={userDetails?.experience_details} />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default UserDetailsPage;