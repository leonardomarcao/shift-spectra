/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    darkMode: ["class"],
    theme: {
        extend: {},
    },
    plugins: [require("@tailwindcss/typography")],
}
