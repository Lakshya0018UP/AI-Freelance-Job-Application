import React, { useState, useEffect, createContext } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import axios from "axios";
import "./App.css";

const AuthContext = createContext();

const API_URL = "http://127.0.0.1:5000/api";

function JobList() {
    const [jobs, setJobs] = useState([]);

    useEffect(() => {
        axios.get(`${API_URL}/jobs`).then(res => setJobs(res.data)).catch(err => console.error(err));
    }, []);

    return (
        <div className="p-4">
            <h2 className="text-xl font-bold">Job Listings</h2>
            <ul>
                {jobs.map(job => (
                    <li key={job.id} className="border p-2 my-2">{job.title} - ₹{job.budget}- {job.description}</li>
                ))}
            </ul>
        </div>
    );
}

function CreateJob() {
    const [form, setForm] = useState({ title: "", description: "", budget: "" });
    const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });
    
    const handleSubmit = async e => {
        e.preventDefault();
        await axios.post(`${API_URL}/jobs`, form);
        alert("Job created!");
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 border">
            <input type="text" name="title" placeholder="Title" className="border p-2" onChange={handleChange} required /><br />
            <input type="text" name="description" placeholder="Description" className="border p-2" onChange={handleChange} required /><br />
            <input type="number" name="budget" placeholder="Budget" className="border p-2" onChange={handleChange} required /><br />
            <button type="submit" className="bg-blue-500 text-white p-2 mt-2">Create Job</button>
        </form>
    );
}

function Signup() {
    const [form, setForm] = useState({ username: "", name: "", email: "", password_hash: "", role: "" });
    const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });
    
    const handleSubmit = async e => {
        e.preventDefault();
        await axios.post(`${API_URL}/signup`, form);
        alert("User registered!");
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 border">
            <input type="text" name="username" placeholder="Username" className="border p-2" onChange={handleChange} required /><br />
            <input type="text" name="name" placeholder="Name" className="border p-2" onChange={handleChange} required /><br />
            <input type="email" name="email" placeholder="Email" className="border p-2" onChange={handleChange} required /><br />
            <input type="password" name="password_hash" placeholder="Password" className="border p-2" onChange={handleChange} required /><br />
            <input type="text" name="role" placeholder="Role" className="border p-2" onChange={handleChange} required /><br />
            <button type="submit" className="bg-green-500 text-white p-2 mt-2">Sign Up</button>
        </form>
    );
}

function Login() {
    const [form, setForm] = useState({ username: "", password: "" });
    const { setAuth } = React.useContext(AuthContext);
    const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });
    
    const handleSubmit = async e => {
        e.preventDefault();
        const res = await axios.post(`${API_URL}/login`, form);
        setAuth(res.data);
        alert("Logged in!");
    };

    return (
        <form onSubmit={handleSubmit} className="p-4 border">
            <input type="text" name="username" placeholder="Username" className="border p-2" onChange={handleChange} required /><br />
            <input type="password" name="password" placeholder="Password" className="border p-2" onChange={handleChange} required /><br />
            <button type="submit" className="bg-blue-500 text-white p-2 mt-2">Login</button>
        </form>
    );
}

function App() {
    const [auth, setAuth] = useState(null);
    return (
        <AuthContext.Provider value={{ auth, setAuth }}>
            <Router>
                <nav className="p-4 bg-gray-200">
                    <Link to="/">Home</Link> | <Link to="/create-job">Create Job</Link> | <Link to="/signup">Signup</Link> | <Link to="/login">Login</Link>
                </nav>
                <Routes>
                    <Route path="/" element={<JobList />} />
                    <Route path="/create-job" element={<CreateJob />} />
                    <Route path="/signup" element={<Signup />} />
                    <Route path="/login" element={<Login />} />
                </Routes>
            </Router>
        </AuthContext.Provider>
    );
}

export default App;
