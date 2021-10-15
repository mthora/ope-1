import { CartService } from './../../services/cart.service';
import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss']
})
export class OrderComponent implements OnInit {

  constructor(private cart: CartService) { }

  ngOnInit(): void {
    this.createCart();
  }

  @Output() cartUpdateEvent = new EventEmitter();

  createCart(): void {
    for (let i of this.cart.order){
      try {
        const product_order = JSON.parse(i);
        this.orderList.push(product_order);
      } catch {
        try{
          const product_order = i;
          this.orderList.push(product_order);
        } catch {
          console.log("deu ruim");
        }
      }
    }
  }

  removeAmount(e: any, product_id: number){
    let product = this.orderList.filter(item => item.product_id == product_id)[0]
    if (product.amount > 1){
      product.amount-=1
    } else {
      this.orderList = this.orderList.filter(item => item.product_id != product_id)
    }
    this.updateCart(this.orderList);
    this.cartUpdateEvent.emit(this.orderList);
  }

  addAmount(e: any, product_id: number){
    let product = this.orderList.filter(item => item.product_id == product_id)[0]

    product.amount+=1
    this.updateCart(this.orderList);
    this.cartUpdateEvent.emit(this.orderList);
  }

  updateCart(order: any[]){
    this.cart.updateCart(order)
    .subscribe(
        (response) => {

        },
        () => {
            console.log("deu ruim");
        }
    );
  }

  orderList: any[] = []

}
