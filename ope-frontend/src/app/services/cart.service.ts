import { AuthService } from 'src/app/services/auth.service';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  private _cart: any[] = [];
  constructor(private _auth: AuthService) { }

  set order(product_order: any)
  {
    localStorage.setItem('order', product_order);
  }

  get order(): any
  {
    const order = JSON.parse(localStorage.getItem('order') || '[]');
    return order;
  }

  addToCart(product_order: any): Observable<any>{

    const countProductInOrder = this._cart.filter((item)=>{
      const productInCart = JSON.parse(item);
      return productInCart["product_id"] == product_order["product_id"];
    })

    if (countProductInOrder.length != 0){
        this._cart = this._cart.filter((item)=>{
          const productInCart = JSON.parse(item);
          return ((productInCart["product_id"] != product_order["product_id"]));
        })
        this.order = JSON.stringify(this._cart);
    }

    if (product_order["amount"] === 0){
      this.order = JSON.stringify(this._cart);
      return of(this._cart);
    }

    this._cart.push(JSON.stringify(product_order));
    this.order = JSON.stringify(this._cart);
    return of(this._cart);
  }
}
