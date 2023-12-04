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
        toast.success('Goodbye!');
    };
    
    return (
        <>
            <nav className='nav-bar'>
                <div className='nav-left'>
                    {isLoggedIn ? (
                        <>
                            <Link id='manageRequestsNav' className='nav-item' to='/manage/requests'>Manage Requests</Link>
                            <Link id='manageReviewsNav' className='nav-item' to='/manage/reviews'>Manage Reviews</Link>
                            <Link id='managePastWorkNav' className='nav-item' to='/manage/past/work'>Manage Past Work</Link>
                            <Link id='manageUsersNav' className='nav-item' to='/manage/users'>Manage Users</Link>
                        </>
                    ) : (
                        <>
                            <Link id='contact' className='nav-item' to='/contact'>Contact Us</Link>
                            <Link id='reviews' className='nav-item' to='/reviews'>Reviews</Link>
                            <Link id='pastWork' className='nav-item' to='/past/work'>Past Work</Link>
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
