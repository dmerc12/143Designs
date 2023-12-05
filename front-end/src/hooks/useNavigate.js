export const useNavigate = () => {
    const navigate = (path) => {
        window.location.href = path;
    };

    return navigate;
};
