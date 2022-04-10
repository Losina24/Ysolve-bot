import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RosService {

  api: string = 'http://localhost:8080/ros';

  constructor(private _httpClient: HttpClient) {}

  moveForward(): Observable<any> {
    return this._httpClient.get(`${this.api}/manual/move/forward`)
  }

  moveBack(): Observable<any> {
    return this._httpClient.get(`${this.api}/manual/move/back`)
  }

  moveRight(): Observable<any> {
    return this._httpClient.get(`${this.api}/manual/move/right`)
  }

  moveLeft(): Observable<any> {
    return this._httpClient.get(`${this.api}/manual/move/left`)
  }

  stopMove(): Observable<any> {
    return this._httpClient.get(`${this.api}/manual/move/stop`)
  }

  connect(): Observable<any> {
    return this._httpClient.get(`${this.api}/manual/connect`)
  }

  disconnect(): Observable<any> {
    return this._httpClient.get(`${this.api}/manual/disconnect`)
  }
}
