import Link from "next/link"
import ThemeProvider from "@/pages/components/ThemeProvider";
import { Inter } from "next/font/google";

const inter = Inter({subsets: ["latin"]})

interface RootLayoutProps {
    children: React.ReactNode
}

export default function RootLayout({children}: RootLayoutProps) {
    return (
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
            <div className={`max-w-2xl mx-auto py-10 px-4 ${inter.className}`}>
                <header>
                    <div className="flex items-center justify-between">
                        <nav className="ml-auto text-sm font-medium space-x-6">
                            <Link href="/">Home</Link>
                            <Link href="/upload">Upload</Link>
                        </nav>
                    </div>
                </header>
                <main>{children}</main>
            </div>
        </ThemeProvider>
    )
}
