export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en">
        <body>
        <header style={{ padding: "1rem", borderBottom: "1px solid #ccc" }}>
            <h2>Reflect Journal</h2>
        </header>

        <main style={{ padding: "2rem" }}>
            {children}
        </main>

        <footer style={{ padding: "1rem", borderTop: "1px solid #ccc" }}>
            <p>© 2025 Reflect</p>
        </footer>
        </body>
        </html>
    )
}
