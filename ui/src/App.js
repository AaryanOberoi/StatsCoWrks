import React, { Component } from 'react';
import './App.css';
import ButtonAppBar from './components/appbar';
import PaperSheet from './components/paper';



class App extends Component {
    render() {
        return (
            <div>
	            <ButtonAppBar/>
	            <PaperSheet/>
            </div>
        );
    }
}

export default App;
