import { AuthService } from 'src/app/services/auth.service';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private _urlOrder: string = `${environment.urlServer}orders/`
  constructor(private _httpClient: HttpClient, private _auth: AuthService) { }

  getOrderDetails(order_id: number): Observable<any> {
    return this._httpClient.get(`${this._urlOrder}${order_id}`)
      .pipe(
        switchMap((response)=>{
          return of(response);
        })
      )
  }

  confirmOrder(order_id: number): Observable<any> {
    return this._httpClient.patch(`${this._urlOrder}`, {"id": order_id, "confirmed":true})
      .pipe(
        switchMap((response)=>{
          return of(response);
        })
      )
  }

  endOrder(order_id: number): Observable<any> {
    return this._httpClient.put(`${this._urlOrder}`, {"id": order_id, "done":true})
      .pipe(
        switchMap((response)=>{
          return of(response);
        })
      )
  }

  listOrders(): Observable<any> {
    return this._httpClient.get(`${this._urlOrder}`)
      .pipe(
        switchMap((response)=>{
          return of(response);
        })
      )
  }

}
