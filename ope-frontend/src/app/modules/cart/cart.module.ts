import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ComponentsModule } from 'src/app/components/components.module';
import { MatSidenavModule } from '@angular/material/sidenav';
import { CartConfirmScreenComponent } from './cart-confirm-screen/cart-confirm-screen.component';
import {MatRadioModule} from '@angular/material/radio';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatSelectModule} from '@angular/material/select';

@NgModule({
  declarations: [
    CartConfirmScreenComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule,
    MatIconModule,
    MatButtonModule,
    MatRadioModule,
    MatFormFieldModule,
    MatSelectModule
  ]
})
export class CartModule { }
