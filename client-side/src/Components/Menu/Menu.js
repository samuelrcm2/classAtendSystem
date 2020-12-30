import React from 'react';
import "./Menu.css";
import { Route, NavLink, Switch } from "react-router-dom";

import  AttendSystem  from "../AttendSystem/AttendSystem";
import  Classes  from "../Classes/Classes";
import  ProfessorArea  from "../ProfessorArea/ProfessorArea";

const Menu = () => {
    return (
        <>
            <header className="App-header">
                <div className="topnav">
                    <NavLink activeClassName="active" exact to="/classes">Aulas</NavLink>
                    <NavLink activeClassName="active" to="/attendcontroll">Controle de Faltas</NavLink>
                    <NavLink activeClassName="active" exact to="/professorarea">Área do Professor</NavLink>
                </div>
            </header>
            <Switch>
                <Route path="/classes" exact component={Classes}  />
                <Route path="/attendcontroll"  component={AttendSystem}  />
                <Route path="/professorarea" exact component={ProfessorArea}  />
            </Switch>
        </>
    );
};

export default Menu;