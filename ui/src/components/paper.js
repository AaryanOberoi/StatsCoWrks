import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Card from 'material-ui/Card';
import Typography from 'material-ui/Typography';
import '../App.css';
import Grid from 'material-ui/Grid';
import dataFetch from './apicall';

var refresh_interval = 60000; // 1 min

class PaperSheet extends Component {
	constructor(props){
        super(props);
        this.state={
            userCount: 0,
            deviceCount: 0,
            epochTime: 0
        };
        this.callBack = this.callBack.bind(this)
        this.callapi = this.callapi.bind(this)
        this.callapi();
    }
    callBack(data){
        console.log(data)
        this.setState({
            deviceCount: data.dev,
            userCount: data.user,
            epochTime: data.epoch
        })
        setInterval(this.callapi, refresh_interval)
    }
    callapi(){
        dataFetch(this.callBack);
    }
    render() {
        return (
            <div>
                <Grid item xs={6} sm={6}>
                    <Card className="paperwala" elevation={4}>
                        <Typography variant="headline" component="h3">
                        <br/>
                        <div>{this.state.deviceCount}</div>
                        </Typography>
                        <Typography component="p">
                        Devices Online
                        </Typography>
                    </Card>
                </Grid>
                <Grid item xs={6} sm={6}>
                    <Card className="paperwala" elevation={4}>
                        <Typography variant="headline" component="h3">
                        <br/>
                        <div>{this.state.userCount}</div>
                        </Typography>
                        <Typography component="p">
                        Users Online
                        </Typography>
                    </Card>
                </Grid>   
            </div>
        );
    }
}


export default PaperSheet;
