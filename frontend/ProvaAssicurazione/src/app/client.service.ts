import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ClientService {
  private path = environment.apiUrl+'/json';
  constructor(private http: HttpClient) { }
  public client(): Observable<any> {
    return this.http.get<any>(`${this.path}`);
  }
}
