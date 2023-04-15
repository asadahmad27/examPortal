import React from 'react'
import Header from './Header'

const Layout = ({ children }) => {
    return (
        <>
            <Header />
            <div className='row'>
                <div className='col-2'>
                    <div className='VerNavbar'>
                        <div className='vernav'>
                            <a href="/Home">Home</a>
                            <a href="/Notifications">Requests</a>
                            <a href="/DuePaper">Due Paper</a>
                            <a href="ResultPending">Result Pending</a>
                        </div>
                        <div>
                            {"hello"}
                        </div>
                    </div>
                </div>
                <div className='col-10'>
                    {children}
                </div>
            </div>
        </>

    )
}

export default Layout
