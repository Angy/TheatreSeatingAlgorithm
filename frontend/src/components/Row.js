import React, { Component } from 'react'
import Seat from './Seat'

export default class Row extends Component {
    render() {
        return (
            <div className="d-flex">
                <Seat />
                <Seat />
                <Seat />
                <Seat />
            </div>
        )
    }
}
