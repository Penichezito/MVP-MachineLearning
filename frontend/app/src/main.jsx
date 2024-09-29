import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
// import { Banner } from './components/Banner/Banner.jsx'
import App from './App.jsx';
import './index.css';
// import { Footer } from './components/Footer/Footer.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* <Banner /> */}
    <App />
  </StrictMode>,
)
