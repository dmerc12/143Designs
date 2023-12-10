import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { useEffect } from 'react';
import { useNavigate } from '../hooks';
import { UserList } from '../components';

export const ManageUsers = ({ toast }) => {
    document.title = "Manage Information";

    const navigate = useNavigate();

    const sessionId = Cookies.get('sessionId');

    useEffect(() => {
        if (!sessionId) {
            navigate('/login');
            toast.current.addToast.info('Please login or register to gain access!' );
        }
    }, [toastRef, navigate, sessionId]);

    return (
        <>
            <h1>Manage Users</h1>
            <div className="action-btn-container">
                <UserList toast={toast} />
            </div>
        </>
    )
};

ManageUsers.propTypes = {
    toast: PropTypes.object.isRequired
};
