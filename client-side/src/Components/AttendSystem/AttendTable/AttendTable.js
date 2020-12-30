import React from 'react';
import "./AttendTable.css";
import { VscError, VscTrash, VscCheck } from "react-icons/vsc";
import { Status } from "../../Util";

const AttendTable = (props) => {

    const updateStudentStatus = (studentData, newStatus) => {
        const newStudentData = {...studentData, Status: newStatus};
        props.updateStudentData(newStudentData);
    }

    return (
        <div className="Attend-table-component">
            <p>Alunos</p>
            <div className="Attend-table-div">
                <table>
                    <tbody>
                        {props.studentData.map(std => (
                            <tr> 
                                <td key={std.id + std.Name}>{std.Name}</td>
                                <td key={std.id + "present"}>
                                    <div className="Tooltip-save">
                                        <VscCheck onClick={() => updateStudentStatus(std, Status.Present)} fill={std.Status === Status.Present ?
                                            "green" : "gray"} />
                                        <span className="Tooltip-text-save">{std.Status === Status.Present ? "Presente" : "Marcar Presença"}</span>
                                    </div>
                                </td>
                                <td key={std.id + "absent"}>
                                    <div className="Tooltip-remove"> 
                                        <VscError onClick={() => updateStudentStatus(std, Status.Absent)} fill={std.Status === Status.Absent ?
                                            "red" : "gray"} />
                                        <span className="Tooltip-text-remove">{std.Status === Status.Absent ? "Ausente" : "Marcar Ausência"}</span>        
                                    </div>
                                </td>
                                <td key={std.id + "undefined"}>
                                    <div className="Tooltip-trash">
                                        <VscTrash  onClick={() => updateStudentStatus(std, Status.Undefined)} fill="gray" />
                                        <span className="Tooltip-text-trash">{std.Status === Status.Undefined ? "Não Informado" : "Limpar Dadoa"}</span>        
                                    </div>
                                </td>
                            </tr>
                        ))}

                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default AttendTable;