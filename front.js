{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import React, \{ useState \} from 'react';\
\
const Home = () => (\
  <div>\
    <h2>Welcome to the Homepage</h2>\
    <p>Explore our services and features.</p>\
  </div>\
);\
\
const Profile = () => (\
  <div>\
    <h2>User Profile</h2>\
    <p>Manage your account settings and preferences.</p>\
  </div>\
);\
\
const Flights = () => (\
  <div>\
    <h2>Flights</h2>\
    <p>Search and book available flights.</p>\
  </div>\
);\
\
const CarRental = () => (\
  <div>\
    <h2>Car Rental & Accommodation</h2>\
    <p>Find rental cars and accommodation options.</p>\
  </div>\
);\
\
const Sidebar = (\{ currentPage, setCurrentPage \}) => (\
  <div style=\{\{ width: '150px', backgroundColor: '#f0f5f5', padding: '20px', position: 'fixed', top: '100px', left: '0', bottom: '0', overflowY: 'auto' \}\}>\
    <ul style=\{\{ listStyleType: 'none', padding: 0 \}\}>\
      <li style=\{\{ marginBottom: '10px' \}\}><button style=\{\{ textAlign: 'left', width: '100%', padding: '10px', border: 'none', backgroundColor: currentPage === 'home' ? '#0073e6' : 'transparent', color: currentPage === 'home' ? 'white' : 'black', cursor: 'pointer', fontFamily: 'Helvetica, sans-serif' \}\} onClick=\{() => setCurrentPage('home')\}>Home</button></li>\
      <li style=\{\{ marginBottom: '10px' \}\}><button style=\{\{ textAlign: 'left', width: '100%', padding: '10px', border: 'none', backgroundColor: currentPage === 'profile' ? '#0073e6' : 'transparent', color: currentPage === 'profile' ? 'white' : 'black', cursor: 'pointer', fontFamily: 'Helvetica, sans-serif' \}\} onClick=\{() => setCurrentPage('profile')\}>Profile</button></li>\
      <li style=\{\{ marginBottom: '10px' \}\}><button style=\{\{ textAlign: 'left', width: '100%', padding: '10px', border: 'none', backgroundColor: currentPage === 'flights' ? '#0073e6' : 'transparent', color: currentPage === 'flights' ? 'white' : 'black', cursor: 'pointer', fontFamily: 'Helvetica, sans-serif' \}\} onClick=\{() => setCurrentPage('flights')\}>Flights</button></li>\
      <li style=\{\{ marginBottom: '10px' \}\}><button style=\{\{ textAlign: 'left', width: '100%', padding: '10px', border: 'none', backgroundColor: currentPage === 'car-rental' ? '#0073e6' : 'transparent', color: currentPage === 'car-rental' ? 'white' : 'black', cursor: 'pointer', fontFamily: 'Helvetica, sans-serif' \}\} onClick=\{() => setCurrentPage('car-rental')\}>Car Rental & Accommodation</button></li>\
    </ul>\
  </div>\
);\
\
export default function App() \{\
  const [currentPage, setCurrentPage] = useState('home');\
\
  const renderPage = () => \{\
    switch (currentPage) \{\
      case 'home':\
        return <Home />;\
      case 'profile':\
        return <Profile />;\
      case 'flights':\
        return <Flights />;\
      case 'car-rental':\
        return <CarRental />;\
      default:\
        return null;\
    \}\
  \};\
\
  return (\
    <div style=\{\{ fontFamily: 'Helvetica, sans-serif', backgroundColor: '#e0ecf8', color: '#333', minHeight: '100vh', padding: '20px' \}\}>\
      <h1 style=\{\{ textAlign: 'center', margin: '0', backgroundColor: '#0073e6', color: 'white', padding: '10px', position: 'fixed', top: '0', width: '100%', zIndex: '1' \}\}>Flight Crew Main Menu</h1>\
      <Sidebar currentPage=\{currentPage\} setCurrentPage=\{setCurrentPage\} />\
      <div style=\{\{ marginLeft: '180px', padding: '20px', paddingTop: '130px' \}\}>\
        \{renderPage()\}\
      </div>\
    </div>\
  );\
\}\
}