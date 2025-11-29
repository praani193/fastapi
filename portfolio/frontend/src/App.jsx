import React from 'react'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Projects from './pages/Projects'
import Skills from './pages/Skills'
import Experience from './pages/Experience'
import Contact from './pages/Contact'


export default function App() {
return (
<div className="bg-gray-50 min-h-screen flex flex-col">
<Navbar />


<div className="flex-1 px-6 py-4">
<Routes>
<Route path="/" element={<Home />} />
<Route path="/projects" element={<Projects />} />
<Route path="/skills" element={<Skills />} />
<Route path="/experience" element={<Experience />} />
<Route path="/contact" element={<Contact />} />
</Routes>
</div>


<Footer />
</div>
)
}