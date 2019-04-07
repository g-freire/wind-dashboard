import { Component } from '@angular/core';
import * as io from 'socket.io-client';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor() {
  }

  MarketStatus: any[];
  marketStatus: any[];

  private url = 'http://localhost:5000/wind';
  private socket;
  public monitor = 12
  public single: any[];
  title = 'Streaming';

  // pie grid options
  animations = false
  minWidth = 150
  colorSchemePie = 'ocean'
  designatedTotal = 100.0
  view: any[] = [750, 250];
  theme = 'dark';
  // horizontal bar options
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
      console.log('Wind Contract: ' + (data)["name"] + ' -- ' + (data)["rotorSpeed"] + ' -- ' + (data)["pf"]);
      
    this.monitor = data["rotorSpeed"]
    this.single = [
      {
        "name": "PUMP1",
        "value": this.monitor
      },
      {
        "name": "PUMP2",
        "value": this.monitor / 1.2
      },
      {
        "name": "PUMP3",
        "value": this.monitor * .4
      },
      {
        "name": "PUMP4",
        "value": this.monitor / 2
      },
      ];
    });
  }
  
  onSelect(event) {
    console.log(event);
  }
}
