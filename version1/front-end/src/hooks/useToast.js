import { uuid } from '../lib';
import { useEffect, useState } from 'react';

export const useToast = () => {
    const [loaded, setLoaded] = useState(false);
    const [toastId] = useState(`toast-portal-${uuid()}`);

    useEffect(() => {
        const div = document.createElement('div');
        div.id = toastId;
        div.style = 'position: fixed; top: 10px; right: 10px;';
        document.getElementsByTagName('body')[0].prepend(div);
        setLoaded(true);

        return () => document.getElementsByTagName('body')[0].removeChild(div);
    }, [toastId]);

    return { loaded, toastId };
};
