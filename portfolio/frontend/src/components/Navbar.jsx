import React from 'react'
import { Link } from 'react-router-dom'


export default function Navbar() {
return (
<nav className="bg-white shadow p-4 flex justify-between items-center">
<h1 className="text-2xl font-bold">Portfolio</h1>


<div className="space-x-6 text-lg">
<Link to="/">Home</Link>
<Link to="/projects">Projects</Link>
<Link to="/skills">Skills</Link>
<Link to="/experience">Experience</Link>
<Link to="/contact">Contact</Link>
</div>
</nav>
)
}