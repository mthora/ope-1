import { AuthService } from 'src/app/services/auth.service';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductOrderService {
  private _urlProductOrders: string = `${environment.urlServer}products_orders/`
  constructor(private _httpClient: HttpClient, private _auth: AuthService) { }

  getProductOrders(order_id: number): Observable<any> {
    return this._httpClient.get(`${this._urlProductOrders}${order_id}`)
      .pipe(
        switchMap((response)=>{
          return of(response);
        })
      )
  }

}
