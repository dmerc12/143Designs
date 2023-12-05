import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { CreateUserForm } from '../components';

export const ManageUsers = ({ toast }) => {
    document.title = "Manage Information";

    const navigate = useNavigate();

    const sessionId = Cookies.get('sessionId');

    useEffect(() => {
        if (!sessionId) {
            navigate('/login');
            toast.info('Please login or register to gain access!' );
        }
    }, [toastRef, navigate, sessionId]);

    return (
        <>
            <h1>Manage Users</h1>
            <div className="action-btn-container">
                <CreateUserForm toastRef={toastRef} />
            </div>
        </>
    )
};

ManageUsers.propTypes = {
    toast: PropTypes.object.isRequired
};
