import PropTypes from 'prop-types';

import { LoginForm } from '../components';

export const Login = ({ toast }) => {
    document.title = "Login"

    return (
        <>
            <LoginForm toast={toast}/>
        </>
    )
};

Login.propTypes = {
    toast: PropTypes.object.isRequired
};
