import type { Metadata } from 'next'
import { Outfit } from 'next/font/google'
import './globals.css'

const outfit = Outfit({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'CineMatch | AI Movie Recommender',
  description: 'Discover your next cinematic adventure with AI-powered recommendations.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={outfit.className}>
        <div className="fixed inset-0 overflow-hidden -z-10 pointer-events-none">
          <div className="blob bg-indigo-600 w-[400px] h-[400px] -top-20 -right-20" />
          <div className="blob bg-purple-600 w-[300px] h-[300px] -bottom-20 -left-20" style={{ animationDelay: '-5s' }} />
          <div className="blob bg-pink-600 w-[250px] h-[250px] top-[40%] left-[20%]" style={{ animationDelay: '-10s' }} />
        </div>
        {children}
      </body>
    </html>
  )
}
