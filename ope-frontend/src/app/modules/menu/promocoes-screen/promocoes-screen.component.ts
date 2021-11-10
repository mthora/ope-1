import { DomSanitizer } from '@angular/platform-browser';
import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { ProductsService } from 'src/app/services/products.service';

@Component({
  selector: 'app-promocoes-screen',
  templateUrl: './promocoes-screen.component.html',
  styleUrls: ['./promocoes-screen.component.scss']
})
export class PromocoesScreenComponent implements OnInit {

  constructor(private _products : ProductsService, private _auth: AuthService, private domSanitizer: DomSanitizer) { }

  ngOnInit() {
    this.getProducts();
    let user = this._auth.getUserId();
    let userRole = user['role'];
    this.admin = userRole == 1;
  }

  getProducts() : any {
    this._products.getProducts()
            .subscribe(
                (response) => {
                    console.log(response);
                    this.products = response.data;
                    this.promocoes = this.products.filter((item)=>item.promotion === true && item.amount > 0)
                },
                (response) => {
                    console.log(response);
                }
            );
  }

  decodeImg(dataURI: string) {
    let imageblob = atob(btoa(dataURI));
    let image = this.domSanitizer.bypassSecurityTrustUrl(`data:image/png;base64, ${imageblob}`);
    console.log('i', image)
    return image
   }

  admin = false;
  products: any[] = [];
  promocoes: any[] = [];

}
