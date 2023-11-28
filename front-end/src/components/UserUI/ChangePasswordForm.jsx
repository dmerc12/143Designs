import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { Modal } from '../../components';
import { useState } from 'react';
import { useFetch } from '../../hooks';
import { useNavigate } from 'react-router-dom';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';

export const ChangePasswordForm = ({ toast }) => {
    const sessionId = Cookies.get('sessionId');

    const [changePasswordForm, setChangePasswordForm] = useState({
        sessionId: sessionId,
        password: '',
        confirmationPassword: ''
    });
    const [formState, setFormState] = useState({
        loading: false,
        failedToFetch: false,
        visible: false
    });

    const { fetch } = useFetch();

    const navigate = useNavigate();

    const showModal = () => {
        setFormState.visible = true;
    };

    const closeModal = () => {
        setFormState.visible = false;
    };

    const goBack = () => {
        setFormState.failedToFetch = false;
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
        setFormState((prevState) => ({
            ...prevState,
            loading: true,
            failedToFetch: false
        }));
        try {
            const { responseStatus, data } = await fetch('/api/change/password', 'PUT', changePasswordForm);

            if (responseStatus === 200) {
                closeModal();
                setFormState.loading = false;
                toast.success('Information successfully updated!');
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Something went horribly wrong!");
            }
        } catch (error) {
            if (error.message === "No session found, please try again!" || error.message === "Session has expired, please log in!") {
                Cookies.remove('sessionId');
                navigate('/login');
                setFormState((prevState) => ({
                    ...prevState,
                    loading: false,
                    visible: false
                }));
                toast.warning(`${error.message}`);
            } else if (error.message === "Failed to fetch") {
                setFormState((prevState) => ({
                    ...prevState,
                    loading: false,
                    visible: false,
                    failedToFetch: true
                }));
            } else {
                setFormState((prevState) => ({
                    ...prevState,
                    loading: false,
                    visible: false
                }));
                toast.error(`${error.message}`);
            }
        }
    };

    return (
        <>
            <div className="component">
                <button onClick={showModal} className="action-btn" id="changePasswordModal">Change Password</button>
            </div>

            <Modal visible={formState.visible} onClose={closeModal}>
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
                            <label className="form-label" htmlFor="NewConfirmationPassword">Confirm Password: </label>
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
