import Axios from 'axios'
import React, { Component } from 'react'
import { ENDPOINT } from '../utils'
import Section from './Section'

export default class Hall extends Component {
    constructor(props) {
        super(props);

    }

    render() {
        const { hallData } = this.props
        return (
            <div className="container">
                <h1>{hallData.name}</h1>
                <h2>Scherm</h2>
                <div className="row">
                    <div className="col-2">
                            <Section  sections={hallData.sections[0]}/>
                        </div>
                        <div className="col-6">
                            <Section sections={hallData.sections[1]}/>
                        </div>
                        <div className="col-2">
                            <Section sections={hallData.sections[2]}/>
                        </div>
                    </div>
            </div>
        )
    }
}
