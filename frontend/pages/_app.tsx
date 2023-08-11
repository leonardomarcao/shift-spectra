import "./globals.css"
import RootLayout from "@/pages/layout";
import {Component} from "react";  // Adjust this path to where your RootLayout is.

class MyApp extends Component<{ Component: any, pageProps: any }> {
    render() {
        let {Component, pageProps} = this.props;
        return (
            <RootLayout>
                <Component {...pageProps} />
            </RootLayout>
        );
    }
}

export default MyApp;
