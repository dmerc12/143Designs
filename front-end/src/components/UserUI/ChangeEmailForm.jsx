import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { Modal } from '../../components';
import { useState, useEffect } from 'react';
import { useFetch } from '../../hooks';
import { useNavigate } from 'react-router-dom';
import { FaSpinner, FaSync } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';

export const ChangeEmailForm = ({ toast }) => {
    const sessionId = Cookies.get('sessionId');

    const [emailForm, setEmailForm] = useState({
        sessionId: sessionId,
        email: ''
    });
    const [formState, setFormState] = useState({
        userPresent: true,
        loading: false,
        failedToFetchData: false,
        failedToFetchSubmission: false,
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
        if (formState.userPresent) {
            setFormState((prevState) => ({
                ...prevState,
                failedToFetchData: false,
                failedToFetchSubmission: false
            }));
        } else {
            setFormState((prevState) => ({
                ...prevState,
                visible: false,
                failedToFetchData: false,
                failedToFetchSubmission: false
            }));
        }
    };

    const onChange = (event) => {
        const { name, value } = event.target;
        setEmailForm((prevForm) => ({
            ...prevForm,
            [name]: value
        }));
    };

    const fetchUser = async () => {
        setFormState((prevState) => ({
            ...prevState,
            loading: true,
            failedToFetchData: false
        }));
        try {
            const { responseStatus, data } = await fetchData('/api/get/user', 'PATCH', {'sessionId': sessionId});

            if (responseStatus === 200) {
                setUpdateForm((prevForm) => ({
                    ...prevForm,
                    email: data.email
                }));
                setFormState((prevForm) => ({
                    ...prevForm,
                    userPresent: true,
                    loading: false
                }));
            } else if (responseStatus === 400) {
                throw new Error(`${data.messsage}`);
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
                    failedToFetchData: true
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

    const onSubmit = async (event) => {
        event.preventDefault();
        setFormState((prevState) => ({
            ...prevState,
            loading: true,
            failedToFetchSubmission: false
        }));
        try {
            const { responseStatus, data } = await fetchData('/api/update/email', 'PUT', emailForm);

            if (responseStatus === 200) {
                closeModal();
                setFormState.loading = false;
                toast.success('Password successfully changed!');
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
                    failedToFetchSubmission: true
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
    
    useEffect(() => {
        if (!formState.userPresent) {
            fetchUser();
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [formState.userPresent]);

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
                ) : formState.failedToFetchData ? (
                    <div className='failed-to-fetch'>
                        <AiOutlineExclamationCircle className='warning-icon'/>
                        <p>Cannot connect to the back end server.</p>
                        <p>Please check your internet connection and try again.</p>
                        <button className='retry-button' onClick={fetchUser}><FaSync className='retry-icon'/> Retry</button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : formState.failedToFetchSubmission ? (
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
