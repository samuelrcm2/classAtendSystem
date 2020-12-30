import React from 'react';
import { VscError, VscTrash, VscCheck } from "react-icons/vsc";

const Status = {
    Undefined: 0,
    Present: 1,
    Absent: 2
}

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

const AttendTable = () => {
    return (
        <div className="Attend-table-component">
            <p>Alunos</p>
            <div className="Attend-table-div">
                <table>
                    {mock.map(std => (
                        <tr> 
                            <td>{std.Name}</td>
                            <td>
                                <div className="Tooltip-save">
                                    <VscCheck onClick={() => console.log("BLABLA")} fill={std.Status === Status.Present ?
                                        "green" : "gray"} />
                                    <span className="Tooltip-text-save">{std.Status === Status.Present ? "Presente" : "Marcar Presença"}</span>
                                </div>
                            </td>
                            <td>
                                <div className="Tooltip-remove"> 
                                    <VscError onClick={() => console.log("BLABLA")} fill={std.Status === Status.Absent ?
                                        "red" : "gray"} />
                                    <span className="Tooltip-text-remove">{std.Status === Status.Absent ? "Ausente" : "Marcar Ausência"}</span>        
                                </div>
                            </td>
                            <td>
                                <div className="Tooltip-trash">
                                    <VscTrash  onClick={() => console.log("BLABLA")} fill="gray" />
                                    <span className="Tooltip-text-trash">{std.Status === Status.Undefined ? "Não Informado" : "Limpar Dadoa"}</span>        
                                </div>
                            </td>
                        </tr>
                    ))}
                </table>
            </div>
        </div>
    );
};

export default AttendTable;