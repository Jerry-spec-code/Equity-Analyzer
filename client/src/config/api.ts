const API_ROOT = process.env.NODE_ENV === 'development' ? 'http://localhost:5000/api' : '/api';

const ROUTES = {
    getAllData : API_ROOT, 
};

export default ROUTES;