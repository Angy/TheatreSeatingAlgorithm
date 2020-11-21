import React, { Component } from 'react'

export default class Seat extends Component {
    constructor(props) {
        super(props);
        // console.log(props)
    }

    render() {
        const {seatData} = this.props;
        return (
            <>
            {seatData.map((seat, index )=> 
                seat.is_blocked === true ? <div className="square"></div> : <div className="green-square"></div>)
            }
            </>
        )
        
    }
}
