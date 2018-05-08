import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import { withStyles } from 'material-ui/styles';
import Typography from 'material-ui/Typography';
import Button from 'material-ui/Button';
import IconButton from 'material-ui/IconButton';
import '../App.css';

const styles = {
    root: {
        flexGrow: 1,
    },
    flex: {
        flex: 1,
    },
};

class ButtonAppBar extends Component {
    constructor(styles) {
        super(styles);
        console.log(styles);
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
