import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Banner from './components/Banner/Banner.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Banner />
    <App />
  </StrictMode>,
)
