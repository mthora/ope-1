import { ProductsService } from './../../../services/products.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-plates-screen',
  templateUrl: './plates-screen.component.html',
  styleUrls: ['./plates-screen.component.scss']
})
export class PlatesScreenComponent implements OnInit {

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
                    this.plates = this.products.filter((item)=>item.category=="prato")
                },
                (response) => {
                    console.log(response);
                }
            );
  }

  products: any[] = [];
  plates: any[] = [];
}
