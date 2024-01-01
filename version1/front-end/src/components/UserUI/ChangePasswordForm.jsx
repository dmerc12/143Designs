import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { useState } from 'react';
import { Modal } from '../../components';
import { useFetch, useNavigate } from '../../hooks';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';

export const ChangePasswordForm = ({ toast }) => {
    const sessionId = Cookies.get('sessionId');

    const [changePasswordForm, setChangePasswordForm] = useState({
        sessionId: sessionId,
        password: '',
        confirmationPassword: ''
    });
    const [visible, setVisible] = useState(false);
    const [loading, setLoading] = useState(false);
    const [failedToFetch, setFailedToFetch] = useState(false);

    const { fetch } = useFetch();

    const navigate = useNavigate();

    const showModal = () => {
        setVisible(true);
    };

    const closeModal = () => {
        setVisible(false);
    };

    const goBack = () => {
        setFailedToFetch(false);
    };

    const onChange = (event) => {
        const { name, value } = event.target;
        setChangePasswordForm((prevForm) => ({
            ...prevForm,
            [name]: value
        }));
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetch('/api/change/password', 'PUT', changePasswordForm);

            if (responseStatus === 200) {
                closeModal();
                setLoading (false);
                toast.current.addToast.success('Information successfully updated!');
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Something went horribly wrong!");
            }
        } catch (error) {
            if (error.message === "No session found, please try again!" || error.message === "Session has expired, please log in!") {
                Cookies.remove('sessionId');
                navigate('/login');
                setVisible(false);
                setLoading(false);
                toast.current.addToast.warning(`${error.message}`);
            } else if (error.message === "Failed to fetch") {
                setVisible(false);
                setLoading(false);
                setFailedToFetch(true);
            } else {
                setVisible(false);
                setLoading(false);
                toast.current.addToast.warning(`${error.message}`);
            }
        }
    };

    return (
        <>
            <div className="component">
                <button onClick={showModal} className="action-btn" id="changePasswordModal">Change Password</button>
            </div>

            <Modal visible={visible} onClose={closeModal}>
                {loading ? (
                    <div className='loading-indicator'>
                        <FaSpinner className='spinner' />
                    </div>
                ) : failedToFetch ? (
                    <div className='failed-to-fetch'>
                        <AiOutlineExclamationCircle className='warning-icon'/>
                        <p>Cannot connect to the back end server.</p>
                        <p>Please check your internet connection and try again.</p>
                        <button className='retry-button' onClick={onSubmit}><FaSync className='retry-icon'/> Retry</button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : (
                    <form className="form" onSubmit={onSubmit}>
                        <div className="form-field">
                            <label className="form-label" htmlFor="newPassword">New Password: </label>
                            <input className="form-input" type="password" id="newPassword" name="password" value={changePasswordForm.password} onChange={onChange}/>
                        </div>

                        <div className="form-field">
                            <label className="form-label" htmlFor="newConfirmationPassword">Confirm Password: </label>
                            <input className="form-input" type="password" id="newConfirmationPassword" name="confirmationPassword" value={changePasswordForm.confirmationPassword} onChange={onChange}/>
                        </div>

                        <button id="changePasswordButton" className="form-btn-1" type="submit">Change Password</button>
                    </form>
                )}
            </Modal>
        </>
    )
};

ChangePasswordForm.propTypes = {
    toast: PropTypes.object.isRequired
};
