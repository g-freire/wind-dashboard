import { Component } from '@angular/core';
import * as io from 'socket.io-client';
import { chartOptions } from './chartsOptions';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor() {
  }

  private socket;
  private url = 'http://localhost:5000/wind';


  public chartDataSchemaPie: any[];
  public chartDataSchemaRPMGauge: any[];
  public chartDataSchemaRPMGauge2: any[];

  public chartOptions // need to extract and import this class

  // wind contract
  private name: string
  private rotorSpeed: string
  private activePower: string
  private reactivePower: string
  private pf: string
  private totalEnergy: string
  private windPrediction1: string
  private windPrediction2: string
  private windPrediction3: string
  private bearingTemperature: string
  private bearingVibration: string
  private bearingOil: string

  // gauge options -----------------------
  gaugeView: any[] = [750, 300]
  gaugeColorSchemePie = 'forest'
  gaugeMin = 0
  gaugeMax = 300
  gaugeUnits = "GW"
  gaugeUnits2 = "RPM"
  gaugeStartAngle = -90
  gaugeEndAngle = 180
  // gaugeLegend = true
  // gaugeLegendTitle = "Generated Power"
  
  gaugeColorSchemePie2 = 'ocean'


  // pie grid options -----------------------
  animations = false
  minWidth = 150
  // colorSchemePie = 'forest'
  colorSchemePie = 'fire'
  designatedTotal = 100.0
  view: any[] = [750, 250];
  theme = 'dark';

  // horizontal bar options -----------------------
  viewHotizontal: any[] = [800, 250];
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = true;
  showXAxisLabel = true;
  xAxisLabel = 'Pressure';
  showYAxisLabel = true;
  yAxisLabel = 'Pump Data';
  showGridLines = true
  yAxisTicks = [10, 20, 30, 40, 50, 60, 70, 80, 90]
  xScaleMin = 0
  xScaleMax = 100
  // schemeType = 'linear'
  scheme = 'ocean'
  colorScheme = {
    domain: ['#1d68fb', '#33c0fc', '#4afffe', '#5d7f84']
  };
  ngOnInit(): void {
    this.socket = io.connect(this.url);
    this.socket.on('wind', (data) => {
      console.log('Wind Contract: ' +
        "rotorSpeed " + data["rotorSpeed"] + ' - ' +
        "activePower " + data["activePower"] + ' - ' +
        "reactivePower " + data["reactivePower"] + ' - ' +
        "windPrediction1 " + data["windPrediction1"] + ' - ' +
        "windPrediction2 " + data["windPrediction2"] + ' - ' +
        "bearingOil " + data["bearingOil"] + ' - ' +
        "bearingVibration " + data["bearingVibration"] + ' - ' +
        "bearingTemperature " + data["bearingTemperature"] + ' - ' +
        "totalEnergy " + data["totalEnergy"]);

      this.name = data["name"]
      this.rotorSpeed = data["rotorSpeed"]
      this.activePower = data["activePower"]
      this.reactivePower = data["reactivePower"]
      this.pf = data["pf"]
      this.totalEnergy = data["totalEnergy"]
      this.windPrediction1 = data["windPrediction1"]
      this.windPrediction2 = data["windPrediction2"]
      this.windPrediction3 = data["windPrediction3"]
      this.bearingTemperature = data["bearingTemperature"]
      this.bearingVibration = data["bearingVibration"]
      this.bearingOil = data["bearingOil"]

      this.chartDataSchemaRPMGauge = [
        {
          "name": "bearingOil",
          "value": this.bearingOil
        },
        {
          "name": "bearingOil",
          "value": this.bearingOil
        },
        {
          "name": "bearingOil",
          "value": this.bearingOil
        },
      ];

      this.chartDataSchemaRPMGauge2 = [
        {
          "name": "bearingOil",
          "value": this.bearingTemperature
        },
        {
          "name": "bearingOil",
          "value": this.bearingTemperature
        },
        {
          "name": "bearingOil",
          "value": this.bearingTemperature
        },
      ];

      this.chartDataSchemaPie = [
        {
          "name": "bearingOil",
          "value": this.bearingOil
        },
        {
          "name": "activePower",
          "value": this.activePower
        },
        {
          "name": "bearingTemperature",
          "value": this.bearingTemperature
        },
        {
          "name": "reactivePower",
          "value": this.reactivePower
        },
        {
          "name": "windPrediction1",
          "value": this.windPrediction1
        },
        {
          "name": "windPrediction2",
          "value": this.windPrediction2
        },
        {
          "name": "bearingOil",
          "value": this.bearingOil
        },
        {
          "name": "activePower",
          "value": this.activePower
        },
      ];
    });
  }

  onSelect(event) {
    console.log(event);
  }
}
