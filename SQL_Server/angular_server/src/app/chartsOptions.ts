export class chartOptions {

  // pie grid options -----------------------
  animations = false
  minWidth = 150
  colorSchemePie = 'ocean'
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

}
