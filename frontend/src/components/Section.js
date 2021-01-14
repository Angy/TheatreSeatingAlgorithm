import React, { Component } from 'react';
import Row from '../components/Row'

export default class Section extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        const {sections} = this.props;
        return (
            <>
                <Row rows={sections.rows} />)
            </>
        )
    }
}
