const API_ROOT = process.env.NODE_ENV === 'development' ? 'http://localhost:5000/api' : '/api';

const ROUTES = {
    stock : API_ROOT, 
    option : `${API_ROOT}/options`,
};

export default ROUTES;