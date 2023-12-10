import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { useState } from 'react';
import { Modal } from '../../components';
import { useFetch, useNavigate } from '../../hooks';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';

export const ChangeEmailForm = ({ user, toast }) => {
    const sessionId = Cookies.get('sessionId');

    const [emailForm, setEmailForm] = useState({
        sessionId: sessionId,
        email: user.email
    });
    const [failedToFetch, setFailedToFetch] = useState(false);
    const [visible, setVisible] = useState(false);
    const [loading, setLoading] = useState(false);

    const { fetchData } = useFetch();

    const navigate = useNavigate();

    const showModal = () => {
        setVisible(true);
    };

    const closeModal = () => {
        setVisible(false);
    };

    const goBack = () => {
        setVisible(false);
        setFailedToFetch(false);
    };

    const onChange = (event) => {
        const { name, value } = event.target;
        setEmailForm((prevForm) => ({
            ...prevForm,
            [name]: value
        }));
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try {
            const { responseStatus, data } = await fetchData('/api/update/email', 'PUT', emailForm);

            if (responseStatus === 200) {
                closeModal();
                setLoading(false);
                toast.current.addToast.success('Email successfully updated!');
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Something went horribly wrong!");
            }
        } catch (error) {
            if (error.message === "No session found, please try again!" || error.message === "Session has expired, please log in!") {
                Cookies.remove('sessionId');
                navigate('/login');
                setLoading(false);
                closeModal();
                toast.current.addToast.warning(`${error.message}`);
            } else if (error.message === "Failed to fetch") {
                setLoading(false);
                setFailedToFetch(true);
                closeModal();
            } else {
                closeModal();
                setLoading(false);
                toast.current.addToast.warning(`${error.message}`);
            }
        }
    };

    return (
        <>
            <div className='component'>
                <button onClick={showModal} className='action-btn' id='changeEmailModal'>Change Email</button>
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
                    <form className='form' onSubmit={onSubmit}>
                        <div className='form-field'>
                            <label className='form-label' htmlFor="changeEmailInput">Email: </label>
                            <input className='form-input' type="text" id='changeEmailInput' name='email' value={emailForm.email} onChange={onChange}/>
                        </div>

                        <button id='changeEmailButton' className='form-btn-3' type='submit'>Update Information</button>
                    </form>
                )}
            </Modal>
        </>
    )
};

ChangeEmailForm.propTypes = {
    toast: PropTypes.object.isRequired
};
