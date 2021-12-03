import { OrderService } from './../../services/order.service';
import { Component, Input, OnInit } from '@angular/core';
import { ProductOrderService } from 'src/app/services/product-order.service';

@Component({
  selector: 'app-current-order',
  templateUrl: './current-order.component.html',
  styleUrls: ['./current-order.component.scss']
})
export class CurrentOrderComponent implements OnInit {

  constructor(private _productOrder: ProductOrderService, private _order: OrderService) { }

  ngOnInit(): void {
    if (this.orderNumber != null){
      this.getOrderList(this.orderNumber);
    }

    console.log(this.orderDate)
  }

  orderList: any;
  orderDetails: any;
  total: number = 0;

  getOrderDetails(id: number){
    this._order.getOrderDetails(id).subscribe(
      (res)=>{
        console.log(res)
        this.orderDetails = res.data;
      },
      (err)=>{
        this.orderDetails = null;
        console.log(err)
      }
    )
  }

  confirm(id: number){
    this._order.confirmOrder(id).subscribe(
      (res)=>{
        console.log(res)
        window.location.reload();
      },
      (err)=>{
        console.log(err)
      }
    )
  }

  end(id: number){
    this._order.endOrder(id).subscribe(
      (res)=>{
        console.log(res)
        window.location.reload();
      },
      (err)=>{
        console.log(err)
      }
    )
  }

  getOrderList(id: number){
    this._productOrder.getProductOrders(id).subscribe(
      (res)=>{
        this.orderList = res.data
        console.log(this.orderList)
        let value = 0;
        for (let i of this.orderList){
          value+=i.price*(i.amount)
        }
        this.total = parseFloat((value+(value*0.10)).toFixed(2));
        console.log;
      },
      (err)=>{
        this.orderList = null;
        console.log(err);
      }
    )
  }

  @Input() orderNumber: number | null = null;
  @Input() orderLocal: any;
  @Input() orderDate: any;
  @Input() orderPayment: any;
  @Input() orderObs: any;
  @Input() orderConfirmed: boolean = false;
}
