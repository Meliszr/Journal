'use client'

import { useState } from 'react'

export default function RegisterPage() {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [username, setUsername] = useState('')
    const [birthdate, setBirthday] = useState('')
    const [message, setMessage] = useState('')

    async function handleRegister(e: React.FormEvent) {
        e.preventDefault()
        console.log({ email, password, username, birthdate })
        try {
            const res = await fetch('http://localhost:8000/auth/register', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    email,
                    password,
                    username,
                    birthdate,
                }),
            })
            const data = await res.json()

            if (res.ok) {
                setMessage(data.message || 'User created successfully!')
            } else {
                setMessage(data.detail || 'Something went wrong.')
            }
        } catch (error) {
            setMessage('Registration failed. Please try again.');
        }
    }


    return (
        <div style={{padding: "2rem"}}>
            <h1>Register</h1>

            <form
                onSubmit={handleRegister}>
                <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                />

                <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />

                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />

                <input
                    type="date"
                    placeholder="Birthdate"
                    value={birthdate}
                    onChange={(e) => setBirthday(e.target.value)}
                />


                <button type="submit">Register</button>
            </form>
            {message && <p>{message}</p>}
        </div>

    )
}