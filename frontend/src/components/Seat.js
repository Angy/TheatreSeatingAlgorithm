import React, { Component } from 'react'

export default class Seat extends Component {
    constructor(){
        super()
        this.state = {
            seats: []
        }
    }
    componentDidMount(props){
        this.setState({seats:''})
    }
    render() {
        const seats = this.state.seats

        return (
            <div className="square"></div>
        )
    }
}
