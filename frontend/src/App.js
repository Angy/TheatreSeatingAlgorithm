import React, { Component } from 'react';
import './App.css';

import Hall from './components/Hall';
import Axios from 'axios';
import { ENDPOINT } from './utils';

export default class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            halls: []
        }
    }
    componentDidMount = () => {
        Axios.get(ENDPOINT + '/api/v1/halls/').then((resp) => {
            this.setState({ halls: resp.data })
        })
    }

    render() {
        const {halls} = this.state;
        return (
            <div className="App">
                {halls.map((hall, index )=> <Hall hallData={hall} key={index} />)}
            </div>
        );
    }

}
