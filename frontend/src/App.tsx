import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import Login from './components/Login';


function App() {
  return (
    <>
      <Router>
        <header>
          <Navbar />
        </header>
        <Route path="/" exact render={() => (
          <>
            <Dashboard />
          </>
        )}>
        </Route>
        <Route path="/signin" component={Login} />
        <Footer />
      </Router>
    </>
  );
};

export default App;
