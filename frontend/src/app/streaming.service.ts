import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

// import {MarketPrice} from './market-price';
import { Subject, from } from  'rxjs';
import * as socketio from 'socket.io-client';

@Injectable({
  providedIn: 'root'
})
export class MarketStatusService {

  private baseUrl =  'http://localhost:5000/test';
  constructor(private httpClient: HttpClient) { }

  getInitialMarketStatus() {
    return this.httpClient.get<any[]>(`${this.baseUrl}`);
    debugger
  }

  getUpdates() {
    let socket = socketio(this.baseUrl);
    let marketSub = new Subject<any>();
    let marketSubObservable = from(marketSub);

    socket.on('newnumber', (marketStatus: any) => {
      marketSub.next(marketStatus);
    });
    debugger
    return marketSubObservable;
  }
}