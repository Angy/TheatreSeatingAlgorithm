import React, { Component } from 'react'

export default class Seat extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        const {seatData} = this.props;
        return (
            <>

            {seatData.map((seat, index )=>
                seat.is_blocked === true ? <div className="square" key={index}>
                    <p id={'seat'}>{seat.seat_number}</p>
            </div> : <div className="green-square" key={index}><p id={'seat'}>{seat.seat_number}</p></div>
            )}
            </>
        )
    }
}
