import React, { Component } from 'react';
import Seat from '../components/Seat'

export default class Row extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        const {rows} = this.props;
        return (
            <>
            {rows.map((row, index )=> <Seat seatData={row.seats} key={index} />)}
            </>
        )
        
    }
}
