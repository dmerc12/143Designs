import Cookies from 'js-cookie';
import PropTypes from 'prop-types';

import { useState } from 'react';
import { useFetch, useNavigate } from '../../hooks';
import { FaSpinner } from 'react-icons/fa';
import { AiOutlineExclamationCircle } from 'react-icons/ai';

export const CreateUserForm = ({ toast }) => {
    sessionId = Cookies.get('sessionId');

    const [createUserForm, setCreateUserForm] = useState({
        sessionId: sessionId,
        email: '',
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
        setCreateUserForm((prevForm) => ({
            ...prevForm,
            [name]: value
        }));
    };

    const onSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setFailedToFetch(false);
        try{
            const { responseStatus, data } = await fetch('/api/create/user', 'POST', createUserForm);

            if (responseStatus === 201) {
                setCreateUserForm({
                    sessionId: sessionId,
                    email: '',
                    password: '',
                    confirmationPassword: ''
                });
                setLoading(false);
                closeModal();
                toast.current.addToast.success("User successfully created!");
            } else if (responseStatus === 400) {
                throw new Error(`${data.message}`);
            } else {
                throw new Error("Cannot connect to the back-end, please try again!");
            }
        } catch (error) {
            if (error.message === "No session found, please try again!" || error.message === "Session has expired, please log in!") {
                Cookies.remove('sessionId');
                navigate('/login');
                toast.current.addToast.warning(`${error.message}`);
            } else if (error.message === "Failed to fetch") {
                setLoading(false);
                setFailedToFetch(true);
            } else {
                setLoading(false);
                toast.current.addToast.warning(`${error.message}`);
            }
        }
    };

    return (
        <>
            <div className='component'>
                <button onClick={showModal} className='action-btn' id='createUserModal'>Create New User</button>
            </div>

            <Modal visible={visible} onClose={closeModal}>
                {loading ? (
                    <div className='loading-indicator'>
                        <FaSpinner className='spinner' />
                    </div>
                ) : failedToFetch ? (
                    <div className='failed-to-fetch'>
                        <AiOutlineExclamationCircle className='warning-icon' />
                        <p>Cannot connect to the back-end server.</p>
                        <p>Please check your internet connection and try again.</p>
                        <button className='retry-button' onClick={onSubmit}><FaSync className='retry-icon' /> Retry</button>
                        <button className='back-button' onClick={goBack}>Go Back</button>
                    </div>
                ) : (
                    <form className='form' onSubmit={onSubmit}>
                        <div className='form-field'>
                            <label className='form-label' htmlFor='createUserEmail'>Email: </label>
                            <input className='form-input' type='email' id='createUserEmail' name='email' value={createUserForm.email} onChange={onChange}></input>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor='createUserPassword'>Password: </label>
                            <input className='form-input' type='password' id='createUserPassword' name='password' value={createUserForm.password} onChange={onChange}></input>
                        </div>

                        <div className='form-field'>
                            <label className='form-label' htmlFor='createUserConfirmationPassword'>Confirm Password: </label>
                            <input className='form-input' type='password' id='createUserConfirmationPassword' name='confirmationPassword' value={createUserForm.confirmationPassword} onChange={onChange}></input>
                        </div>

                        <button id='createUserButton' className='form-btn-1' type='submit'>Create User</button>
                    </form>
                )}
            </Modal>
        </>
    )
};

CreateUserForm.propTypes = {
    toast: PropTypes.object.isRequired
};
