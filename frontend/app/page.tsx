import Link from "next/link";

export default function HomePage() {
    return (
        <div>
            <h1>Welcome to Reflect Journal</h1>
            <p>This is your starting page.</p>
            <Link href="/register">Go to Register</Link>
        </div>
    )
}
