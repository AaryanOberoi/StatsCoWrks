import React from 'react';
import $ from 'jquery';

// const dataFetch = ({userCount, deviceCount, epochTime}) => {
//   return(
//     // console.log('Component will mount', this.state)
//     fetch('http://127.0.0.1:5000', {method: 'GET'})
//     .then(response => response.json())
//     .catch(error => console.log('Error is ', error))
//     .then(resp => this.setState({
//         deviceCount: resp.dev,
//         userCount: resp.user,
//         epochTime: resp.epoch
//     }))
//   )
// }

// export default dataFetch;
export default function dataFetch(callBack,refreshData) {
    $.ajax({
      type: 'GET',
      url: 'http://127.0.0.1:8000',
      success: function(data) {
        callBack(data);
      },
      error: function(e, x) {
        console.log("Coudn't communicate to local server")
      },
    });
  }