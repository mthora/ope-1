import { ProductsService } from './../../../services/products.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lanches-screen',
  templateUrl: './lanches-screen.component.html',
  styleUrls: ['./lanches-screen.component.scss']
})
export class LanchesScreenComponent implements OnInit {

  constructor(private _products : ProductsService) { }

  ngOnInit() {
    this.getProducts();
  }

  getProducts() : any {
    this._products.getProducts()
            .subscribe(
                (response) => {
                    console.log(response);
                    this.products = response.data;
                    this.lanches = this.products.filter((item)=>item.category==2)
                },
                (response) => {
                    console.log(response);
                }
            );
  }

  products: any[] = [];
  lanches: any[] = [];

}
