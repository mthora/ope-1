import { CartService } from './../../services/cart.service';
import { Component, OnChanges, OnInit } from '@angular/core';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss']
})
export class OrderComponent implements OnInit, OnChanges {

  constructor(private cart: CartService) { }

  ngOnInit(): void {
    this.createCart();
  }

  ngOnChanges() : void {
    this.createCart();
  }

  createCart(): void {
    for (let i of this.cart.order){
      const product_order = JSON.parse(i);
      this.orderList.push(product_order);
    }
  }

  orderList: any[] = []

}
