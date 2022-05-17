// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT


import React from 'react'
import { Nav, Navbar, NavDropdown, Container } from 'react-bootstrap';
import { Link } from 'react-router-dom';


const BaseNavbar = () => {
    return (
        <Navbar collapseOnSelect expand="lg" bg="primary" variant="dark">
            <Container>
                <Navbar.Brand as={Link} to="/">FastAPI FS</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link as={Link} to="/">Dashboard</Nav.Link>

                    </Nav>
                    <Nav>
                        <Nav.Link as={Link} to="/signin">Login</Nav.Link>
                        <NavDropdown title="Account" id="collasible-nav-dropdown">
                            <NavDropdown.Item as={Link} to="/profile">Profile</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item as={Link} to="/logout">Logout</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default BaseNavbar