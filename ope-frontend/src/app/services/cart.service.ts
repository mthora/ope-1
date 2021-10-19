import { AuthService } from 'src/app/services/auth.service';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { switchMap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private _urlOrders: string = `${environment.urlServer}orders/`
  private _urlProductsInOrder: string = `${environment.urlServer}products_orders/`
  private _cart: any[] = [];
  constructor(private _auth: AuthService, private _httpClient: HttpClient) { }

  set order(product_order: any)
  {
    localStorage.setItem('order', JSON.stringify(product_order));
  }

  get order(): any
  {
    const order = JSON.parse(localStorage.getItem('order') || '[]');
    return order;
  }

  emptyCart() : void {
    this._cart = []
    this.order = this._cart
  }

  updateCart(order: any[]) : Observable<any> {
    console.log("service",order)
    this._cart = order;
    this.order = this._cart;
    console.log("upd", this.order);
    return of(this._cart);
  }

  addToCart(product_order: any): Observable<any>{

    const countProductInOrder = this._cart.filter((item)=>{
    const productInCart = item;
    return productInCart["product_id"] == product_order["product_id"];
    })

    if (countProductInOrder.length != 0){
        this._cart = this._cart.filter((item)=>{
            const productInCart = item;
            return ((productInCart["product_id"] != product_order["product_id"]));
        })
        this.order = this._cart;
    }

    if (product_order["amount"] === 0){
      this.order = this._cart;
      return of(this._cart);
    }

    this._cart.push(product_order);
    this.order = this._cart;
    return of(this._cart);
  }

  addProductOrder(product_order: any) : Observable<any>{
    return this._httpClient.post(this._urlProductsInOrder, product_order, {headers: new HttpHeaders()
      .set('Authorization', `Bearer ${this._auth.accessToken}`)})
      .pipe(
        switchMap((response: any) => {
            console.log(response);
            return of(response);
        })
    );
  }

  sendOrder(order: any) : Observable<any> {
    return this._httpClient.post(this._urlOrders, order, {headers: new HttpHeaders()
      .set('Authorization', `Bearer ${this._auth.accessToken}`)})
      .pipe(
        switchMap((response: any) => {
            console.log(response);
            return of(response.data);
        })
    );
  }
}
