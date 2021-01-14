import React, { Component } from 'react'

export default class Seat extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        const {seatData} = this.props;
        console.log(seatData)
        return (
            <>

            {seatData.map((seat, index )=>
                seat.is_blocked === true ? <div className="square" key={index}></div> : <div className="green-square" key={index}></div>
            )}
            </>
        )
    }
}
