import { ProductsService } from './../../../services/products.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-bebidas_sobremesas-screen',
  templateUrl: './bebidas_sobremesas-screen.component.html',
  styleUrls: ['./bebidas_sobremesas-screen.component.scss']
})
export class Bebidas_SobremesasScreenComponent implements OnInit {

  constructor(private _products: ProductsService) { }

  ngOnInit() {
    this.getProducts();
  }

  getProducts() : any {
    this._products.getProducts()
            .subscribe(
                (response) => {
                    console.log(response);
                    this.products = response.data;
                    this.bebidas_sobremesas = this.products.filter((item)=>item.category=="bebida_sobremesa")
                },
                (response) => {
                    console.log(response);
                }
            );
  }

  products: any[] = [];
  bebidas_sobremesas: any[] = [];
}
