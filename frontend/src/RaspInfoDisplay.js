import React from 'react';
import Request from 'superagent'
import './css/RaspInfoDisplay.css';

class RaspInfoDisplay extends React.Component {

    constructor() {
        super();
        this.state = {}
        this._getWidgetInfo = this._getWidgetInfo.bind(this);
    }

    render() {
        return (
            <div className="display-wrapper">
                <div className="weather">
                    { this._getWidgetInfo('weather') }
                </div>
            </div>
        );
    }



    _getWidgetInfo(widget_name) {
        var url = `http://127.0.0.1:5000/${widget_name}`;

        Request.get(url).then((response) => {
            console.log(response.body)
            this.setState({
                widget_name: response.body
            })
        });
    }
}

export default RaspInfoDisplay;
