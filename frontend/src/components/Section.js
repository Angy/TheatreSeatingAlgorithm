import React, { Component } from 'react';
import Row from '../components/Row'

export default class Section extends Component {
    constructor(props) {
        super(props);
    }
    // componentDidMount = () => {
    //     Axios.get(ENDPOINT + '/api/v1/sections/').then((resp) => {
    //         this.setState({ sections: resp.data })
    //     })
    // }

    render() {
        const {sections} = this.props;
        return (
            <>
            {sections.map((section, index )=> <Row rows={section.rows} key={index} />)}
            </>
        )
    }
}
