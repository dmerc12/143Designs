import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import { uuid } from '../../lib';
import { useToast, useAutoClose } from '../../hooks';
import { forwardRef, useImperativeHandle, useState } from 'react';
import { Toast } from '../../components';

export const ToastContainer = forwardRef(function ToastContainer
    ({ autoClose = true, autoCloseTime = 5000 }, ref) {
        const [ toasts, setToasts] = useState([]);
        const { loaded, toastId } = useToast();

        useAutoClose({ toasts, setToasts, autoClose, autoCloseTime });

        const removeToast = id => {
            setToasts((toasts) => toasts.filter(toast => toast.id !== id));
        };

        useImperativeHandle(ref, () => ({
            addToast: {
                success: (message) => {
                    setToasts((toasts) => [...toasts, { mode: 'success', message, id: uuid() }]);
                },
                info: (message) => {
                    setToasts((toasts) => [...toasts, { mode: 'info', message, id: uuid() }]);
                },
                warning: (message) => {
                    setToasts((toasts) => [...toasts, { mode: 'warning', message, id: uuid() }]);
                },
            }
        }));

        return loaded ? ReactDOM.createPortal(
            <div className="toast-container">
                {toasts.map(toast => (
                    <Toast key={toast.id} mode={toast.mode} message={toast.message} onClose={() => removeToast(toast.id)} />
                ))}
            </div>,
            document.getElementById(toastId)
        ) : (
            <></>
        )
    }
);

ToastContainer.propTypes = {
    autoClose: PropTypes.bool,
    autoCloseTime: PropTypes.number
};
