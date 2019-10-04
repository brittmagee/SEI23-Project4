import React, { Component } from 'react'
import 'bulma/css/bulma.css'

import Title from './Title.js'
import Benefits from './Benefits.js'
import Parallax from './Parallax.js'
import Bikes from './Bikes.js'
import Testimonials from './Testimonials.js'

export default class Main extends Component {
    render() {
        return (
            <div>
                <Title />
                <Benefits />
                <Parallax />
                <Bikes />
                <Testimonials />
            </div>
        )
    }
}