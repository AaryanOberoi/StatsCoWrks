import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import '../App.css';


class ButtonAppBar extends Component {
    constructor(styles) {
        super(styles);
    }
    render() {
        return (
            <AppBar position="static" className="appbarwala">
        <Toolbar>
          <Typography variant="title">
            User Statistics
          </Typography>
        </Toolbar>
      </AppBar>

        );
    }
}

export default ButtonAppBar;
