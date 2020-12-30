import React from 'react';
import "./AttendSearchBar.css";

const AttendSearchBar = (props) => {

    const filterStudents = value => {
        props.filterStudents(value.trim());
    }

    return (
        <div className="Attend-search-bar">
            <label form="fname">Buscar</label>
            <input type="text" id="fname" name="fname" onChange={(ev) => filterStudents(ev.target.value)} />
        </div>
    );
};

export default AttendSearchBar;