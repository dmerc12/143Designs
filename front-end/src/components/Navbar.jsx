import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { Link } from 'react-router-dom';
import { useNavigate } from '../hooks';

export const Navbar = ({ toast }) => {
    const navigate = useNavigate();

    const isLoggedIn = Cookies.get('sessionId');

    const handleLogout = () => {
        Cookies.remove('sessionId');
        navigate('/login');
        toast.current.addToast.success('Goodbye!');
    };
    
    return (
        <>
            <nav className='nav-bar'>
                <div className='nav-left'>
                    {isLoggedIn ? (
                        <>
                            <button id='manageRequestsNav' className='nav-item' to='/manage/requests'>Manage Requests</button>
                            <button id='manageReviewsNav' className='nav-item' to='/manage/reviews'>Manage Reviews</button>
                            <button id='managePastWorkNav' className='nav-item' to='/manage/past/work'>Manage Past Work</button>
                            <button id='manageUsersNav' className='nav-item' to='/manage/users'>Manage Users</button>
                        </>
                    ) : (
                        <>
                            <button id='contact' className='nav-item' to='/contact'>Contact Us</button>
                            <button id='reviews' className='nav-item' to='/reviews'>Reviews</button>
                            <button id='pastWork' className='nav-item' to='/past/work'>Past Work</button>
                        </>
                    )}
                </div>
                <div className='nav-right'>
                        {isLoggedIn ? (
                            <button id='logoutButton' className='nav-item' onClick={handleLogout}>Logout</button>
                        ) : (
                            <></>
                        )}
                </div>
            </nav>
        </>
    )
};

Navbar.propTypes = {
    toast: PropTypes.object.isRequired
};
