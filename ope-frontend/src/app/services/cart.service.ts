import { AuthService } from 'src/app/services/auth.service';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private _urlProducts: string = `${environment.urlServer}product_orders/`
  private _cart: any[] = [];
  constructor(private _httpClient: HttpClient, private _auth: AuthService) { }

  set order(product_order: string)
  {
    localStorage.setItem('order', product_order);
  }

  get order(): string
  {
    const order = JSON.parse(localStorage.getItem('order') || '[]');
    return order;
  }

  addToCart(product_order: any): Observable<any>{
    this._cart.push(JSON.stringify(product_order));
    this.order = JSON.stringify(this._cart);
    return of(this._cart);
  }
}
