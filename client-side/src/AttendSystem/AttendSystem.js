import React from 'react';
import AttendSearchBar from "./AttendSearchBar/AttendSearchBar";
import AttendTable from "./AttendTable/AttendTable";

const AttendSystem = () => {
    return (
        <div className="Attemd-system">
            <div className="Attend-system-content">
                <AttendSearchBar />
                <AttendTable />
            </div>
        </div>
    );
};

export default AttendSystem;