import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import Card from 'material-ui/Card';
import Typography from 'material-ui/Typography';
import '../App.css';
import Grid from 'material-ui/Grid';


class PaperSheet extends Component {
    render() {
        return (
            <div>
            <Grid container spacing={12}>
                <Grid item xs={12} sm={3}/>
                <Grid item xs={12} sm={3}>
                <Card className="paperwala" elevation={4}>
                    <Typography variant="headline" component="h3">
                    <br/>
                      720
                    </Typography>
                    <Typography component="p">
                      Devices Online
                    </Typography>
                </Card>
                </Grid>
                <Grid item xs={12} sm={3}>
                <Card className="paperwala" elevation={4}>
                    <Typography variant="headline" component="h3">
                    <br/>
                      720
                    </Typography>
                    <Typography component="p">
                      Users Online
                    </Typography>
                </Card>
                </Grid>
                <Grid item xs={12} sm={3}/>
                <Grid item xs={12} sm={3}/> 
                <Grid item xs={12} sm={6}>
                <Card className="paperwala" elevation={4}>
                    <Typography variant="headline" component="h3">
                    <br/>
                      1010
                    </Typography>
                    <Typography component="p">
                      App Installs
                    </Typography>
                </Card>
                </Grid>
            </Grid>    
        </div>
        );
    }
}


export default PaperSheet;
