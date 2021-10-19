import { ProductsService } from 'src/app/services/products.service';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-new-item-screen',
  templateUrl: './new-item-screen.component.html',
  styleUrls: ['./new-item-screen.component.scss']
})
export class NewItemScreenComponent implements OnInit {

  constructor(private _auth: AuthService, private _router: Router, private _products: ProductsService) { }

  ngOnInit(): void {
    if (this._auth.getUserId()['role'] != 1) {
      this._router.navigateByUrl('cardapio');
    }
  }

  form = new FormGroup({
    name: new FormControl(''),
    description: new FormControl(''),
    category: new FormControl(0),
    price: new FormControl(0),
    amount: new FormControl(100),
    promotion: new FormControl(false)
  })

  selectFiles(event: any) {
    const reader = new FileReader();
    this.selectedFile = event.target?.files[0];
    reader.onload = (e: any) => {
      this.preview = e.target.result;
    }
    reader.readAsDataURL(this.selectedFile);
    this.name = this.selectedFile.name;
  }

  fileInputOpen(){
    document.getElementById('fileInput')?.click()
  }

  sendProduct(){
    const dataToSend = {
      'name': this.form.value.name,
      'description': this.form.value.description,
      'category': parseInt(this.form.value.category),
      'amount': this.form.value.amount,
      'price': this.form.value.price,
      'promotion': this.form.value.promotion
    }

    let id: any;

    console.log(dataToSend)
    this._products.createProduct(dataToSend).subscribe(
      (res) => {
        id =  res['id'];
        this._products.uploadImage(this.selectedFile, id).subscribe(
          (res) => {
            console.log(res),
            this._router.navigateByUrl('cardapio')
          },
          err => console.log(err)
        )
      },
      err => console.log(err)
    )
  }

  name: string = '';
  selectedFile!: File;
  preview!: string;
}
