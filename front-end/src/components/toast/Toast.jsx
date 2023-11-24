import PropTypes from 'prop-types';

export const Toast = ({ mode, onClose, message }) => {
    const classes = `toast ${mode}`

    return (
        <div onClick={onClose} className={classes}>
            <div id='toast' className="message">{message}</div>
        </div>
    )
};

Toast.propTypes = {
    mode: PropTypes.string.isRequired,
    onClose: PropTypes.func.isRequired,
    message: PropTypes.string.isRequired
};
