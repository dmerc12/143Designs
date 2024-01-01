import { useEffect, useState } from 'react';

export const useAutoClose = ({ toasts, setToasts, autoClose, autoCloseTime }) => {
    const [removing, setRemoving] = useState(null);

    useEffect(() => {
        if (removing) {
            setToasts(toasts.filter(toast => toast.id !== removing));
        }
    }, [removing, setToasts]);

    useEffect(() => {
        if (autoClose && toasts.length) {
            const id = toasts[toasts.length - 1].id;
            const timeoutId = setTimeout(() => setRemoving(id), autoCloseTime);

            return () => clearTimeout(timeoutId);
        }
    }, [autoClose, autoCloseTime, toasts]);
};
