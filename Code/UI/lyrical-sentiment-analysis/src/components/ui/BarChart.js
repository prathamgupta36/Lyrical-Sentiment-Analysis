import React from 'react';
import ApexCharts from 'react-apexcharts';

class BarChart extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			series: props.results.map(x => Math.round(x[1]*100000)/100000),
			options: {
				chart: {
					height: '40%',
					type: 'donut'
				},
				labels: props.results.map(x => x[0]),
				colors: ['#008FFB', '#FD6A6A'],
				height: '40%'
			},
			height: '40%'
		};
	}
	render() {
		return (
			<div style={{ display: 'flex', justifyContent: 'center' }}>
				<div id="chart" style={{ width: '400px'}}> 
					<ApexCharts options={this.state.options} series={this.state.series} type="donut" />
				</div>
				<div id="html-dist"></div>
			</div>
		);
	}
}

export default BarChart;