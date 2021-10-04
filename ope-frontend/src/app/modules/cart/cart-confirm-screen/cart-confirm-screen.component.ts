import { CartService } from './../../../services/cart.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cart-confirm-screen',
  templateUrl: './cart-confirm-screen.component.html',
  styleUrls: ['./cart-confirm-screen.component.scss']
})
export class CartConfirmScreenComponent implements OnInit {

  constructor(private router: Router, private cart: CartService) { }

  ngOnInit(): void {
    this.hasProducts = this.cart.order.length != 0
    for (let i of this.cart.order) {
      this.sumList.push(parseFloat(JSON.parse(i).price) * parseInt(JSON.parse(i).amount))
    }
    this.orderSum = this.sumList.reduce((a, b) => a + b, 0);
    this.tip = this.orderSum*0.1;
  }

  hasProducts: boolean = false;
  sumList: any[] = [];
  orderSum: number = 0;
  tip: number = 0;

  deliveryOptions = ["Entrega na mesa", "Retirar no local"]

  navigate(screen: string): void{
    this.router.navigateByUrl(screen);
  }

}
