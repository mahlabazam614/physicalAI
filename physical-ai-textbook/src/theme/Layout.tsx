import React from 'react';
import Layout from '@theme-original/Layout';
import ChatWidget from '@site/src/components/ChatWidget';

export default function LayoutWrapper(props: any): JSX.Element {
    return (
        <>
            <Layout {...props} />
            <ChatWidget />
        </>
    );
}
