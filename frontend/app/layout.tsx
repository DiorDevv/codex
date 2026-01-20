import "./globals.css";
import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "ProFolio",
  description: "Personal portfolio with blog and admin panel",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <div className="min-h-screen">
          <header className="border-b border-white/10 bg-black/30">
            <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
              <Link className="text-lg font-semibold" href="/">
                ProFolio
              </Link>
              <nav className="flex gap-6 text-sm text-white/70">
                <Link href="/about">About</Link>
                <Link href="/projects">Projects</Link>
                <Link href="/blog">Blog</Link>
                <Link href="/contact">Contact</Link>
                <Link href="/admin">Admin</Link>
              </nav>
            </div>
          </header>
          <main className="mx-auto max-w-6xl px-6 py-12">{children}</main>
          <footer className="border-t border-white/10 py-8">
            <div className="mx-auto max-w-6xl px-6 text-sm text-white/60">
              © 2024 ProFolio. Crafted with FastAPI + Next.js.
            </div>
          </footer>
        </div>
      </body>
    </html>
  );
}
