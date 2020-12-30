import React, { useState, useEffect } from 'react';
import "./AttendSystem.css"
import AttendSearchBar from "./AttendSearchBar/AttendSearchBar";
import AttendTable from "./AttendTable/AttendTable";
import { Status } from "../Util";

const mock = [
    {
        Name: "Samuel Renan Costa Morais",
        Status:  Status.Present
    },
    {
        Name: "Saulo Bastos de Morais",
        Status:  Status.Present
    },
    {
        Name: "Jefferson de Oliveira Ferreira",
        Status:  Status.Absent
    },
    {
        Name: "Laura Moreano Cáceres",
        Status:  Status.Undefined
    },
    {
        Name: "Amanda Costa de Morais",
        Status:  Status.Undefined
    },
    {
        Name: "Samuel Renan Costa Morais",
        Status:  Status.Present
    },
    {
        Name: "Saulo Bastos de Morais",
        Status:  Status.Present
    },
    {
        Name: "Jefferson de Oliveira Ferreira",
        Status:  Status.Absent
    },
    {
        Name: "Laura Moreano Cáceres",
        Status:  Status.Undefined
    },
    {
        Name: "Amanda Costa de Morais",
        Status:  Status.Undefined
    },
    {
        Name: "Samuel Renan Costa Morais",
        Status:  Status.Present
    },
    {
        Name: "Saulo Bastos de Morais",
        Status:  Status.Present
    },
    {
        Name: "Jefferson de Oliveira Ferreira",
        Status:  Status.Absent
    },
    {
        Name: "Laura Moreano Cáceres",
        Status:  Status.Undefined
    },
    {
        Name: "Amanda Costa de Morais",
        Status:  Status.Undefined
    }
]

const AttendSystem = () => {
    const [allStudentsData, setAllStudentsData] = useState(mock);
    const [studentsData, setStudentsData] = useState(allStudentsData);

    const filterStudentsByName = value => {
        const filteredStudentData = allStudentsData.filter(std => std.Name.toLowerCase().includes(value.toLowerCase()));
        setStudentsData(filteredStudentData);
    }
    
    const updateStudentData = updatedStudentData => {
        console.log(updatedStudentData);
    }

    return (
        <div className="App-body">
            <div className="Attemd-system">
                <div className="Attend-system-content">
                    <p className="Attend-system-title">Aula 1 - Projetos de Sistemas Aeroespaciais</p>
                    <AttendSearchBar filterStudents={(value) => filterStudentsByName(value)} />
                    <AttendTable studentData={studentsData} updateStudentData={(updatedStudentData) => updateStudentData(updatedStudentData)} />
                </div>
            </div>
        </div>
    );
};

export default AttendSystem;