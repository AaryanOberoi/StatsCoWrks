import React, { Component } from 'react';
import './App.css';
import ButtonAppBar from './components/appbar';
import PaperSheet from './components/paper';
import Welcome from './components/division';


class App extends Component {
    render() {
        return (
            <div>
            <ButtonAppBar/>
            <PaperSheet/>
            <Welcome/>
            </div>

        );
    }
}

export default App;
